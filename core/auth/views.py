import abc

from django.conf import settings
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseServerError
from django.shortcuts import redirect
from django.utils.functional import cached_property
from django.urls import reverse
from django.views.generic import RedirectView
from django.views.generic.base import View

from core.auth.utils import get_profile


class AuthView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        url, state = self.request.authbroker_client.authorization_url(settings.AUTHBROKER_AUTHORIZATION_URL)
        self.request.session[f"{settings.TOKEN_SESSION_KEY}_oauth_state"] = state
        return url


class AuthLogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        self.request.session.flush()
        return settings.LOGOUT_URL + self.request.build_absolute_uri("/")


class AbstractAuthCallbackView(abc.ABC, View):
    @abc.abstractmethod
    def handle_failure(self, data, status_code):
        pass

    @abc.abstractmethod
    def handle_success(self, data, status_code):
        pass

    @abc.abstractmethod
    def authenticate_user(self):
        pass

    @cached_property
    def user_profile(self):
        return get_profile(self.request.authbroker_client)

    def get(self, request, *args, **kwargs):
        auth_code = request.GET.get("code", None)
        if not auth_code:
            return redirect(reverse("auth:login"))
        state = self.request.session.get(f"{settings.TOKEN_SESSION_KEY}_oauth_state", None)
        if not state:
            return HttpResponseServerError()
        token = request.authbroker_client.fetch_token(
            settings.AUTHBROKER_TOKEN_URL, client_secret=settings.AUTHBROKER_CLIENT_SECRET, code=auth_code
        )
        self.request.session[settings.TOKEN_SESSION_KEY] = dict(token)
        del self.request.session[f"{settings.TOKEN_SESSION_KEY}_oauth_state"]
        data, status_code = self.authenticate_user()

        if status_code == 200:
            return self.handle_success(data=data, status_code=status_code)
        return self.handle_failure(data=data, status_code=status_code)


class LoginRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.authbroker_client.authorized

    def handle_no_permission(self):
        # overridden to handle absense of request.user
        if self.raise_exception or self.test_func():
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect_to_login(self.request.get_full_path(), self.get_login_url(), self.get_redirect_field_name())
