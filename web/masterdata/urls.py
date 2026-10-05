from django.urls import path

from . import views

app_name = "masterdata"

urlpatterns = [
    path("dane/", views.home, name="home"),
    path("dane/import/<str:kind>/", views.upload, name="upload"),
    path("dane/import/<int:pk>/raport/", views.log_detail, name="log_detail"),
    path("dane/wzor/<str:kind>.csv", views.template, name="template"),
    path("dane/materialy/", views.materials, name="materials"),
    path("dane/materialy/<int:pk>/", views.material_edit, name="material_edit"),
    path("dane/nosniki-i-klasy/", views.catalog, name="catalog"),
    path("dane/demo/", views.demo, name="demo"),
]
