from exporter.conf.client import post
from exporter.conf.constants import AUTHENTICATION_URL


def authenticate_exporter_user(request, json):
    data = post(request, AUTHENTICATION_URL, json)
    return data.json(), data.status_code