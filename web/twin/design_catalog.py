"""Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.

Czysty Python (bez Django, bez bpy): importuje go zarówno TWINEMA (wskaźniki wariantów),
jak i zestaw projektowy w Blenderze (`tools/blender/twinema_design_kit.py`), więc
pojemność, obrys i wymagania alejek liczą się w obu miejscach identycznie.

Wspólna konwencja geometrii (jak regały modelu magazynu): element ma narożnik (x, y)
na planie hali, oś szerokości wzdłuż kąta `angle`, głębokość „w bok" od frontu.
Jednostki: metry, sekundy, palety (EU 1,2 × 0,8 m).

Wartości domyślne to typowe dane katalogowe (rząd wielkości do porównań wariantów),
nie oferta dostawcy — przed decyzją inwestycyjną zweryfikuj je z dostawcą sprzętu.
"""

PALLET_L, PALLET_W = 1.2, 0.8

ELEMENTS = {
    "rack_std": {
        "label": "Regał paletowy (wózek wysokiego składowania)",
        "group": "składowanie",
        "params": {"bays": 10, "levels": 5, "bay_width": 2.7, "depth": 1.1, "level_h": 1.8,
                   "pallets_per_bay": 3},
        "aisle_m": 3.0,          # reach truck: korytarz roboczy ~2,9–3,2 m
        "equipment": "Wózek wysokiego składowania (reach truck)",
    },
    "rack_vna": {
        "label": "Regał wąskokorytarzowy VNA (wózek systemowy)",
        "group": "składowanie",
        "params": {"bays": 20, "levels": 8, "bay_width": 2.7, "depth": 1.1, "level_h": 1.6,
                   "pallets_per_bay": 3},
        "aisle_m": 1.8,          # wózek systemowy prowadzony szynowo/indukcyjnie
        "equipment": "Wózek systemowy VNA (prowadzenie szynowe / indukcyjne)",
    },
    "shuttle": {
        "label": "Regał kanałowy z shuttlem (składowanie blokowe)",
        "group": "składowanie",
        "params": {"channels": 6, "depth_pallets": 12, "levels": 5, "channel_width": 1.4,
                   "level_h": 1.6},
        "aisle_m": 3.0,          # obsługa czoła kanałów wózkiem
        "equipment": "Wózek satelitarny (shuttle) + wózek wysokiego składowania na czole",
        "throughput_h": 25,      # cykle/h na shuttle (rząd wielkości)
    },
    "amr": {
        "label": "Robot AMR / AGV (transport palet)",
        "group": "transport",
        "params": {"length": 1.3, "width": 0.9, "speed": 1.5},
        "aisle_m": 2.0,          # mijanie się dwóch robotów / robot + pieszy
        "throughput_h": 20,      # zadań/h na robota przy ~60 m trasy
    },
    "amr_station": {
        "label": "Stanowisko kompletacji (towar do człowieka)",
        "group": "kompletacja",
        "params": {"width": 2.5, "depth": 2.0, "ports": 2},
        "throughput_h": 150,     # linii/h na stanowisko
    },
    "conveyor": {
        "label": "Przenośnik rolkowy",
        "group": "transport",
        "params": {"length": 10.0, "width": 0.8, "height": 0.8, "speed": 0.5},
        "throughput_h": 1200,    # kartonów/h
    },
    "sorter": {
        "label": "Sorter z zsypami",
        "group": "transport",
        "params": {"length": 12.0, "width": 1.2, "chutes": 10},
        "throughput_h": 3000,    # kartonów/h
    },
}

RACK_KINDS = ("rack_std", "rack_vna", "shuttle")
SHELF_AISLE_M = 2.0      # regał półkowy, kompletacja ręczna z wózka EPT (strefa K1 generatora)


def params_for(kind, **overrides):
    """Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)."""
    if kind not in ELEMENTS:
        raise ValueError(f"Nieznany element: {kind!r}. Dostępne: {', '.join(ELEMENTS)}")
    params = dict(ELEMENTS[kind]["params"])
    unknown = set(overrides) - set(params)
    if unknown:
        raise ValueError(f"{kind}: nieznane parametry {sorted(unknown)}")
    params.update(overrides)
    return params


