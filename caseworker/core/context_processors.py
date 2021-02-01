import os

from django.urls import reverse

from caseworker.core.constants import Permission
from caseworker.core.services import get_user_permissions, get_menu_notifications
from lite_content.lite_internal_frontend import strings, open_general_licences
from lite_content.lite_internal_frontend.flags import FlagsList
from lite_content.lite_internal_frontend.organisations import OrganisationsPage
from lite_content.lite_internal_frontend.queues import QueuesList
from lite_content.lite_internal_frontend.teams import TeamsPage
from lite_content.lite_internal_frontend.users import UsersPage
from lite_forms.helpers import conditional
from caseworker.queues.services import get_queue


def current_queue(request):
    kwargs = getattr(request.resolver_match, "kwargs", {})
    if "queue_pk" in kwargs and "disable_queue_lookup" not in kwargs:
        queue_pk = request.resolver_match.kwargs["queue_pk"]
        queue = get_queue(request, queue_pk)
        return {"queue": queue}

    return {}


def export_vars(request):
    return {
        "ENVIRONMENT_VARIABLES": dict(os.environ.items()),
        "CURRENT_PATH": request.get_full_path(),
        "CURRENT_PATH_WITHOUT_PARAMS": request.get_full_path().split("?")[0].split("#")[0],
        "CURRENT_PATH_ONLY_PARAMS": "?" + request.get_full_path().split("?")[1]
        if "?" in request.get_full_path()
        else "",
    }


def lite_menu(request):
    has_notifications = False
    if "lite_api_user_id" in request.session:
        permissions = get_user_permissions(request)
        notifications = get_menu_notifications(request)
        notification_data = notifications["notifications"]
        has_notifications = notifications["has_notifications"]
        pages = [
            {"title": "Cases", "url": reverse("core:index"), "icon": "menu/cases"},
            {
                "title": OrganisationsPage.TITLE,
                "url": reverse("organisations:organisations"),
                "icon": "menu/businesses",
                "notifications": notification_data.get("organisations"),
            },
            {"title": TeamsPage.TITLE, "url": reverse("teams:teams"), "icon": "menu/teams"},
            {"title": "My Team", "url": reverse("teams:team"), "icon": "menu/teams"},
            {"title": QueuesList.TITLE, "url": reverse("queues:manage"), "icon": "menu/queues"},
            {"title": UsersPage.TITLE, "url": reverse("users:users"), "icon": "menu/users"},
            {"title": FlagsList.TITLE, "url": reverse("flags:flags"), "icon": "menu/flags"},
            conditional(
                Permission.MAINTAIN_OGL.value in permissions,
                {
                    "title": open_general_licences.List.TITLE,
                    "url": reverse("open_general_licences:open_general_licences"),
                    "icon": "menu/open-general-licences",
                },
            ),
            conditional(
                Permission.CONFIGURE_TEMPLATES.value in permissions,
                {
                    "title": strings.DOCUMENT_TEMPLATES_TITLE,
                    "url": reverse("letter_templates:letter_templates"),
                    "icon": "menu/letter-templates",
                },
            ),
            conditional(
                Permission.MANAGE_FLAGGING_RULES.value in permissions,
                {"title": "Flagging rules", "url": reverse("flags:flagging_rules"), "icon": "menu/flags"},
            ),
            conditional(
                Permission.MANAGE_TEAM_ROUTING_RULES.value in permissions
                or Permission.MANAGE_ALL_ROUTING_RULES.value in permissions,
                {"title": "Routing rules", "url": reverse("routing_rules:list"), "icon": "menu/routing-rules"},
            ),
            {"title": "Denial records", "url": reverse("external_data:denials-upload"), "icon": "menu/cases"},
        ]
    else:
        pages = []
    return {"LITE_MENU": [x for x in pages if x is not None], "MENU_NOTIFICATIONS": has_notifications}
