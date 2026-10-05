from django.urls import path

from . import views

app_name = "studio"

urlpatterns = [
    path("studio/", views.presentation_list, name="list"),
    path("studio/nowa/", views.presentation_create, name="create"),
    path("studio/<int:pk>/", views.presentation_detail, name="detail"),
    path("studio/<int:pk>/kwestie/", views.shots_save, name="shots_save"),
    path("studio/<int:pk>/szkic-ai/", views.shots_ai, name="shots_ai"),
    path("studio/<int:pk>/szkic-szablon/", views.shots_template, name="shots_template"),
    path("studio/<int:pk>/zatwierdz/", views.approve, name="approve"),
    path("studio/<int:pk>/edycja/", views.reopen, name="reopen"),
    path("studio/<int:pk>/usun/", views.presentation_delete, name="delete"),
    path("studio/<int:pk>/lektor/<int:shot_pk>/", views.voice_shot, name="voice_shot"),
    path("studio/<int:pk>/napisy.srt", views.subtitles, name="subtitles"),
    path("studio/lektor/<int:pk>.mp3", views.voice_file, name="voice_file"),
]
