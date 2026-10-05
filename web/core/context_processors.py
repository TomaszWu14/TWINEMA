from django.conf import settings

from .roles import GROUP_ADMIN, GROUP_DESIGNER


def branding(request):
    return {"app_name": settings.APP_NAME}


def user_roles(request):
    """Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()."""
    user = getattr(request, "user", None)
    if not user or not user.is_authenticated:
        return {"is_admin": False, "is_designer": False}
    if user.is_superuser:
        return {"is_admin": True, "is_designer": True}
    names = set(user.groups.values_list("name", flat=True))
    is_admin = GROUP_ADMIN in names
    return {"is_admin": is_admin, "is_designer": is_admin or GROUP_DESIGNER in names}
