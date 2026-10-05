from functools import wraps

# ── ZAMROŻONY KONTRAKT: nazwy grup ───────────────────────────────────────────
# Stringi po prawej to wiersze w tabeli auth_group. Zmiana stringu = nowa, pusta grupa
# i cichy odpływ uprawnień. Identyfikator po lewej wolno refaktorować, stringu nie.
# Pilnuje tego core/tests/test_group_contract.py.
GROUP_ADMIN = "Administratorzy"
GROUP_DESIGNER = "Projektant"      # modeluje hale, warianty, symulacje, prezentacje
GROUP_VIEWER = "Podgląd"           # ogląda gotowe modele i filmy (zarząd, rekruter)

ALL_GROUPS = [GROUP_ADMIN, GROUP_DESIGNER, GROUP_VIEWER]


def has_role(user, *group_names):
    """True dla superusera albo członka którejś z grup."""
    if not user or not user.is_authenticated:
        return False
    if user.is_superuser:
        return True
    return user.groups.filter(name__in=group_names).exists()


def role_required(*group_names):
    """Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze przechodzi)."""
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated:
                from django.contrib.auth.views import redirect_to_login
                return redirect_to_login(request.get_full_path())
            if has_role(request.user, *group_names):
                return view_func(request, *args, **kwargs)
            from django.shortcuts import render
            return render(request, "core/403.html", status=403)
        return wrapped
    return decorator


admin_only = role_required(GROUP_ADMIN)
designer = role_required(GROUP_ADMIN, GROUP_DESIGNER)
any_role = role_required(*ALL_GROUPS)
