from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

# Moduły platformy w kolejności przepływu pracy. `url` = nazwa widoku wejścia; brak = zapowiedź.
MODULES = [
    {"key": "dane", "name": "Dane", "desc": "Materiały, master lokalizacji, stany — importy z plików z raportem.",
     "phase": "F2", "url": "masterdata:home"},
    {"key": "model", "name": "Model hali", "desc": "Hala od zera albo z danych: regały, strefy, pola odkładcze.",
     "phase": "F1", "url": "twin:warehouse_model_list"},
    {"key": "symulacja", "name": "Symulacja", "desc": "Dzień projektowy, flota, kalibracja, porównanie wariantów.",
     "phase": "F1", "url": "twin:design_hub"},
    {"key": "ml", "name": "Prognozy i ML", "desc": "Wzrost wolumenów, segmentacja SKU, czas cyklu.",
     "phase": "F4"},
    {"key": "render", "name": "Render 3D", "desc": "Blender: ujęcia i animacje przepływów.",
     "phase": "F3"},
    {"key": "studio", "name": "Studio prezentacji", "desc": "Scenariusz, lektor, montaż — film i deck.",
     "phase": "F5"},
]


@login_required
def home(request):
    modules = [{**m, "url": reverse(m["url"]) if m.get("url") else ""} for m in MODULES]
    return render(request, "core/home.html", {"modules": modules})
