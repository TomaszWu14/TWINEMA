"""Działka pod halą (D1) — czysty Python (bez Django), testowalny bez bazy.

Układ działki jak hali: metry, x w prawo, y „w głąb” (na planie w dół), prostokąt [0, width] × [0, depth].
Strony: N = y 0, S = y depth, W = x 0, E = x width („wjazd od południa” = dolna krawędź planu).
Hala leży na działce jak element: narożnik (x, y) + kąt (konwencja `blender_route`: u_w = (cos θ, −sin θ),
u_d = (sin θ, cos θ)), wymiary = podłoga hali. `hall_to_site` / `site_to_hall` to jedyna transformacja.

Format (JSON w `WarehouseModel.site`, pusty = model bez działki — wszystko działa jak dotąd):
  {"width", "depth", "hall": {"x", "y", "angle"},
   "max_height", "max_coverage_pct", "min_bio_pct",      # None = bez ograniczenia
   "setback": {"road", "other"}, "access_side": "N|S|E|W",
   "entries": [{"kind": "truck|car", "side", "pos", "width"}],   # pos = odległość od początku boku (N/S od x 0, W/E od y 0)
   "areas": [{"kind": "yard|parking|green|road", "label", "x", "y", "width", "depth", "angle"}],
   "boundary": [[x, y], …]}   # D2, opcjonalnie: granica-wielokąt (3–64 punkty); width/depth = jej obrys
Granica-wielokąt: odległość od granicy liczona per krawędź — krawędź zwrócona ku stronie dojazdu „od drogi”,
pozostałe „od sąsiadów”; wjazd (strona + pozycja jak dla prostokąta) dosuwany do najbliższego punktu granicy.
Problemy jak w `twin.layout` + klucze `areas` (indeksy elementów terenu) i `hall` (dotyczy całej hali).
"""
import math

from .blender_containers import outward
from .blender_route import overlap_depth, rack_axes, rack_corners
from .layout import ROOF_GAP_M, LayoutError, _num, _text, guess_dock_role

SIDES = ("N", "S", "E", "W")
AREA_KINDS = {"yard": "Plac manewrowy", "parking": "Parking osobowy", "green": "Zieleń (biologicznie czynna)",
              "road": "Droga wewnętrzna"}
PAVED_KINDS = {"yard", "parking", "road"}
TRUCK_ROLES = {"in_container", "in_pallet", "out", "shared"}
YARD_M = 35.0            # plac przed dokiem tira (zestaw ~16,5 m + manewr)
VAN_YARD_M = 20.0        # dok kurierski (bus / solówka)
ROOF_M = 1.0             # konstrukcja dachu nad wysokością w świetle
STEP_M = 2.0             # próbkowanie odcinków (plac, droga)
MAX_AREAS, MAX_ENTRIES = 200, 6
MAX_VERTICES = 64
OUT_DIR = {"N": (0.0, -1.0), "S": (0.0, 1.0), "W": (-1.0, 0.0), "E": (1.0, 0.0)}   # na zewnątrz działki
ROAD_EDGE_COS = 0.7      # krawędź „od drogi”, gdy jej normalna zewnętrzna odchyla się od strony dojazdu < ~45°


# ── wejście z przeglądarki ─────────────────────────────────────────────────────────────────
def _opt(v, what, lo, hi):
    return None if v in (None, "") else _num(v, what, lo, hi)