def footprint(kind, p):
    """(szerokość wzdłuż osi elementu, głębokość) [m]."""
    if kind in ("rack_std", "rack_vna"):
        return p["bays"] * p["bay_width"], p["depth"]
    if kind == "shuttle":
        return p["channels"] * p["channel_width"], p["depth_pallets"] * (PALLET_L + 0.05)
    if kind in ("amr", ):
        return p["length"], p["width"]
    if kind == "amr_station":
        return p["width"], p["depth"]
    if kind in ("conveyor", "sorter"):
        extra = 1.2 if kind == "sorter" else 0.0     # zsypy po obu stronach
        return p["length"], p["width"] + extra
    raise ValueError(kind)


def height(kind, p):
    if kind in ("rack_std", "rack_vna", "shuttle"):
        return p["levels"] * p["level_h"]
    return {"amr": 0.4, "amr_station": 1.1, "conveyor": p.get("height", 0.8),
            "sorter": 1.0}.get(kind, 1.0)


def pallet_positions(kind, p):
    """Liczba miejsc paletowych elementu (0 dla transportu/kompletacji)."""
    if kind in ("rack_std", "rack_vna"):
        return p["bays"] * p["pallets_per_bay"] * p["levels"]
    if kind == "shuttle":
        return p["channels"] * p["depth_pallets"] * p["levels"]
    return 0


def element_summary(kind, p):
    w, d = footprint(kind, p)
    return {"kind": kind, "label": ELEMENTS[kind]["label"], "width": round(w, 3),
            "depth": round(d, 3), "height": round(height(kind, p), 3),
            "area_m2": round(w * d, 2), "pallet_positions": pallet_positions(kind, p),
            "aisle_m": ELEMENTS[kind].get("aisle_m"),
            "throughput_h": ELEMENTS[kind].get("throughput_h")}


BACK_GAP_M = 0.1          # szczelina między regałami plecami do siebie — jedno źródło (generator, edytor JS)


def block_rows(kind, rows, *, back_to_back=True, aisle=None, **overrides):
    """Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.

    back_to_back=True: pary plecami do siebie (szczelina `BACK_GAP_M`) i korytarz `aisle`
    (domyślnie wymagany przez sprzęt z katalogu) między parami."""
    p = params_for(kind, **overrides)
    _, d = footprint(kind, p)
    aisle = ELEMENTS[kind].get("aisle_m", 3.0) if aisle is None else aisle
    offsets, pos = [], 0.0
    for i in range(rows):
        offsets.append(round(pos, 3))
        gap = BACK_GAP_M if (back_to_back and i % 2 == 0) else aisle
        pos += d + gap
    return offsets


def _proj(e, axis):
    """Rzut 4 narożników elementu na oś: (min, max) [m] — działa dla każdego kąta (też 180°)."""
    from .blender_route import rack_corners

    w, d = footprint(e["kind"], e["params"])
    v = [x * axis[0] + y * axis[1] for x, y in
         rack_corners({"x": e["x"], "y": e["y"], "angle": e["angle"] or 0, "width": w, "depth": d})]
    return min(v), max(v)


def _front_to(r, axis, sign):
    """Czy front regału (strona −u_d regału) patrzy w stronę `sign`·axis."""
    from .blender_route import rack_axes

    ud = rack_axes(r["angle"])[1]
    return (ud[0] * axis[0] + ud[1] * axis[1]) * sign < 0


def _parallel(a, b):
    """Ten sam kierunek osi modulo 180° (0° i 180° = rzędy plecami albo frontami do siebie)."""
    return abs(((a["angle"] or 0) - (b["angle"] or 0) + 90) % 180 - 90) <= 1


