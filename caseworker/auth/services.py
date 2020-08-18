from caseworker.core.client import post
from caseworker.core.constants import AUTHENTICATION_URL


def authenticate_gov_user(request, json):
    data = post(request, AUTHENTICATION_URL, json)
    return data.json(), data.status_code
