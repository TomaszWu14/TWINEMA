from django.urls import path

from . import api, views

app_name = "render"

urlpatterns = [
    path("render/", views.jobs, name="jobs"),
    path("render/nowy/", views.create, name="create"),
    path("render/status.json", views.status_json, name="status_json"),
    path("render/<int:pk>/plik/", views.result_file, name="result_file"),
    path("render/<int:pk>/usun/", views.delete, name="delete"),
    path("api/render/claim/", api.claim, name="api_claim"),
    path("api/render/<int:pk>/scene.json", api.scene, name="api_scene"),
    path("api/render/<int:pk>/result/", api.result, name="api_result"),
    path("api/render/<int:pk>/fail/", api.fail, name="api_fail"),
]
