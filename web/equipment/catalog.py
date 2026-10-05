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
    ("stacker", "Wózek podnośnikowy (unoszący z masztem)"),
    ("order_picker", "Wózek do kompletacji"),
    ("tractor", "Ciągnik"),
    ("conveyor", "Przenośnik"),
    ("sorter", "Sorter"),
]
# Typy przypisywalne do regałów w edytorze. Ciągnik, AGV/AMR, przenośnik i sorter nie podnoszą palety do gniazda.
RACK_CATEGORY = {"reach": "reach", "counterbalance": "reach", "stacker": "reach", "order_picker": "reach",
                 "vna": "vna"}

# Osprzęt: kod → (etykieta, redukcja udźwigu [%], dodatkowy czas na pobranie i na odłożenie [s]).
# Wartości przybliżone (typowe rzędy wielkości), do nadpisania własnym modelem z karty katalogowej.
ATTACHMENTS = {
    "forks": ("Widły standardowe", 0, 0),
    "sideshift": ("Przesuw boczny", 5, -3),
    "positioner": ("Pozycjoner wideł", 8, 0),
    "rotator": ("Obrotnica", 15, 8),
    "carton_clamp": ("Zaciski do kartonów", 20, 8),
    "drum_clamp": ("Zaciski do beczek", 20, 10),
    "telescopic": ("Widły teleskopowe / podwójnej głębokości", 15, 12),
    "double_pallet": ("Widły do dwóch palet (podwójny załadunek)", 0, 5),
    "platform": ("Platforma / kosz dla operatora", 0, 0),
}


def apply_attachments(params, codes):
    """Parametry sprzętu po osprzęcie: udźwig (i krzywa) pomniejszony o sumę redukcji, czasy obsługi palety
    wydłużone. Nieznane kody pomijane. Zwraca nowy dict."""
    known = [ATTACHMENTS[c] for c in codes or [] if c in ATTACHMENTS]
    if not known:
        return dict(params)
    k = max(0.0, 1 - sum(a[1] for a in known) / 100)
    extra = sum(a[2] for a in known)
    out = dict(params)
    out["capacity_kg"] = round((params.get("capacity_kg") or 0) * k)
    out["lift_curve"] = [[h, round(kg * k)] for h, kg in params.get("lift_curve") or []]
    for f in ("pick_s", "drop_s"):
        out[f] = max(1.0, (params.get(f) or 20) + extra)
    return out


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
