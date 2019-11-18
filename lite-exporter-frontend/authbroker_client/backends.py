import logging
from django.contrib.auth import get_user_model
from authbroker_client.utils import get_client, has_valid_token, get_profile


logger = logging.getLogger("authbroker-client")


class AuthbrokerBackend:
    def authenticate(self, request, **kwargs):
        client = get_client(request)
        if has_valid_token(client):
            User = get_user_model()

            profile = get_profile(client)

            user, created = User.objects.get_or_create(email=profile["email"])
            if created:
                setattr(user, user.USERNAME_FIELD, profile["email"])
                user.set_unusable_password()
                user.save()
            return user

        return None

    def get_user(self, user_id):
        User = get_user_model()

        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
