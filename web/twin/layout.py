"""Layout hali dla edytora planu (czysty Python — bez Django, testowalny bez bazy).

Format edytora (JSON, metry, konwencja repo: narożnik (x, y) + kąt w stopniach, y „w głąb” hali):
  {"floor": {"width", "depth", "clear_height"?},
   "racks":    [{"id"?, "zone", "rack_id", "x", "y", "angle", "n_bays", "n_levels",
                 "bay_width_cm", "depth_cm", "level_height_cm", "equipment"?, "equipment_id"?}],
   "features": [{"id"?, "kind", "label", "x", "y", "width", "depth", "angle"}],
   "columns":  {"pitch_x", "pitch_y", "offset_x", "offset_y", "size", "removed": [[i, j]], "extra": [[x, y]]},
   "underlay": {"scale", "x", "y", "opacity"} | null,
   "version": "<updated_at modelu, ISO>"}
`id` = klucz wiersza w bazie (brak = nowy element). Problemy wskazują elementy po INDEKSIE na listach.

  • `clean_layout` — walidacja wejścia z przeglądarki (typy, zakresy) → LayoutError z opisem.
  • `rack_row` / `feature_row` — wiersz bazy → dict edytora (konwerter w drugą stronę robi widok zapisu).
  • `column_list` — słupy z siatki (minus usunięte, plus dodane ręcznie) jako kwadraty na planie.
  • `check_layout` — kolizje na obróconych prostokątach (SAT): regał–regał, regał w polu odkładczym/doku/
    drodze pożarowej…, regał lub dok/brama na słupie, poza halą, duplikat adresu, wysokość w świetle,
    regał na drodze ruchu (ostrzeżenie).
  • `analyze` — KPI jak w wariantach (`design_kpi.compute_kpi`) + problemy, w tym alejki
    z `design_catalog.check_aisles` (jedna reguła w repo; wymagana alejka zależy od sprzętu regału).
    Z katalogiem sprzętu (K1, `catalog` = {id: parametry}): alejka Ast z katalogu, najwyższa belka ponad
    maks. wysokość podnoszenia (błąd), nośność miejsca ponad udźwig sprzętu na tej wysokości (ostrzeżenie).
"""
import math

from equipment.catalog import RACK_CATEGORY, capacity_at

from .blender_route import bbox, near_pairs, overlap_depth, rack_corners
from .design_kpi import compute_kpi, rack_to_element

# Cechy hali, w których nie wolno stawiać regałów: ruch, obsługa, bezpieczeństwo. Obszary (strefa blokowa,
# zwroty, strefy specjalne, „inny”) to tylko oznaczenia na planie — regały mogą w nich stać.
BLOCKING_KINDS = {"dock", "gate", "staging", "station", "leader", "corridor", "fire_route", "charging"}
TRAFFIC_KINDS = {"walkway", "truckway"}      # drogi ruchu: regał na nich = ostrzeżenie (oznaczenie, nie mur)
COLUMN_BLOCKS = {"dock", "gate"}             # słup w doku/bramie = błąd (auto musi podjechać)
SPECIAL_ZONE_KINDS = {"zone_temp", "zone_adr", "zone_oversize", "zone_value"}   # reguły rozmieszczenia → S3
EQUIPMENT = ("reach", "vna", "shelf")
DOCK_ROLES = ("in_container", "in_pallet", "out", "courier", "shared")
DEFAULT_LOAD_KG = 1000
ROOF_GAP_M = 0.5        # zapas nad najwyższym poziomem regału pod konstrukcją dachu / tryskaczami
OVERLAP_TOL_M = 0.02    # styk krawędzią / plecami do siebie to nie kolizja
OUTSIDE_TOL_M = 0.05

MAX_RACKS, MAX_FEATURES, MAX_COLUMNS = 5000, 1000, 20_000
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


def clean_columns(c):
    """Siatka słupów z edytora. Brak = hala bez słupów (zwraca {}); rozstaw 0 = bez siatki (same dodane)."""
    if not c:
        return {}
    if not isinstance(c, dict):
        raise LayoutError("Słupy: oczekiwany obiekt.")
    out = {"pitch_x": _num(c.get("pitch_x", 0), "Słupy: rozstaw X", 0, 500),
           "pitch_y": _num(c.get("pitch_y", 0), "Słupy: rozstaw Y", 0, 500),
           "offset_x": _num(c.get("offset_x", 0), "Słupy: przesunięcie X", 0, 500),
           "offset_y": _num(c.get("offset_y", 0), "Słupy: przesunięcie Y", 0, 500),
           "size": _num(c.get("size", 0.6), "Słupy: wymiar", 0.1, 5)}
    if any(0 < out[k] < 2 for k in ("pitch_x", "pitch_y")):
        raise LayoutError("Słupy: rozstaw musi wynosić 0 (brak siatki) albo co najmniej 2 m.")
    removed, extra = c.get("removed") or [], c.get("extra") or []
    if not isinstance(removed, list) or not isinstance(extra, list) or len(removed) + len(extra) > MAX_COLUMNS:
        raise LayoutError("Słupy: niepoprawne listy usuniętych / dodanych.")
    if any(not isinstance(p, list) or len(p) != 2 for p in removed + extra):
        raise LayoutError("Słupy: każdy wpis to para liczb.")
    out["removed"] = sorted({(_int(i, "Słup: indeks", 0, 10_000), _int(j, "Słup: indeks", 0, 10_000))
                             for i, j in removed})
    out["removed"] = [list(p) for p in out["removed"]]
    out["extra"] = [[_num(x, "Słup: X"), _num(y, "Słup: Y")] for x, y in extra]
    return out


