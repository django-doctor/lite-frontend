from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest, HttpResponseServerError
from django.shortcuts import redirect
from django.views.generic.base import RedirectView, View, TemplateView
from lite_forms.generators import error_page
from raven.contrib.django.raven_compat.models import client

from auth.services import authenticate_exporter_user
from authbroker_client.utils import get_client, AUTHORISATION_URL, TOKEN_URL, TOKEN_SESSION_KEY, get_profile
from conf.settings import LOGOUT_URL
from core.builtins.custom_tags import get_string
from users.services import get_user


class AuthView(RedirectView):
    """
    Auth wrapper which connects to api
    """

    permanent = False

    def get_redirect_url(self, *args, **kwargs):

        authorization_url, state = get_client(self.request).authorization_url(AUTHORISATION_URL)

        self.request.session[TOKEN_SESSION_KEY + "_oauth_state"] = state

        return authorization_url


class AuthCallbackView(View):
    """
    Auth process for exporter, only called by 'great sso'
    """

    def get(self, request, *args, **kwargs):
        auth_code = request.GET.get("code", None)

        if not auth_code:
            return HttpResponseBadRequest()

        state = self.request.session.get(TOKEN_SESSION_KEY + "_oauth_state", None)

        if not state:
            return HttpResponseServerError()

        try:
            token = get_client(self.request).fetch_token(
                TOKEN_URL, client_secret=settings.AUTHBROKER_CLIENT_SECRET, code=auth_code
            )

            self.request.session[TOKEN_SESSION_KEY] = dict(token)

            del self.request.session[TOKEN_SESSION_KEY + "_oauth_state"]

        # NOTE: the BaseException will be removed or narrowed at a later date. The try/except block is
        # here due to reports of the app raising a 500 if the url is copied.  Current theory is that
        # somehow the url with the authcode is being copied, which would cause `fetch_token` to raise
        # an exception. However, looking at the fetch_code method, I'm not entirely sure what exceptions it
        # would raise in this instance.
        except BaseException:
            client.captureException()

        profile = get_profile(get_client(self.request))

        response, status_code = authenticate_exporter_user(profile)
        if status_code != 200:
            return error_page(
                None,
                title=get_string("authentication.user_does_not_exist.title"),
                description=get_string("authentication.user_does_not_exist.description"),
                show_back_link=False,
            )

        # Create the user in the session
        user = authenticate(request)
        user.user_token = response["token"]
        user.first_name = response["first_name"]
        user.last_name = response["last_name"]
        user.lite_api_user_id = response["lite_api_user_id"]
        user.organisation = None
        user.save()

        if user is not None:
            login(request, user)

            user_dict, _ = get_user(request)

            if len(user_dict["user"]["organisations"]) == 0:
                return error_page(request, "You don't belong to any organisations", show_back_link=False)
            elif len(user_dict["user"]["organisations"]) == 1:
                user.organisation = user_dict["user"]["organisations"][0]["id"]
                user.save()
            elif len(user_dict["user"]["organisations"]) > 1:
                return redirect("core:pick_organisation")

        return redirect(getattr(settings, "LOGIN_REDIRECT_URL", "/"))


class AuthLogoutView(TemplateView):
    def get(self, request, **kwargs):
        request.user.delete()
        logout(request)
        return redirect(LOGOUT_URL + "https://" + request.get_host())
