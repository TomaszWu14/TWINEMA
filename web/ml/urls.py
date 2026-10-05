from django.urls import path

from . import views

app_name = "ml"

urlpatterns = [
    path("ml/", views.home, name="home"),
    path("ml/uruchom/<str:kind>/", views.run, name="run"),
    path("ml/<int:pk>/", views.detail, name="detail"),
    path("ml/<int:pk>/segmenty.csv", views.segments_csv, name="segments_csv"),
]