def clean_underlay(u):
    """Położenie i skala podkładu (sam plik przychodzi osobnym uploadem)."""
    if not u:
        return None
    if not isinstance(u, dict):
        raise LayoutError("Podkład: oczekiwany obiekt.")
    return {"scale": _num(u.get("scale"), "Podkład: skala [m/px]", 1e-5, 100),
            "x": _num(u.get("x", 0), "Podkład: X"), "y": _num(u.get("y", 0), "Podkład: Y"),
            "opacity": _num(u.get("opacity", 0.5), "Podkład: przezroczystość", 0, 1)}


def clean_layout(data, feature_kinds):
    """Dane z przeglądarki → znormalizowany layout. `feature_kinds` = dozwolone rodzaje cech hali."""
    if not isinstance(data, dict):
        raise LayoutError("Oczekiwany obiekt JSON z polami floor, racks, features.")
    floor, racks, feats = data.get("floor"), data.get("racks"), data.get("features")
    if not isinstance(floor, dict) or not isinstance(racks, list) or not isinstance(feats, list):
        raise LayoutError("Brak pól floor / racks / features.")
    if len(racks) > MAX_RACKS or len(feats) > MAX_FEATURES:
        raise LayoutError(f"Za dużo elementów (maks. {MAX_RACKS} regałów, {MAX_FEATURES} elementów hali).")
    clear_h = floor.get("clear_height")
    out = {"floor": {"width": _num(floor.get("width"), "Szerokość hali", 1, 5000),
                     "depth": _num(floor.get("depth"), "Głębokość hali", 1, 5000),
                     "clear_height": None if clear_h in (None, "") else _num(clear_h, "Wysokość w świetle", 2, 100)},
           "racks": [], "features": [], "columns": clean_columns(data.get("columns")),
           "underlay": clean_underlay(data.get("underlay")),
           "version": data.get("version") if isinstance(data.get("version"), str) else ""}
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
        row["equipment"] = r.get("equipment") or "reach"
        eid = r.get("equipment_id")
        row["equipment_id"] = None if eid in (None, "") else _int(eid, f"Regał {i} sprzęt z katalogu", 1, 2**31)
        row["equipment_given"] = "equipment_id" in r          # stary klient bez pola = sprzęt w bazie bez zmian
        if row["equipment"] not in EQUIPMENT:
            raise LayoutError(f"Regał {i}: nieznany sprzęt {row['equipment']!r}.")
        # brak klucza = zostaw wartość z bazy (stary klient); None przy zapisie nie nadpisuje
        row["load_kg"] = (None if r.get("load_kg") in (None, "")
                          else _int(r.get("load_kg"), f"Regał {i} nośność [kg]", 50, 10000))
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
            "angle": _num(f.get("angle", 0), f"Element hali {i} kąt", -3600, 3600) % 360,
            "dock_role": _dock_role(f, i)})
    return out


def _dock_role(f, i):
    if "dock_role" not in f or f["dock_role"] is None:
        return None
    role = f["dock_role"]
    if role not in ("", *DOCK_ROLES):
        raise LayoutError(f"Element hali {i}: nieznana rola doku {role!r}.")
    return role


def guess_dock_role(label):
    """Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery, „pacz…/kurier” → paczki,
    „wspóln” → wspólny, „przyj/paletowy/ IN ” → palety IN, reszta → wydania."""
    s = f" {(label or '').lower()} "
    if "wspóln" in s:
        return "shared"
    if "pacz" in s or "kurier" in s:
        return "courier"
    if "kontener" in s:
        return "in_container"
    if "przyj" in s or "paletowy" in s or " in " in s:
        return "in_pallet"
    return "out"