def clean_site(d):
    """Dane z edytora → znormalizowana działka albo {} (brak działki). LayoutError przy złych danych."""
    if not d:
        return {}
    if not isinstance(d, dict):
        raise LayoutError("Działka: oczekiwany obiekt.")
    boundary = _clean_boundary(d.get("boundary"))
    if boundary:
        out = {"width": round(max(x for x, _ in boundary), 3), "depth": round(max(y for _, y in boundary), 3),
               "boundary": boundary}
    else:
        out = {"width": _num(d.get("width"), "Działka: szerokość", 5, 10000),
               "depth": _num(d.get("depth"), "Działka: głębokość", 5, 10000)}
    hall = d.get("hall") or {}
    if not isinstance(hall, dict):
        raise LayoutError("Działka: położenie hali — oczekiwany obiekt.")
    out["hall"] = {"x": _num(hall.get("x", 0), "Hala na działce: X"), "y": _num(hall.get("y", 0), "Hala na działce: Y"),
                   "angle": _num(hall.get("angle", 0), "Hala na działce: kąt", -3600, 3600) % 360}
    out["max_height"] = _opt(d.get("max_height"), "Działka: maks. wysokość budynku", 2, 200)
    out["max_coverage_pct"] = _opt(d.get("max_coverage_pct"), "Działka: maks. % zabudowy", 1, 100)
    out["min_bio_pct"] = _opt(d.get("min_bio_pct"), "Działka: min. % biologicznie czynnej", 0, 100)
    sb = d.get("setback") or {}
    if not isinstance(sb, dict):
        raise LayoutError("Działka: odległości od granic — oczekiwany obiekt.")
    out["setback"] = {"road": _num(sb.get("road", 0), "Odległość od drogi", 0, 500),
                      "other": _num(sb.get("other", 0), "Odległość od pozostałych granic", 0, 500)}
    out["access_side"] = d.get("access_side") or "S"
    if out["access_side"] not in SIDES:
        raise LayoutError("Działka: strona dojazdu to N, S, E albo W.")
    entries, areas = d.get("entries") or [], d.get("areas") or []
    if not isinstance(entries, list) or len(entries) > MAX_ENTRIES:
        raise LayoutError(f"Działka: maks. {MAX_ENTRIES} wjazdów.")
    if not isinstance(areas, list) or len(areas) > MAX_AREAS:
        raise LayoutError(f"Działka: maks. {MAX_AREAS} elementów terenu.")
    out["entries"] = []
    for i, e in enumerate(entries, 1):
        if not isinstance(e, dict) or e.get("side") not in SIDES or e.get("kind", "truck") not in ("truck", "car"):
            raise LayoutError(f"Wjazd {i}: strona N/S/E/W, rodzaj truck/car.")
        length = out["width"] if e["side"] in "NS" else out["depth"]
        out["entries"].append({"kind": e.get("kind", "truck"), "side": e["side"],
                               "pos": _num(e.get("pos"), f"Wjazd {i}: położenie na granicy", 0, length),
                               "width": _num(e.get("width", 8), f"Wjazd {i}: szerokość", 3, 50)})
    out["areas"] = []
    for i, a in enumerate(areas, 1):
        if not isinstance(a, dict) or a.get("kind") not in AREA_KINDS:
            raise LayoutError(f"Element terenu {i}: rodzaj {', '.join(AREA_KINDS)}.")
        out["areas"].append({"kind": a["kind"], "label": _text(a.get("label"), f"Element terenu {i}: etykieta", 100,
                                                               required=False),
                             "x": _num(a.get("x"), f"Element terenu {i}: X"), "y": _num(a.get("y"), f"Element terenu {i}: Y"),
                             "width": _num(a.get("width"), f"Element terenu {i}: szerokość", 0.5, 10000),
                             "depth": _num(a.get("depth"), f"Element terenu {i}: głębokość", 0.5, 10000),
                             "angle": _num(a.get("angle", 0), f"Element terenu {i}: kąt", -3600, 3600) % 360})
    return out


def _clean_boundary(raw):
    """Granica-wielokąt: lista [x, y] (≥ 0), 3–MAX_VERTICES punktów, pole > 1 m²; brak → None (prostokąt)."""
    if raw in (None, "", []):
        return None
    if not isinstance(raw, list) or not 3 <= len(raw) <= MAX_VERTICES:
        raise LayoutError(f"Granica działki: od 3 do {MAX_VERTICES} wierzchołków.")
    pts = []
    for i, p in enumerate(raw, 1):
        if not isinstance(p, (list, tuple)) or len(p) != 2:
            raise LayoutError(f"Granica działki: wierzchołek {i} — oczekiwane [x, y].")
        pts.append((_num(p[0], f"Wierzchołek {i}: X", 0, 10000), _num(p[1], f"Wierzchołek {i}: Y", 0, 10000)))
    if abs(polygon_area(pts)) < 1:
        raise LayoutError("Granica działki: wierzchołki nie tworzą wielokąta (pole ≈ 0).")
    # ponytail: bez sprawdzania samoprzecięć — przy „ósemce” pole i testy punktów będą mylące; dodać, gdy
    # granice zaczną przychodzić z importu, a nie tylko z edytora.
    return [[round(x, 3), round(y, 3)] for x, y in pts]


