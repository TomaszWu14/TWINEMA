from django.urls import path

from . import views

app_name = "scenario"

urlpatterns = [
    path("scenariusze/", views.scenario_list, name="list"),
    path("scenariusze/nowy/", views.scenario_create, name="create"),
    path("scenariusze/<int:pk>/", views.scenario_detail, name="detail"),
    path("scenariusze/<int:pk>/parametry/", views.scenario_save, name="save"),
    path("scenariusze/<int:pk>/przyjecia/<str:kind>/", views.day_save, name="day_save"),
    path("scenariusze/<int:pk>/kopia/", views.scenario_copy, name="copy"),
    path("scenariusze/<int:pk>/usun/", views.scenario_delete, name="delete"),
]