def column_list(columns, floor):
    """[{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla dodanych ręcznie."""
    if not columns:
        return []
    size, px, py = columns.get("size", 0.6), columns.get("pitch_x", 0), columns.get("pitch_y", 0)
    ox, oy = columns.get("offset_x", 0), columns.get("offset_y", 0)
    out = []
    if px and py:
        nx, ny = int((floor["width"] - ox) // px) + 1, int((floor["depth"] - oy) // py) + 1
        if nx * ny > MAX_COLUMNS:
            raise LayoutError(f"Za gęsta siatka słupów ({nx * ny}); maks. {MAX_COLUMNS}.")
        removed = {tuple(p) for p in columns.get("removed", [])}
        out = [{"x": round(ox + i * px, 3), "y": round(oy + j * py, 3), "size": size, "ref": [i, j]}
               for i in range(nx) for j in range(ny) if (i, j) not in removed]
    return out + [{"x": x, "y": y, "size": size, "ref": ["e", k]} for k, (x, y) in enumerate(columns.get("extra", []))]


def _column_corners(c):
    h = c["size"] / 2
    return rack_corners({"x": c["x"] - h, "y": c["y"] - h, "angle": 0.0, "width": c["size"], "depth": c["size"]})


# ── Konwersja: wiersz bazy → dict edytora (obiekty z atrybutami jak modele Django) ─────────────
def rack_row(r):
    return {"id": r.pk, "zone": r.zone, "rack_id": r.rack_id, "x": r.x_m or 0.0, "y": r.y_m or 0.0,
            "angle": r.angle_deg or 0.0, "n_bays": r.n_bays, "n_levels": r.n_levels,
            "bay_width_cm": r.bay_width_cm, "depth_cm": r.depth_cm, "level_height_cm": r.level_height_cm,
            "equipment": getattr(r, "equipment", None) or "reach",
            "equipment_id": getattr(r, "equipment_model_id", None),
            "load_kg": getattr(r, "load_kg", None) or DEFAULT_LOAD_KG}


def feature_row(f):
    return {"id": f.pk, "kind": f.kind, "label": f.label, "x": f.x_m, "y": f.y_m,
            "width": f.width_m, "depth": f.depth_m, "angle": f.angle_deg or 0.0,
            "dock_role": getattr(f, "dock_role", "") or ""}


def rack_geom(r):
    """Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i KPI."""
    return {"zone": r["zone"], "rack_id": r["rack_id"], "x": r["x"], "y": r["y"], "angle": r["angle"],
            "width": r["n_bays"] * r["bay_width_cm"] / 100, "depth": r["depth_cm"] / 100,
            "level_h": r["level_height_cm"] / 100, "n_bays": r["n_bays"], "n_levels": r["n_levels"],
            "equipment": r.get("equipment") or "reach", "aisle_m": (r.get("_eq") or {}).get("aisle_m")}


def _issue(code, severity, message, racks=(), features=()):
    return {"code": code, "severity": severity, "message": message,
            "racks": sorted(set(racks)), "features": sorted(set(features))}


def _name(r):
    return f"{r['zone']}-{r['rack_id']}"


def _fname(f):
    return f["label"] or f["kind"]


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
                    issues.append(_issue("outside", "warning", f"Element „{_fname(items[i])}” wychodzi poza halę.",
                                         (), [i]))

    # Jeden indeks siatki: regały | cechy blokujące i drogi ruchu | słupy. Pary sprawdzamy, gdy biorą
    # w nich udział regały albo słup z dokiem/bramą (cecha–cecha i słup–słup są normalne).
    shown = [j for j, f in enumerate(feats) if f["kind"] in BLOCKING_KINDS | TRAFFIC_KINDS]
    cols = column_list(layout.get("columns"), floor)
    shapes = rc + [fc[j] for j in shown] + [_column_corners(c) for c in cols]
    n, m = len(rc), len(rc) + len(shown)
    for a, b in near_pairs([bbox(c) for c in shapes]):                  # a < b
        feature_column = n <= a < m <= b and feats[shown[a - n]]["kind"] in COLUMN_BLOCKS
        if a >= n and not feature_column:
            continue
        depth = overlap_depth(shapes[a], shapes[b])
        if depth <= OVERLAP_TOL_M:
            continue
        if b >= m:
            c = cols[b - m]
            where = f"słupem w punkcie ({c['x']:g}; {c['y']:g}) m"
            if a < n:
                issues.append(_issue("column", "error", f"Regał {_name(racks[a])} koliduje ze {where}.", [a]))
            else:
                issues.append(_issue("column", "error", f"„{_fname(feats[shown[a - n]])}” koliduje ze {where} — "
                                                        "dok i brama muszą być wolne.", (), [shown[a - n]]))
        elif b < n:
            issues.append(_issue("collision", "error",
                                 f"Regały {_name(racks[a])} i {_name(racks[b])} nachodzą na siebie ({depth:.2f} m).",
                                 [a, b]))
        else:
            j = shown[b - n]
            if feats[j]["kind"] in TRAFFIC_KINDS:
                issues.append(_issue("traffic", "warning", f"Regał {_name(racks[a])} stoi na drodze ruchu "
                                                           f"„{_fname(feats[j])}”.", [a], [j]))
            else:
                issues.append(_issue("blocked", "error", f"Regał {_name(racks[a])} stoi w obszarze "
                                                         f"„{_fname(feats[j])}” — tu musi być wolna posadzka.",
                                     [a], [j]))

    H = floor.get("clear_height")
    if H:
        usable = H - ROOF_GAP_M
        for i, r in enumerate(racks):
            top = r["n_levels"] * r["level_height_cm"] / 100
            if top > usable + 1e-6:
                issues.append(_issue("height", "error", f"Regał {_name(r)} ma {top:.2f} m — ponad wysokość użytkową "
                                                        f"{usable:.2f} m (hala {H:g} m − {ROOF_GAP_M:g} m zapasu).",
                                     [i]))
    return issues


def height_kpi(layout):
    """Wysokość w świetle → maks. poziomów per strefa (przy wysokości poziomu jej regałów)."""
    H = layout["floor"].get("clear_height")
    if not H:
        return None
    zones = {}
    for r in layout["racks"]:
        z = zones.setdefault(r["zone"], {"levels": 0, "max_levels": None})
        z["levels"] = max(z["levels"], r["n_levels"])
        fit = int((H - ROOF_GAP_M) // (r["level_height_cm"] / 100))
        z["max_levels"] = fit if z["max_levels"] is None else min(z["max_levels"], fit)
    return {"clear_m": H, "usable_m": round(H - ROOF_GAP_M, 2), "zones": zones}


def attach_equipment(layout, catalog):
    """Regał z `equipment_id` z katalogu → `_eq` (parametry) i kategoria z typu sprzętu (reach/vna);
    nieznane id (usunięty model) → bez sprzętu."""
    for r in layout["racks"]:
        eq = (catalog or {}).get(r.get("equipment_id"))
        r["_eq"] = eq
        if eq is None:
            r["equipment_id"] = None
        elif RACK_CATEGORY.get(eq["kind"]):
            r["equipment"] = RACK_CATEGORY[eq["kind"]]


def check_equipment(racks):
    """Wysokość podnoszenia (błąd) i udźwig na wysokości vs nośność miejsca (ostrzeżenie, najgorszy poziom)."""
    issues = []
    for i, r in enumerate(racks):
        eq = r.get("_eq")
        if not eq:
            continue
        lh = r["level_height_cm"] / 100
        top = (r["n_levels"] - 1) * lh
        if eq.get("max_lift_m") is not None and top > eq["max_lift_m"] + 1e-6:
            issues.append(_issue("lift", "error", f"Regał {_name(r)}: najwyższa belka {top:.2f} m, a „{eq['name']}” "
                                                  f"podnosi do {eq['max_lift_m']:g} m.", [i]))
            continue
        load = r.get("load_kg") or DEFAULT_LOAD_KG
        cap = capacity_at(eq["capacity_kg"], eq.get("lift_curve"), top)
        if r["n_levels"] > 1 and load > cap + 1e-6:
            low = next(k for k in range(r["n_levels"]) if load > capacity_at(eq["capacity_kg"], eq.get("lift_curve"),
                                                                               k * lh) + 1e-6)
            issues.append(_issue("lift_load", "warning", f"Regał {_name(r)}: nośność miejsca {load} kg, a „{eq['name']}” "
                                                         f"na {top:.2f} m podniesie {cap:.0f} kg — od poziomu {low + 1} "
                                                         "palety cięższe niż udźwig.", [i]))
    return issues


def analyze(layout, catalog=None):
    """(kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a alejki z jego
    `aisle_issues` (`design_catalog.check_aisles`), więc jedna reguła i jedno liczenie."""
    attach_equipment(layout, catalog)
    issues = check_layout(layout) + check_equipment(layout["racks"])
    if not layout["racks"]:
        return {}, issues
    kpi = compute_kpi([rack_to_element(rack_geom(r)) for r in layout["racks"]], layout["features"],
                      layout["floor"]["width"], layout["floor"]["depth"])
    for it in kpi.pop("aisle_issues"):
        if it["type"] == "za wąska alejka":                 # kolizje liczy SAT w check_layout
            issues.append(_issue("aisle", "warning",
                                 f"Alejka {it['a']} / {it['b']}: {it['gap_m']:.2f} m, sprzęt wymaga {it['need_m']} m.",
                                 [it["ia"], it["ib"]]))
    kpi["height"] = height_kpi(layout)
    kpi["columns"] = len(column_list(layout.get("columns"), layout["floor"]))
    return kpi, issues