# ── wielokąt granicy (D2) ──────────────────────────────────────────────────────────────────
def polygon_area(pts):
    """Pole ze znakiem (wzór Gaussa); > 0 = punkty zgodnie z ruchem wskazówek przy y w dół planu."""
    return sum(a[0] * b[1] - b[0] * a[1] for a, b in zip(pts, pts[1:] + pts[:1], strict=True)) / 2


def plot_polygon(site):
    """Granica działki jako lista punktów: wielokąt albo prostokąt [0, W] × [0, D]."""
    if site.get("boundary"):
        return [tuple(p) for p in site["boundary"]]
    W, D = site["width"], site["depth"]
    return [(0.0, 0.0), (W, 0.0), (W, D), (0.0, D)]


def _edges(pts):
    return list(zip(pts, pts[1:] + pts[:1], strict=True))


def _outward_normal(a, b, sign):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L = math.hypot(dx, dy) or 1.0
    return (dy / L * sign, -dx / L * sign)


def edge_setbacks(site):
    """Odległość od granicy dla każdej krawędzi wielokąta (kolejność `plot_polygon`)."""
    pts = plot_polygon(site)
    sign = 1.0 if polygon_area(pts) > 0 else -1.0
    road = OUT_DIR[site["access_side"]]
    out = []
    for a, b in _edges(pts):
        n = _outward_normal(a, b, sign)
        out.append(site["setback"]["road"] if n[0] * road[0] + n[1] * road[1] > ROAD_EDGE_COS
                   else site["setback"]["other"])
    return out


