"""Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.

Operacje na całej strefie regałów naraz (np. blok VNA „V”, półki „K1”): przesunięcie,
długość rzędów (gniazda), wysokość (poziomy), usunięcie. Do tego kontrola kolizji regałów
i dopasowanie hali do obrysu. Graficzny edytor „jak w grze” to osobna inicjatywa
(edytor układu, część 2) — tu tylko szybkie przeróbki wariantu z generatora.
"""
from .blender_route import bbox, near_pairs, overlap_depth, rack_corners


def zone_summary(racks):
    """{strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla formularza."""
    out = {}
    for r in racks:
        z = out.setdefault(r["zone"], {"zone": r["zone"], "rows": 0, "n_bays": 0, "n_levels": 0})
        z["rows"] += 1
        z["n_bays"] = max(z["n_bays"], r["n_bays"])
        z["n_levels"] = max(z["n_levels"], r["n_levels"])
    return [out[k] for k in sorted(out)]


def apply_zone_edit(racks, zone, *, dx=0.0, dy=0.0, n_bays=None, n_levels=None):
    """Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę zmienionych."""
    changed = []
    for r in racks:
        if r["zone"] != zone:
            continue
        if dx or dy:
            r["x"], r["y"] = round(r["x"] + dx, 2), round(r["y"] + dy, 2)
        if n_bays and n_bays != r["n_bays"]:
            bay_w = r["width"] / max(1, r["n_bays"])
            r["n_bays"], r["width"] = n_bays, round(bay_w * n_bays, 3)
        if n_levels:
            r["n_levels"] = n_levels
        changed.append(r)
    return changed


def _box(r):
    return bbox(rack_corners(r))


def collisions(racks, tol=0.05):
    """Pary regałów nachodzących na siebie o więcej niż `tol` m — obrócone prostokąty (SAT), więc
    regał pod kątem nie „koliduje" fałszywie przez swój obrys osiowy. [(etykieta, etykieta)]"""
    corners = [rack_corners(r) for r in racks]
    return [(f"{racks[i]['zone']}-{racks[i]['rack_id']}", f"{racks[j]['zone']}-{racks[j]['rack_id']}")
            for i, j in near_pairs([bbox(c) for c in corners])
            if overlap_depth(corners[i], corners[j]) > tol]


def fit_floor(racks, width, depth, margin=1.0):
    """Hala co najmniej tak duża, jak obrys regałów (+ margines), nie mniejsza niż podana."""
    for r in racks:
        x0, y0, x1, y1 = _box(r)
        width, depth = max(width, x1 + margin), max(depth, y1 + margin)
    return round(width, 2), round(depth, 2)
