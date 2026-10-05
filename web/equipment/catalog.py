"""Katalog sprzętu (K1) — czysty Python, bez Django.

  • `KINDS` — typy sprzętu; `RACK_CATEGORY` — który typ obsługuje jaką kategorię regału z layoutu
    (`reach` / `vna`; regał półkowy = kompletacja ręczna, bez sprzętu z katalogu).
  • Klasy systemowe (anonimowe, wartości przybliżone/syntetyczne) zakłada migracja `0002_klasy_systemowe`;
    konkretne modele użytkownik dodaje w aplikacji z kart katalogowych (nazwy żyją tylko w jego bazie).
  • `capacity_at` — udźwig na wysokości z krzywej redukcji (interpolacja liniowa).
  • `move_minutes` — czas jednego ruchu palety: jazda tam i z powrotem + podnoszenie/opuszczanie + pobranie/odłożenie.
"""
KINDS = [
    ("pallet_truck", "Wózek paletowy elektryczny"),
    ("counterbalance", "Wózek czołowy"),
    ("reach", "Reach truck (wysokiego składowania)"),
    ("vna", "VNA / wózek systemowy (kombi)"),
    ("agv", "AGV paletowy"),
    ("amr", "AMR"),
    ("conveyor", "Przenośnik"),
    ("sorter", "Sorter"),
]
RACK_CATEGORY = {"reach": "reach", "counterbalance": "reach", "vna": "vna"}


def capacity_at(nominal_kg, curve, height_m):
    """Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem liniowo, powyżej
    ostatniego punktu — ostatnia wartość (sprawdzenie maks. wysokości osobno)."""
    pts = sorted((float(h), float(kg)) for h, kg in (curve or []))
    if not pts or height_m <= pts[0][0]:
        return float(nominal_kg)
    for (h0, k0), (h1, k1) in zip(pts, pts[1:], strict=False):
        if height_m <= h1:
            return k0 + (k1 - k0) * (height_m - h0) / (h1 - h0)
    return pts[-1][1]


def move_minutes(eq, dist_m, lift_m):
    """Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę), podniesienie i opuszczenie
    wideł na `lift_m`, pobranie i odłożenie. ponytail: bez przyspieszeń i zakrętów — rząd wielkości."""
    v_full = max(eq.get("speed_loaded_kmh") or 0, 0.1) / 3.6
    v_empty = max(eq.get("speed_empty_kmh") or 0, 0.1) / 3.6
    lift = lift_m / max(eq.get("lift_speed_ms") or 0.3, 0.01) + lift_m / max(eq.get("lower_speed_ms") or 0.3, 0.01)
    s = dist_m / v_full + dist_m / v_empty + lift + (eq.get("pick_s") or 20) + (eq.get("drop_s") or 20)
    return s / 60