def dist_segment(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    L2 = dx * dx + dy * dy
    t = 0.0 if not L2 else max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


def in_polygon(pts, p):
    """Punkt w wielokącie (promień w prawo, parzystość przecięć)."""
    inside = False
    for (x0, y0), (x1, y1) in _edges(pts):
        if (y0 > p[1]) != (y1 > p[1]) and p[0] < x0 + (p[1] - y0) * (x1 - x0) / (y1 - y0):
            inside = not inside
    return inside


def in_plot(site, p, tol=0.0):
    """Punkt na działce (z tolerancją przy granicy)."""
    pts = plot_polygon(site)
    return in_polygon(pts, p) or (tol > 0 and min(dist_segment(p, a, b) for a, b in _edges(pts)) <= tol)


def _buildable(site, p, setbacks_):
    pts = plot_polygon(site)
    return in_polygon(pts, p) and all(dist_segment(p, a, b) >= sb - 0.01 for (a, b), sb in zip(_edges(pts), setbacks_, strict=True))


def buildable_m2(site):
    """Pole w liniach zabudowy: prostokąt — dokładnie; wielokąt — próbkowanie siatki co STEP_M."""
    if not site.get("boundary"):
        b = building_rect(site)
        return (b[2] - b[0]) * (b[3] - b[1]) if b else 0.0
    sbs = edge_setbacks(site)
    n = sum(_buildable(site, (x + STEP_M / 2, y + STEP_M / 2), sbs)
            for x in _frange(0, site["width"], STEP_M) for y in _frange(0, site["depth"], STEP_M))
    return n * STEP_M * STEP_M


def _frange(a, b, step):
    v = a
    while v < b:
        yield v
        v += step


# ── geometria ──────────────────────────────────────────────────────────────────────────────
def hall_to_site(site, p):
    """Punkt hali (x, y) → punkt działki."""
    h = site["hall"]
    u_w, u_d = rack_axes(h["angle"])
    return (h["x"] + u_w[0] * p[0] + u_d[0] * p[1], h["y"] + u_w[1] * p[0] + u_d[1] * p[1])


def site_to_hall(site, p):
    """Punkt działki → punkt hali (odwrotność `hall_to_site`; osie ortonormalne)."""
    h = site["hall"]
    u_w, u_d = rack_axes(h["angle"])
    dx, dy = p[0] - h["x"], p[1] - h["y"]
    return (dx * u_w[0] + dy * u_w[1], dx * u_d[0] + dy * u_d[1])


def hall_rect(site, floor):
    return {**site["hall"], "width": floor["width"], "depth": floor["depth"]}


def _inside(rect, p, tol=0.0):
    """Punkt w obróconym prostokącie (narożnik + kąt)."""
    u_w, u_d = rack_axes(rect.get("angle", 0))
    dx, dy = p[0] - rect["x"], p[1] - rect["y"]
    a, c = dx * u_w[0] + dy * u_w[1], dx * u_d[0] + dy * u_d[1]
    return -tol <= a <= rect["width"] + tol and -tol <= c <= rect["depth"] + tol


def setbacks(site):
    """Odległość od granicy per strona: strona dojazdu = od drogi, pozostałe = od sąsiadów."""
    sb = site["setback"]
    return {s: sb["road"] if s == site["access_side"] else sb["other"] for s in SIDES}


def building_rect(site):
    """Obszar w liniach zabudowy (osiowy prostokąt) albo None, gdy odległości go zjadają."""
    s = setbacks(site)
    x0, y0, x1, y1 = s["W"], s["N"], site["width"] - s["E"], site["depth"] - s["S"]
    return (x0, y0, x1, y1) if x1 > x0 and y1 > y0 else None


def entry_point(site, e, inset=0.0):
    """Środek wjazdu na granicy (inset > 0 — tyle metrów w głąb działki). Granica-wielokąt: z punktu na boku
    obrysu promień w głąb działki do pierwszej krawędzi granicy (brak → najbliższa), wcięcie wzdłuż jej normalnej."""
    W, D = site["width"], site["depth"]
    if not site.get("boundary"):
        return {"N": (e["pos"], inset), "S": (e["pos"], D - inset),
                "W": (inset, e["pos"]), "E": (W - inset, e["pos"])}[e["side"]]
    p = {"N": (e["pos"], 0.0), "S": (e["pos"], D), "W": (0.0, e["pos"]), "E": (W, e["pos"])}[e["side"]]
    pts = plot_polygon(site)
    sign = 1.0 if polygon_area(pts) > 0 else -1.0
    hit = _ray_hit(pts, p, tuple(-v for v in OUT_DIR[e["side"]]))
    if hit is None:
        a, b = min(_edges(pts), key=lambda ab: dist_segment(p, *ab))
        dx, dy = b[0] - a[0], b[1] - a[1]
        t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / ((dx * dx + dy * dy) or 1.0)))
        hit = (a, b, (a[0] + t * dx, a[1] + t * dy))
    a, b, q = hit
    n = _outward_normal(a, b, sign)
    return (q[0] - n[0] * inset, q[1] - n[1] * inset)


def _ray_hit(pts, p, d):
    """Pierwsze przecięcie promienia p + s·d (s ≥ 0) z krawędzią wielokąta → (a, b, punkt) albo None."""
    best = None
    for a, b in _edges(pts):
        ex, ey = b[0] - a[0], b[1] - a[1]
        den = d[0] * ey - d[1] * ex
        if abs(den) < 1e-12:
            continue
        wx, wy = a[0] - p[0], a[1] - p[1]
        s_, t = (wx * ey - wy * ex) / den, (wx * d[1] - wy * d[0]) / den
        if s_ >= -1e-9 and -1e-9 <= t <= 1 + 1e-9 and (best is None or s_ < best[0]):
            best = (s_, a, b, (p[0] + s_ * d[0], p[1] + s_ * d[1]))
    return best and best[1:]


