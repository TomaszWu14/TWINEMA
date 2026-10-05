"""Layout hali dla edytora planu (czysty Python — bez Django, testowalny bez bazy).

Format edytora (JSON, metry, konwencja repo: narożnik (x, y) + kąt w stopniach, y „w głąb” hali):
  {"floor": {"width", "depth"},
   "racks":    [{"id"?, "zone", "rack_id", "x", "y", "angle", "n_bays", "n_levels",
                 "bay_width_cm", "depth_cm", "level_height_cm"}],
   "features": [{"id"?, "kind", "label", "x", "y", "width", "depth", "angle"}],
   "version": "<updated_at modelu, ISO>"}
`id` = klucz wiersza w bazie (brak = nowy element). Problemy wskazują elementy po INDEKSIE na listach.

  • `clean_layout` — walidacja wejścia z przeglądarki (typy, zakresy) → LayoutError z opisem.
  • `rack_row` / `feature_row` — wiersz bazy → dict edytora (konwerter w drugą stronę robi widok zapisu).
  • `check_layout` — kolizje na obróconych prostokątach (SAT), regał w polu odkładczym/doku…,
    poza halą, duplikat adresu regału.
  • `analyze` — KPI jak w wariantach (`design_kpi.compute_kpi`) + problemy, w tym alejki
    z `design_catalog.check_aisles` (jedna reguła w repo).
"""
import math

from .blender_route import bbox, near_pairs, overlap_depth, rack_corners
from .design_kpi import compute_kpi, rack_to_element

# Cechy hali, w których nie wolno stawiać regałów: ruch i obsługa. Obszary (strefa blokowa, zwroty,
# „inny”) to tylko oznaczenia na planie — regały mogą w nich stać.
BLOCKING_KINDS = {"dock", "gate", "staging", "station", "leader", "corridor"}
OVERLAP_TOL_M = 0.02          # styk krawędzią / plecami do siebie to nie kolizja
OUTSIDE_TOL_M = 0.05

MAX_RACKS, MAX_FEATURES = 5000, 1000
RACK_LIMITS = {"n_bays": (1, 500), "n_levels": (1, 40), "bay_width_cm": (20, 2000),
               "depth_cm": (20, 1000), "level_height_cm": (20, 1000)}


class LayoutError(ValueError):
    """Nieprawidłowe dane z edytora — komunikat do pokazania użytkownikowi."""


def _num(v, what, lo=-1e5, hi=1e5):
    if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) or not lo <= v <= hi:
        raise LayoutError(f"{what}: oczekiwana liczba z zakresu {lo:g}–{hi:g}.")
    return float(v)


def _int(v, what, lo, hi):
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    if isinstance(v, bool) or not isinstance(v, int) or not lo <= v <= hi:
        raise LayoutError(f"{what}: oczekiwana liczba całkowita {lo}–{hi}.")
    return v


def _id(v, what):
    return None if v is None else _int(v, what, 1, 2**63 - 1)


def _text(v, what, max_len, required=True):
    s = (v if isinstance(v, str) else "").strip()
    if required and not s:
        raise LayoutError(f"{what}: pole wymagane.")
    if len(s) > max_len:
        raise LayoutError(f"{what}: maks. {max_len} znaków.")
    return s


def clean_layout(data, feature_kinds):
    """Dane z przeglądarki → znormalizowany layout. `feature_kinds` = dozwolone rodzaje cech hali."""
    if not isinstance(data, dict):
        raise LayoutError("Oczekiwany obiekt JSON z polami floor, racks, features.")
    floor, racks, feats = data.get("floor"), data.get("racks"), data.get("features")
    if not isinstance(floor, dict) or not isinstance(racks, list) or not isinstance(feats, list):
        raise LayoutError("Brak pól floor / racks / features.")
    if len(racks) > MAX_RACKS or len(feats) > MAX_FEATURES:
        raise LayoutError(f"Za dużo elementów (maks. {MAX_RACKS} regałów, {MAX_FEATURES} elementów hali).")
    out = {"floor": {"width": _num(floor.get("width"), "Szerokość hali", 1, 5000),
                     "depth": _num(floor.get("depth"), "Głębokość hali", 1, 5000)},
           "racks": [], "features": [], "version": data.get("version") if isinstance(data.get("version"), str) else ""}
    for i, r in enumerate(racks, 1):
        if not isinstance(r, dict):
            raise LayoutError(f"Regał {i}: oczekiwany obiekt.")
        row = {"id": _id(r.get("id"), f"Regał {i} id"),
               "zone": _text(r.get("zone"), f"Regał {i} strefa", 20),
               "rack_id": _text(r.get("rack_id"), f"Regał {i} numer", 20),
               "x": _num(r.get("x"), f"Regał {i} X"), "y": _num(r.get("y"), f"Regał {i} Y"),
               "angle": _num(r.get("angle", 0), f"Regał {i} kąt", -3600, 3600) % 360}
        for k, (lo, hi) in RACK_LIMITS.items():
            row[k] = _int(r.get(k), f"Regał {i} {k}", lo, hi)
        out["racks"].append(row)
    for i, f in enumerate(feats, 1):
        if not isinstance(f, dict):
            raise LayoutError(f"Element hali {i}: oczekiwany obiekt.")
        kind = f.get("kind")
        if kind not in feature_kinds:
            raise LayoutError(f"Element hali {i}: nieznany rodzaj {kind!r}.")
        out["features"].append({
            "id": _id(f.get("id"), f"Element hali {i} id"), "kind": kind,
            "label": _text(f.get("label"), f"Element hali {i} etykieta", 100, required=False),
            "x": _num(f.get("x"), f"Element hali {i} X"), "y": _num(f.get("y"), f"Element hali {i} Y"),
            "width": _num(f.get("width"), f"Element hali {i} szerokość", 0.1, 5000),
            "depth": _num(f.get("depth"), f"Element hali {i} głębokość", 0.1, 5000),
            "angle": _num(f.get("angle", 0), f"Element hali {i} kąt", -3600, 3600) % 360})
    return out


