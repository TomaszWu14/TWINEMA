from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

urlpatterns = [
    path("robots.txt", lambda r: HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")),
    path("admin/", admin.site.urls),
    path("health/", include("core.health_urls")),
    path("", include("core.urls")),
    path("", include("masterdata.urls")),
    path("", include("twin.urls")),
    path("", include("render.urls")),
]
