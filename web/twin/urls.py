from django.urls import path

from . import views

app_name = "twin"

urlpatterns = [
    path("magazyn/", views.design_hub, name="design_hub"),

    # ── Typy regałów ────────────────────────────────────────────────────────────
    path("magazyn/types/", views.warehouse_rack_type_list, name="warehouse_rack_type_list"),
    path("magazyn/types/new/", views.warehouse_rack_type_form, name="warehouse_rack_type_new"),
    path("magazyn/types/<int:pk>/edit/", views.warehouse_rack_type_form, name="warehouse_rack_type_edit"),
    path("magazyn/types/<int:pk>/delete/", views.warehouse_rack_type_delete, name="warehouse_rack_type_delete"),

    # ── Model hali ──────────────────────────────────────────────────────────────
    path("magazyn/model/", views.warehouse_model_list, name="warehouse_model_list"),
    path("magazyn/model/upload/", views.warehouse_model_upload, name="warehouse_model_upload"),
    path("magazyn/model/generator/", views.warehouse_model_generator, name="warehouse_model_generator"),
    path("magazyn/model/<int:pk>/kopia/", views.warehouse_model_copy, name="warehouse_model_copy"),
    path("magazyn/model/<int:pk>/strefy/", views.warehouse_model_zones, name="warehouse_model_zones"),
    path("magazyn/model/szablony/", views.bay_template_list, name="bay_template_list"),
    path("magazyn/model/szablony/nowy/", views.bay_template_form, name="bay_template_new"),
    path("magazyn/model/szablony/<int:pk>/", views.bay_template_form, name="bay_template_edit"),
    path("magazyn/model/szablony/<int:pk>/usun/", views.bay_template_delete, name="bay_template_delete"),
    path("magazyn/warianty/", views.warehouse_variants, name="warehouse_variants"),
    path("magazyn/warianty/import/", views.warehouse_variant_import, name="warehouse_variant_import"),
    path("magazyn/warianty/z-modelu/", views.warehouse_variant_from_model, name="warehouse_variant_from_model"),
    path("magazyn/warianty/<int:pk>.json", views.warehouse_variant_json, name="warehouse_variant_json"),
    path("magazyn/warianty/<int:pk>/usun/", views.warehouse_variant_delete, name="warehouse_variant_delete"),
    path("magazyn/model/<int:pk>/paste/", views.warehouse_model_paste, name="warehouse_model_paste"),
    path("magazyn/model/<int:pk>/features/", views.warehouse_model_features, name="warehouse_model_features"),
    path("magazyn/model/<int:pk>/coords/", views.warehouse_model_coords, name="warehouse_model_coords"),
    path("magazyn/model/<int:pk>/wykryj-ewm/", views.warehouse_model_detect, name="warehouse_model_detect"),
    path("magazyn/model/<int:pk>/wykryj-ewm/zapisz/", views.warehouse_model_detect_save,
         name="warehouse_model_detect_save"),
    path("magazyn/model/<int:pk>/zgodnosc-ewm/", views.warehouse_model_compliance,
         name="warehouse_model_compliance"),
    path("magazyn/model/<int:pk>/view/", views.warehouse_model_view, name="warehouse_model_view"),
    path("magazyn/model/<int:pk>/edytor/", views.warehouse_layout_editor, name="warehouse_layout_editor"),
    path("magazyn/model/<int:pk>/uklad.json", views.warehouse_layout_json, name="warehouse_layout_json"),
    path("magazyn/model/<int:pk>/uklad/sprawdz/", views.warehouse_layout_check, name="warehouse_layout_check"),
    path("magazyn/model/<int:pk>/uklad/zapisz/", views.warehouse_layout_save, name="warehouse_layout_save"),
    path("magazyn/model/<int:pk>/blender.json", views.warehouse_model_blender_json, name="warehouse_model_blender_json"),
    path("magazyn/model/<int:pk>/przeplywy.json", views.warehouse_model_flow_json, name="warehouse_model_flow_json"),
    path("magazyn/model/<int:pk>/delete/", views.warehouse_model_delete, name="warehouse_model_delete"),

    # ── Zadania magazynowe (import WT) → profil, symulacja, kalibracja, porównanie, prognoza ──
    path("magazyn/zadania-ewm/", views.ewm_tasks_list, name="ewm_tasks_list"),
    path("magazyn/zadania-ewm/podglad/", views.ewm_tasks_preview, name="ewm_tasks_preview"),
    path("magazyn/zadania-ewm/importuj/", views.ewm_tasks_import, name="ewm_tasks_import"),
    path("magazyn/zadania-ewm/<int:pk>/", views.ewm_tasks_detail, name="ewm_tasks_detail"),
    path("magazyn/zadania-ewm/<int:pk>/status/", views.ewm_tasks_status, name="ewm_tasks_status"),
    path("magazyn/zadania-ewm/<int:pk>/usun/", views.ewm_tasks_delete, name="ewm_tasks_delete"),
    path("magazyn/zadania-ewm/<int:pk>/profil/", views.ewm_tasks_profile, name="ewm_tasks_profile"),
    path("magazyn/zadania-ewm/<int:pk>/symulacja/", views.ewm_tasks_simulate, name="ewm_tasks_simulate"),
    path("magazyn/zadania-ewm/<int:pk>/kalibracja/", views.ewm_tasks_calibration, name="ewm_tasks_calibration"),
    path("magazyn/zadania-ewm/<int:pk>/porownanie/", views.ewm_tasks_compare, name="ewm_tasks_compare"),
    path("magazyn/zadania-ewm/<int:pk>/prognoza/", views.ewm_tasks_forecast, name="ewm_tasks_forecast"),
]
