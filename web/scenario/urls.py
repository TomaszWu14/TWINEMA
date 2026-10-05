from django.urls import path

from . import views, views_compare, views_play, views_showcase, views_sim

app_name = "scenario"

urlpatterns = [
    path("prezentacje/", views_showcase.showcase_list, name="showcase_list"),
    path("prezentacje/nowa/", views_showcase.showcase_create, name="showcase_create"),
    path("prezentacje/<int:pk>/", views_showcase.showcase_detail, name="showcase"),
    path("prezentacje/<int:pk>/dane.json", views_showcase.showcase_data, name="showcase_data"),
    path("prezentacje/<int:pk>/zapisz/", views_showcase.showcase_save, name="showcase_save"),
    path("prezentacje/<int:pk>/szablon/", views_showcase.showcase_reset, name="showcase_reset"),
    path("prezentacje/<int:pk>/usun/", views_showcase.showcase_delete, name="showcase_delete"),
    path("scenariusze/<int:pk>/symulacja/", views_sim.scenario_simulate, name="simulate"),
    path("scenariusze/symulacja/<int:pk>/zdarzenia.json", views_sim.run_events, name="run_events"),
    path("scenariusze/symulacja/<int:pk>/wyniki.xlsx", views_compare.run_xlsx, name="run_xlsx"),
    path("scenariusze/porownanie/", views_compare.compare, name="compare"),
    path("scenariusze/symulacja/<int:pk>/animacja/", views_play.run_play, name="run_play"),
    path("scenariusze/", views.scenario_list, name="list"),
    path("scenariusze/nowy/", views.scenario_create, name="create"),
    path("scenariusze/demo/", views.scenario_demo, name="demo"),
    path("scenariusze/<int:pk>/", views.scenario_detail, name="detail"),
    path("scenariusze/<int:pk>/parametry/", views.scenario_save, name="save"),
    path("scenariusze/<int:pk>/przyjecia/<str:kind>/", views.day_save, name="day_save"),
    path("scenariusze/<int:pk>/wydania/<str:kind>/", views.outbound_save, name="outbound_save"),
    path("scenariusze/<int:pk>/obsada/", views.shifts_save, name="shifts_save"),
    path("scenariusze/<int:pk>/kopia/", views.scenario_copy, name="copy"),
    path("scenariusze/<int:pk>/usun/", views.scenario_delete, name="delete"),
]