# ── Konwersja: wiersz bazy → dict edytora (obiekty z atrybutami jak modele Django) ─────────────
def rack_row(r):
    return {"id": r.pk, "zone": r.zone, "rack_id": r.rack_id, "x": r.x_m or 0.0, "y": r.y_m or 0.0,
            "angle": r.angle_deg or 0.0, "n_bays": r.n_bays, "n_levels": r.n_levels,
            "bay_width_cm": r.bay_width_cm, "depth_cm": r.depth_cm, "level_height_cm": r.level_height_cm}


def feature_row(f):
    return {"id": f.pk, "kind": f.kind, "label": f.label, "x": f.x_m, "y": f.y_m,
            "width": f.width_m, "depth": f.depth_m, "angle": f.angle_deg or 0.0}


def rack_geom(r):
    """Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i KPI."""
    return {"zone": r["zone"], "rack_id": r["rack_id"], "x": r["x"], "y": r["y"], "angle": r["angle"],
            "width": r["n_bays"] * r["bay_width_cm"] / 100, "depth": r["depth_cm"] / 100,
            "level_h": r["level_height_cm"] / 100, "n_bays": r["n_bays"], "n_levels": r["n_levels"]}


def _issue(code, severity, message, racks=(), features=()):
    return {"code": code, "severity": severity, "message": message,
            "racks": sorted(set(racks)), "features": sorted(set(features))}


def _name(r):
    return f"{r['zone']}-{r['rack_id']}"


def check_layout(layout):
    """Lista problemów: error blokuje zapis, warning tylko ostrzega."""
    racks, feats, floor = layout["racks"], layout["features"], layout["floor"]
    issues = []

    seen = {}
    for i, r in enumerate(racks):
        seen.setdefault((r["zone"], r["rack_id"]), []).append(i)
    for (zone, rid), idx in seen.items():
        if len(idx) > 1:
            issues.append(_issue("duplicate", "error", f"Adres regału {zone}-{rid} występuje {len(idx)} razy.", idx))

    rc = [rack_corners(rack_geom(r)) for r in racks]
    fc = [rack_corners(f) for f in feats]
    W, D = floor["width"], floor["depth"]
    for kind, corners, items in (("rack", rc, racks), ("feature", fc, feats)):
        for i, c in enumerate(corners):
            x0, y0, x1, y1 = bbox(c)
            if x0 < -OUTSIDE_TOL_M or y0 < -OUTSIDE_TOL_M or x1 > W + OUTSIDE_TOL_M or y1 > D + OUTSIDE_TOL_M:
                if kind == "rack":
                    issues.append(_issue("outside", "error", f"Regał {_name(items[i])} wychodzi poza halę.", [i]))
                else:                                       # rampa doku bywa przed ścianą — tylko ostrzeżenie
                    issues.append(_issue("outside", "warning", f"Element „{items[i]['label'] or items[i]['kind']}” "
                                                               "wychodzi poza halę.", (), [i]))

    # Kolizje: regały + blokujące cechy hali w jednym indeksie siatki.
    blocking = [j for j, f in enumerate(feats) if f["kind"] in BLOCKING_KINDS]
    shapes = rc + [fc[j] for j in blocking]
    n = len(rc)
    for a, b in near_pairs([bbox(c) for c in shapes]):
        if a >= n:                                         # cecha–cecha: doki przy bramach są normalne
            continue
        depth = overlap_depth(shapes[a], shapes[b])
        if depth <= OVERLAP_TOL_M:
            continue
        if b < n:
            issues.append(_issue("collision", "error",
                                 f"Regały {_name(racks[a])} i {_name(racks[b])} nachodzą na siebie ({depth:.2f} m).",
                                 [a, b]))
        else:
            f = feats[blocking[b - n]]
            issues.append(_issue("blocked", "error",
                                 f"Regał {_name(racks[a])} stoi w obszarze „{f['label'] or f['kind']}” — "
                                 "tu musi być wolna posadzka.", [a], [blocking[b - n]]))

    return issues


def analyze(layout):
    """(kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a alejki z jego
    `aisle_issues` (`design_catalog.check_aisles`), więc jedna reguła i jedno liczenie."""
    issues = check_layout(layout)
    if not layout["racks"]:
        return {}, issues
    kpi = compute_kpi([rack_to_element(rack_geom(r)) for r in layout["racks"]], layout["features"],
                      layout["floor"]["width"], layout["floor"]["depth"])
    for it in kpi.pop("aisle_issues"):
        if it["type"] == "za wąska alejka":                 # kolizje liczy SAT w check_layout
            issues.append(_issue("aisle", "warning",
                                 f"Alejka {it['a']} / {it['b']}: {it['gap_m']:.2f} m, sprzęt wymaga {it['need_m']} m.",
                                 [it["ia"], it["ib"]]))
    return kpi, issues
