from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Moduły platformy w kolejności przepływu pracy. `ready=False` = zapowiedź na hubie.
MODULES = [
    {"key": "dane", "name": "Dane", "desc": "Materiały, nośniki, regały, historia ruchów — importy z plików.",
     "phase": "F2", "ready": False},
    {"key": "model", "name": "Model hali", "desc": "Hala od zera albo z danych: regały, strefy, pola odkładcze.",
     "phase": "F1", "ready": False},
    {"key": "symulacja", "name": "Symulacja", "desc": "Dzień projektowy, flota, kalibracja, porównanie wariantów.",
     "phase": "F1", "ready": False},
    {"key": "ml", "name": "Prognozy i ML", "desc": "Wzrost wolumenów, segmentacja SKU, czas cyklu.",
     "phase": "F4", "ready": False},
    {"key": "render", "name": "Render 3D", "desc": "Blender: ujęcia i animacje przepływów.",
     "phase": "F3", "ready": False},
    {"key": "studio", "name": "Studio prezentacji", "desc": "Scenariusz, lektor, montaż — film i deck.",
     "phase": "F5", "ready": False},
]


@login_required
def home(request):
    return render(request, "core/home.html", {"modules": MODULES})