def _area_m2(a):
    return a["width"] * a["depth"]


def building_height(floor, racks):
    """Wysokość budynku: wysokość w świetle (albo najwyższy regał + zapas) + konstrukcja dachu."""
    top = max((r["n_levels"] * r["level_height_cm"] / 100 for r in racks), default=0.0)
    clear = floor.get("clear_height") or (top + ROOF_GAP_M if top else 0.0)
    return round(max(clear, top + ROOF_GAP_M if top else 0.0) + ROOF_M, 2)


def site_kpi(site, floor, racks=()):
    plot = abs(polygon_area(plot_polygon(site)))
    hall = floor["width"] * floor["depth"]
    by_kind = {}
    for a in site["areas"]:
        by_kind[a["kind"]] = by_kind.get(a["kind"], 0.0) + _area_m2(a)
    buildable = buildable_m2(site)
    cap = min(buildable, plot * site["max_coverage_pct"] / 100) if site["max_coverage_pct"] else buildable
    def pct(v):
        return round(100 * v / plot, 1)
    return {"plot_m2": round(plot), "hall_m2": round(hall), "coverage_pct": pct(hall),
            "bio_pct": pct(by_kind.get("green", 0.0)), "paved_pct": pct(sum(by_kind.get(k, 0.0) for k in PAVED_KINDS)),
            "reserve_m2": round(max(0.0, cap - hall)), "building_height_m": building_height(floor, racks)}


def _issue(code, severity, message, features=(), areas=(), hall=False):
    return {"code": code, "severity": severity, "message": message, "racks": [], "features": sorted(set(features)),
            "areas": sorted(set(areas)), "hall": hall}


