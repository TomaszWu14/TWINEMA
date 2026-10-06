from django.conf import settings
from django.db import connection
from django.http import JsonResponse
from django.urls import path
from django.utils import timezone


def health(request):
    """DB ping + wersja (git SHA z build-argu) — smoke po deployu czeka na NOWY SHA."""
    try:
        connection.ensure_connection()
        db_ok = True
    except Exception:
        db_ok = False
    return JsonResponse({
        "status": "ok" if db_ok else "degraded",
        "db": "ok" if db_ok else "error",
        "version": settings.GIT_SHA,
        "time": timezone.now().isoformat(),
    }, status=200 if db_ok else 503)


urlpatterns = [path("", health, name="health")]
