from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse

# Moduły platformy w kolejności przepływu pracy — jedno źródło dla nawigacji w nagłówku i kafli strony
# głównej (R4: te same nazwy). `apps` / `match` = kiedy pozycja jest aktywna (patrz `active_module`).
MODULES = [
    {"key": "dane", "name": "Dane", "desc": "Materiały, master lokalizacji, stany — importy z plików z raportem.",
     "url": "masterdata:home", "apps": {"masterdata"}},
    {"key": "model", "name": "Modele hal", "desc": "Hala od zera albo z danych: regały, strefy, pola odkładcze, działka.",
     "url": "twin:warehouse_model_list", "apps": {"twin"}},
    {"key": "scenariusze", "name": "Scenariusze", "desc": "Wolumeny dnia typowego i szczytowego, symulacja dnia, koszty.",
     "url": "scenario:list", "apps": {"scenario"}},
    {"key": "projektowanie", "name": "Projektowanie", "desc": "Dzień projektowy z danych, flota, kalibracja, porównanie wariantów.",
     "url": "twin:design_hub", "match": ("design_",)},
    {"key": "zadania", "name": "Zadania EWM", "desc": "Import zadań magazynowych: profil, prognoza i symulacja dnia.",
     "url": "twin:ewm_tasks_list", "match": ("ewm_tasks",)},
    {"key": "sprzet", "name": "Sprzęt", "desc": "Wózki, AGV/AMR z osprzętem: prędkości, podnoszenie, udźwig, alejka, koszty.",
     "url": "equipment:list", "apps": {"equipment"}},
    {"key": "prezentacje", "name": "Prezentacje", "desc": "Pokaz 3D dla zarządu: ujęcia hali, wyniki dnia, szczyt, wnioski.",
     "url": "scenario:showcase_list", "match": ("showcase",)},
    {"key": "ml", "name": "Prognozy i ML", "desc": "Holt-Winters kontra baseline, segmentacja SKU pod rozmieszczenie.",
     "url": "ml:home", "apps": {"ml"}},
    {"key": "render", "name": "Render", "desc": "Blender: ujęcia i animacje przepływów (worker na PC).",
     "url": "render:jobs", "apps": {"render"}},
    {"key": "studio", "name": "Studio", "desc": "Scenariusz, lektor, montaż — film i deck.",
     "url": "studio:list", "apps": {"studio"}},
]


def active_module(rm):
    """Klucz modułu dla bieżącego widoku: najpierw dopasowanie po nazwie URL (moduły w obrębie jednej appki:
    prezentacje w `scenario`, projektowanie i zadania EWM w `twin`), potem po appce. Brak → None."""
    if rm is None:
        return None
    for m in MODULES:
        if any(x in (rm.url_name or "") for x in m.get("match", ())):
            return m["key"]
    return next((m["key"] for m in MODULES if rm.app_name in m.get("apps", ())), None)


@login_required
def home(request):
    modules = [{**m, "url": reverse(m["url"])} for m in MODULES]
    return render(request, "core/home.html", {"modules": modules})
