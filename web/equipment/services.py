"""Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co migracja 0006 w twin."""
from .catalog import RACK_CATEGORY
from .models import Equipment


def pick_class(category, top_m):
    """Najmniejsza klasa systemowa danej kategorii regału (reach/vna), która sięga belki `top_m`;
    gdy żadna — najwyższa. Półki i nieznane kategorie → None."""
    kinds = [k for k, c in RACK_CATEGORY.items() if c == category and k != "counterbalance"]
    cands = sorted(Equipment.objects.filter(is_system=True, kind__in=kinds), key=lambda e: e.max_lift_m or 0)
    return next((e for e in cands if (e.max_lift_m or 0) >= top_m), cands[-1] if cands else None)


def assign_classes(racks):
    """Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii i wysokości."""
    cache = {}
    for r in racks:
        top = max(0, r["n_levels"] - 1) * r["level_height_cm"] / 100
        key = (r.get("equipment") or "reach", top)
        if key not in cache:
            cache[key] = pick_class(*key)
        r["equipment_model"] = cache[key]
    return racks