def _segment(a, b):
    n = max(1, int(math.dist(a, b) // STEP_M))
    return [(a[0] + (b[0] - a[0]) * k / n, a[1] + (b[1] - a[1]) * k / n) for k in range(n + 1)]


def check_site(site, floor, racks, features):
    """Problemy działki (format `twin.layout`): linie zabudowy, % zabudowy, wysokość, zieleń, plac
    przed dokami, droga od wjazdu do doków, wjazdy."""
    if not site:
        return []
    issues, kpi = [], site_kpi(site, floor, racks)
    W, D = site["width"], site["depth"]
    plot = {"x": 0.0, "y": 0.0, "angle": 0.0, "width": W, "depth": D}
    hall = hall_rect(site, floor)
    corners = rack_corners(hall)

    if not _within_building_line(site, hall, corners):
        sb = site["setback"]
        issues.append(_issue("building_line", "error", f"Hala wychodzi poza linie zabudowy (od drogi {sb['road']:g} m, "
                                                       f"od pozostałych granic {sb['other']:g} m).", hall=True))
    if site["max_coverage_pct"] and kpi["coverage_pct"] > site["max_coverage_pct"] + 1e-9:
        issues.append(_issue("coverage", "error", f"Zabudowa {kpi['coverage_pct']:g} % działki — ponad dopuszczalne "
                                                  f"{site['max_coverage_pct']:g} %.", hall=True))
    if site["max_height"] and kpi["building_height_m"] > site["max_height"] + 1e-9:
        issues.append(_issue("site_height", "error", f"Budynek ~{kpi['building_height_m']:g} m (wysokość w świetle / "
                                                     f"regały + {ROOF_M:g} m dachu) — ponad dopuszczalne "
                                                     f"{site['max_height']:g} m.", hall=True))
    if site["min_bio_pct"] and kpi["bio_pct"] < site["min_bio_pct"] - 1e-9:
        issues.append(_issue("bio", "error", f"Powierzchnia biologicznie czynna {kpi['bio_pct']:g} % — wymagane "
                                             f"min. {site['min_bio_pct']:g} %. Dorysuj zieleń.",
                             areas=[i for i, a in enumerate(site["areas"]) if a["kind"] == "green"]))
    for i, a in enumerate(site["areas"]):
        if overlap_depth(rack_corners(a), corners) > 0.05:
            issues.append(_issue("area_hall", "warning", f"„{a['label'] or AREA_KINDS[a['kind']]}” zachodzi pod halę.",
                                 areas=[i], hall=True))
        if any(not in_plot(site, p, 0.05) for p in rack_corners(a)):
            issues.append(_issue("area_outside", "warning", f"„{a['label'] or AREA_KINDS[a['kind']]}” wychodzi poza "
                                                            "działkę.", areas=[i]))
    for i, e in enumerate(site["entries"]):
        if e["kind"] == "truck" and e["side"] != site["access_side"]:
            issues.append(_issue("entry_side", "error", f"Wjazd {i + 1} jest od strony {e['side']}, a dojazd do działki "
                                                        f"od strony {site['access_side']}."))
    issues += _dock_issues(site, floor, features, plot)
    return issues


def _within_building_line(site, hall, corners):
    """Hala w liniach zabudowy: prostokąt — jak D1; wielokąt — narożniki na działce z odstępem od każdej
    krawędzi i żaden wierzchołek granicy (wcięcie działki) nie wchodzi w halę."""
    if not site.get("boundary"):
        b = building_rect(site)
        return bool(b) and all(b[0] - 0.01 <= x <= b[2] + 0.01 and b[1] - 0.01 <= y <= b[3] + 0.01 for x, y in corners)
    # Odcinki bez przecięcia są najbliżej w którymś końcu: narożniki hali ↔ krawędzie granicy (_buildable)
    # i wierzchołki granicy ↔ boki hali (wklęsłe „wcięcie” działki podchodzące pod bok hali).
    sbs, pts = edge_setbacks(site), plot_polygon(site)
    if not all(_buildable(site, c, sbs) for c in corners):
        return False
    sides = list(zip(corners, corners[1:] + corners[:1], strict=True))
    for i, v in enumerate(pts):
        need = min(sbs[i - 1], sbs[i])                 # krawędzie schodzące się w wierzchołku
        if _inside(hall, v, -0.01) or min(dist_segment(v, a, b) for a, b in sides) < need - 0.01:
            return False
    return True


def _dock_issues(site, floor, features, plot):
    """Plac przed dokami tirów (min. YARD_M) i droga od najbliższego wjazdu tirów do placu doku."""
    blocked = [a for a in site["areas"] if a["kind"] in ("green", "parking")]
    paved = [a for a in site["areas"] if a["kind"] in ("yard", "road")]
    hall = hall_rect(site, floor)
    trucks = [entry_point(site, e, inset=1.0) for e in site["entries"] if e["kind"] == "truck"]

    def ok(p):
        return (in_plot(site, p) and not _inside(hall, p, -0.01) and not any(_inside(a, p) for a in blocked)
                and (not paved or any(_inside(a, p, 0.5) for a in paved)))

    out, no_yard, bad_route = [], [], []
    for j, f in enumerate(features):
        if f["kind"] not in ("dock", "gate"):
            continue
        role = f.get("dock_role") or guess_dock_role(f.get("label"))
        need = YARD_M if role in TRUCK_ROLES else VAN_YARD_M
        u_w, u_d = rack_axes(f.get("angle", 0))
        c = (f["x"] + (u_w[0] * f["width"] + u_d[0] * f["depth"]) / 2, f["y"] + (u_w[1] * f["width"] + u_d[1] * f["depth"]) / 2)
        n = outward(c, floor)
        wall = ((floor["width"] if n[0] > 0 else 0.0) if n[0] else c[0],
                (floor["depth"] if n[1] > 0 else 0.0) if n[1] else c[1])
        pts = [hall_to_site(site, (wall[0] + n[0] * k, wall[1] + n[1] * k)) for k in range(2, int(need) + 1, int(STEP_M))]
        if not all(ok(p) for p in pts):
            no_yard.append(j)
        elif trucks and role in TRUCK_ROLES:
            # ponytail: droga = odcinek prosty od najbliższego wjazdu do końca placu; przy krętych drogach
            # wewnętrznych — trasowanie po obszarach „road/yard” (graf siatki jak blender_route).
            far = pts[-1]
            route = _segment(min(trucks, key=lambda t: math.dist(t, far)), far)
            if any(any(_inside(a, p) for a in blocked) for p in route):
                bad_route.append(j)
    if no_yard:
        out.append(_issue("dock_yard", "warning", f"{len(no_yard)} dok(ów) bez wolnego placu przed bramą "
                                                  f"(tir: {YARD_M:g} m, bus: {VAN_YARD_M:g} m na działce, bez zieleni i parkingu).",
                          features=no_yard))
    if bad_route:
        out.append(_issue("route", "warning", f"Droga od wjazdu do {len(bad_route)} dok(ów) przecina zieleń albo parking.",
                          features=bad_route))
    return out


# ── działka domyślna (generator, „Dodaj działkę” w edytorze) ──────────────────────────────────
def default_site(floor, *, side_yards=("W", "E"), max_height=None):
    """Działka wokół hali: place 35 + 10 m przy ścianach z dokami (W/E), droga i parking od południa
    (strona dojazdu), pas zieleni od północy dobrany do ≥ 22 % (wymóg demo 20 %), zabudowa ≤ 55 %.
    Wartości syntetyczne (anonimowy scenariusz): wysokość z hali + zapas, odległości 6 m / od drogi 12 m."""
    Wh, Dh = floor["width"], floor["depth"]
    yard = YARD_M + 10
    left, right = (yard if "W" in side_yards else 12.0), (yard if "E" in side_yards else 12.0)
    south = 12.0 + 24.0                                   # droga wzdłuż hali + parking pod nią
    W = Wh + left + right
    north = max(10.0, math.ceil(0.22 * (Dh + south) / 0.78))
    while Wh * Dh / (W * (north + Dh + south)) > 0.55:
        north += 2
    D = north + Dh + south
    y_road = north + Dh
    areas = [{"kind": "green", "label": "Zieleń — pas północny", "x": 0, "y": 0, "width": W, "depth": north, "angle": 0},
             {"kind": "road", "label": "Droga wzdłuż hali", "x": 0, "y": y_road, "width": W, "depth": 12.0, "angle": 0},
             {"kind": "parking", "label": "Parking osobowy", "x": left + 10, "y": y_road + 12, "width": max(10.0, Wh - 20),
              "depth": south - 12, "angle": 0}]
    if left > 12:
        areas += [{"kind": "yard", "label": "Plac manewrowy — przyjęcia", "x": 0, "y": north, "width": left, "depth": Dh, "angle": 0},
                  {"kind": "road", "label": "Wjazd tirów — zachód", "x": 0, "y": y_road + 12, "width": left, "depth": south - 12, "angle": 0}]
    if right > 12:
        areas += [{"kind": "yard", "label": "Plac manewrowy — wydania", "x": W - right, "y": north, "width": right, "depth": Dh, "angle": 0},
                  {"kind": "road", "label": "Wjazd tirów — wschód", "x": W - right, "y": y_road + 12, "width": right,
                   "depth": south - 12, "angle": 0}]
    entries = [{"kind": "truck", "side": "S", "pos": round(left / 2, 2), "width": 10.0}]
    if right > 12:
        entries.append({"kind": "truck", "side": "S", "pos": round(W - right / 2, 2), "width": 10.0})
    entries.append({"kind": "car", "side": "S", "pos": round(W / 2, 2), "width": 6.0})
    height = max_height or max(15.0, math.ceil((floor.get("clear_height") or 12.0) + ROOF_M + 2))
    return {"width": round(W, 2), "depth": round(D, 2), "hall": {"x": round(left, 2), "y": round(north, 2), "angle": 0.0},
            "max_height": float(height), "max_coverage_pct": 60.0, "min_bio_pct": 20.0,
            "setback": {"road": 12.0, "other": 6.0}, "access_side": "S", "entries": entries,
            "areas": [{**a, "x": round(a["x"], 2), "y": round(a["y"], 2), "width": round(a["width"], 2),
                       "depth": round(a["depth"], 2)} for a in areas]}
