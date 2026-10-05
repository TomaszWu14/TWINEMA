"""Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python, bez Django.

    check_placement(racks, features, stock, growth=1.0, heavy_max_level=2) → {capacity, issues}

racks    — regały w formacie edytora (`twin.layout.rack_row`: zone, x, y, angle, n_bays, n_levels, bay_width_cm,
           depth_cm, equipment, load_kg); półki (`equipment="shelf"`) to kompletacja, nie miejsca paletowe,
features — elementy hali (`twin.layout.feature_row`: kind, x, y, width, depth, angle),
stock    — `masterdata.services.stock_profile()`: palety na stanie per materiał z wagą i flagami.

Stany nie mają przypisania do konkretnych regałów (adresy z WMS ≠ regały projektu), więc reguły liczą
ZAPOTRZEBOWANIE vs POJEMNOŚĆ: „potrzeba 120 miejsc ADR, strefa ADR ma 80”. Wszystko to ostrzeżenia (#5) —
poza przepełnieniem całej hali, które jest błędem planu.
ponytail: regał należy do strefy specjalnej, gdy jego środek leży w obszarze strefy; regał na granicy
dwóch stref liczy się do jednej — dokładny podział miejsc, gdy strefy zaczną ciąć regały w poprzek.
"""
import math

from twin.blender_route import rack_corners
from twin.blender_scene import rack_class
from twin.design_compare import PALLET_W_M          # 0,9 m na paletę w boku — ten sam wzór co `rack_to_element`

FILL_WARN_PCT = 90
ZONE_FLAGS = [("zone_adr", "adr", "ADR (towary niebezpieczne)"),
              ("zone_temp", "temp_controlled", "temperatura kontrolowana"),
              ("zone_oversize", "oversize", "gabaryty / dłużyca"),
              ("zone_value", "high_value", "wysoka wartość")]


def positions(r):
    """Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość / 0,9 m) albo 0 dla półek."""
    if rack_class({"equipment": r.get("equipment"), "level_h": r["level_height_cm"] / 100}) == "shelf":
        return 0
    return r["n_bays"] * max(1, round(r["bay_width_cm"] / 100 / PALLET_W_M)) * r["n_levels"]


def _poly(o, w, d):
    return rack_corners({"x": o["x"], "y": o["y"], "angle": o.get("angle") or 0.0, "width": w, "depth": d})


def _center(r):
    pts = _poly(r, r["n_bays"] * r["bay_width_cm"] / 100, r["depth_cm"] / 100)
    return sum(p[0] for p in pts) / 4, sum(p[1] for p in pts) / 4


def _inside(pt, poly):
    """Punkt w wypukłym wielokącie (rogi w kolejności obwodu)."""
    sign = 0
    for (x1, y1), (x2, y2) in zip(poly, poly[1:] + poly[:1], strict=True):
        c = (x2 - x1) * (pt[1] - y1) - (y2 - y1) * (pt[0] - x1)
        if abs(c) < 1e-9:
            continue
        if sign == 0:
            sign = 1 if c > 0 else -1
        elif (c > 0) != (sign > 0):
            return False
    return True


def _issue(code, severity, message, racks=(), features=()):
    return {"code": code, "severity": severity, "message": message, "racks": list(racks), "features": list(features)}


def check_placement(racks, features, stock, growth=1.0, heavy_max_level=2):
    pos = [positions(r) for r in racks]
    pallet_racks = [i for i, p in enumerate(pos) if p]
    total = sum(pos)

    def need(pred=lambda s: True):
        return math.ceil(round(sum(s["pallets"] for s in stock if pred(s)) * growth, 6))   # 200×1,1 = 220, nie 221

    need_all = need()
    issues = []
    fill = round(need_all / total * 100, 1) if total else None
    if stock and not total:
        issues.append(_issue("capacity_none", "error", f"Layout nie ma miejsc paletowych, a stan wymaga {need_all}."))
    elif fill is not None and fill > 100:
        issues.append(_issue("capacity_over", "error", f"Stan × wzrost to {need_all} palet, a layout ma {total} "
                                                        f"miejsc ({fill:g} %) — brakuje {need_all - total} miejsc."))
    elif fill is not None and fill > FILL_WARN_PCT:
        issues.append(_issue("capacity_tight", "warning", f"Wypełnienie {fill:g} % (> {FILL_WARN_PCT} %) — "
                                                          f"za mało luzu na przyjęcia i rotację."))

    # strefy specjalne: miejsca w regałach, których środek leży w obszarze strefy
    centers = {i: _center(racks[i]) for i in pallet_racks}
    zones = []
    for kind, flag, label in ZONE_FLAGS:
        fidx = [j for j, f in enumerate(features) if f["kind"] == kind]
        polys = [_poly(features[j], features[j]["width"], features[j]["depth"]) for j in fidx]
        in_zone = [i for i in pallet_racks if any(_inside(centers[i], p) for p in polys)]
        cap, req = sum(pos[i] for i in in_zone), need(lambda s, f=flag: s.get(f))
        zones.append({"kind": kind, "label": label, "positions": cap, "need": req, "areas": len(fidx)})
        if req and not fidx:
            issues.append(_issue(f"{kind}_missing", "warning",
                                 f"Na stanie są towary „{label}” ({req} palet), a layout nie ma takiej strefy."))
        elif req > cap:
            issues.append(_issue(f"{kind}_short", "warning",
                                 f"Strefa „{label}”: potrzeba {req} miejsc, w regałach w strefie jest {cap}.",
                                 racks=in_zone, features=fidx))

    # nośność: palety cięższe niż L muszą mieć miejsca o nośności > L (dla każdego progu L w layoucie)
    loads = sorted({racks[i].get("load_kg") or 1000 for i in pallet_racks})
    weighed = [s for s in stock if s.get("kg")]
    for lim in loads:
        heavy = math.ceil(round(sum(s["pallets"] for s in weighed if s["kg"] > lim) * growth, 6))
        cap = sum(pos[i] for i in pallet_racks if (racks[i].get("load_kg") or 1000) > lim)
        if heavy > cap:
            issues.append(_issue("load_over", "warning",
                                 f"{heavy} palet waży ponad {lim:g} kg, a miejsc o większej nośności jest {cap}.",
                                 racks=[i for i in pallet_racks if (racks[i].get("load_kg") or 1000) <= lim]))
            break                                   # niższe progi tylko powtórzyłyby ten sam brak
    # ciężkie (najwyższa klasa wagi) tylko na dolnych poziomach
    heavy_need = need(lambda s: s.get("heavy"))
    low = sum(pos[i] // racks[i]["n_levels"] * min(racks[i]["n_levels"], heavy_max_level) for i in pallet_racks)
    if heavy_need > low:
        issues.append(_issue("heavy_high", "warning",
                             f"Ciężkich palet (najwyższa klasa wagi) jest {heavy_need}, a miejsc na poziomach "
                             f"1–{heavy_max_level} tylko {low} — część trafi wyżej."))
    return {"capacity": {"positions": total, "need": need_all, "fill_pct": fill, "zones": zones,
                         "heavy_need": heavy_need, "heavy_low_positions": low, "loads": loads,
                         "pallet_racks": len(pallet_racks)},
            "issues": issues}