def check_aisles(elements):
    """Kontrola szerokości alejek między równoległymi elementami składowania.

    elements: dicty {kind, x, y, angle, params, label, aisle_m?} (`aisle_m` nadpisuje katalog,
    np. półki z kompletacją albo Ast sprzętu). Para równoległa (kąt modulo 180°), nakładająca się
    wzdłuż osi: prześwit liczony z rzutu narożników. Alejka wymagana tylko, gdy w prześwit patrzy
    front któregoś regału (front = strona −u_d regału) i tylko między najbliższymi sąsiadami
    (nie „przez" regał stojący pomiędzy). Szczelina plecami do siebie ≤ 0,3 m — bez alejki.
    `ia`/`ib` = indeksy pary w `elements`."""
    from .blender_route import bbox, near_pairs, rack_axes, rack_corners

    idx = [n for n, e in enumerate(elements) if e["kind"] in RACK_KINDS]
    racks = [elements[n] for n in idx]
    boxes = []
    for e in racks:
        w, d = footprint(e["kind"], e["params"])
        boxes.append(bbox(rack_corners({"x": e["x"], "y": e["y"], "angle": e["angle"], "width": w, "depth": d})))
    pad = max([ELEMENTS[k].get("aisle_m", 0) for k in RACK_KINDS]
              + [e.get("aisle_m") or 0 for e in elements]) + 0.1      # dalej niż alejka = bez znaczenia
    pairs = near_pairs(boxes, pad)
    near = {}
    for i, j in pairs:
        near.setdefault(i, set()).add(j)
        near.setdefault(j, set()).add(i)
    issues = []
    for i, j in pairs:
        a, b = racks[i], racks[j]
        if not _parallel(a, b):
            continue
        u_w, u_d = rack_axes(a["angle"])
        aw, bw = _proj(a, u_w), _proj(b, u_w)
        lo_w, hi_w = max(aw[0], bw[0]), min(aw[1], bw[1])
        if hi_w - lo_w <= 0.2:                              # nie leżą naprzeciw siebie
            continue
        (low, sl), (up, su) = sorted(((_proj(a, u_d), a), (_proj(b, u_d), b)), key=lambda t: t[0][0])
        gap = up[0] - low[1]
        need = max(e.get("aisle_m") or ELEMENTS[e["kind"]].get("aisle_m", 0) for e in (a, b))
        if gap < -0.01:
            kind = "kolizja"
        else:
            facing = _front_to(sl, u_d, +1) or _front_to(su, u_d, -1)
            kind = "za wąska alejka" if facing and 0.3 < gap < need - 0.01 else None
            if kind:                                        # tylko najbliżsi sąsiedzi
                for k in (near.get(i, set()) | near.get(j, set())) - {i, j}:
                    c = racks[k]
                    if not _parallel(a, c):
                        continue
                    cw, cd = _proj(c, u_w), _proj(c, u_d)
                    if min(hi_w, cw[1]) - max(lo_w, cw[0]) > 0.2 and cd[1] > low[1] + 0.01 and cd[0] < up[0] - 0.01:
                        kind = None
                        break
        if kind:
            issues.append({"type": kind, "a": a.get("label"), "b": b.get("label"),
                           "gap_m": round(gap, 2), "need_m": need,
                           "ia": idx[i], "ib": idx[j]})
    return issues


def variant_summary(elements, floor_w, floor_d):
    """Wskaźniki wariantu: miejsca paletowe, powierzchnia zabudowy, sprzęt, naruszenia."""
    by_kind, positions, area = {}, 0, 0.0
    for e in elements:
        s = element_summary(e["kind"], e["params"])
        k = by_kind.setdefault(e["kind"], {"label": s["label"], "count": 0, "pallet_positions": 0})
        k["count"] += 1
        pp = 0 if e.get("shelf") else s["pallet_positions"]
        k["pallet_positions"] += pp
        positions += pp
        area += s["area_m2"]
    floor = floor_w * floor_d
    return {"pallet_positions": positions, "built_area_m2": round(area, 1),
            "floor_area_m2": round(floor, 1),
            "positions_per_m2": round(positions / floor, 3) if floor else 0,
            "by_kind": by_kind, "aisle_issues": check_aisles(elements)}
