from django.urls import path

from . import views

app_name = "equipment"

urlpatterns = [
    path("sprzet/", views.catalog_list, name="list"),
    path("sprzet/nowy/", views.catalog_form, name="create"),
    path("sprzet/stawki/", views.rates, name="rates"),
    path("sprzet/import/", views.import_file, name="import"),
    path("sprzet/import/wzor.xlsx", views.import_template, name="import_template"),
    path("sprzet/<int:pk>/", views.catalog_detail, name="detail"),
    path("sprzet/<int:pk>/edycja/", views.catalog_form, name="edit"),
    path("sprzet/<int:pk>/kopia/", views.catalog_copy, name="copy"),
    path("sprzet/<int:pk>/usun/", views.catalog_delete, name="delete"),
]
