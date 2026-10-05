"""ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu rotacji.

Cechy materiału z historii pobrań (dni robocze): log(1 + pobrania), zmienność dzienna (CV),
udział dni z ruchem i — gdy jest w danych materiałowych — objętość kartonu. Standaryzacja z-score,
k-means++ z ustalonym ziarnem (powtarzalny wynik), k = 4 domyślnie. Segmenty nazywane po
centroidach: rotacja (wysoka/średnia/niska) × regularność → rekomendacja miejsca w hali.
Obok ABC×XYZ, żeby było widać, co klasteryzacja wnosi ponad klasyczny podział. Czysty Python.
"""
import math
import random
import statistics

VERSION = "segmentation-v1"
FEATURES = [("hits", "Pobrania (log)"), ("cv", "Zmienność dzienna (CV)"), ("active", "Dni z ruchem [%]"),
            ("volume", "Objętość kartonu [dm³]")]


def features(material_days, days, volumes=None):
    """{materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem."""
    day_set, out = set(days), {}
    for m, per_day in material_days.items():
        series = [per_day.get(d, 0) for d in days]
        hits = sum(n for d, n in per_day.items() if d in day_set)
        if not hits:
            continue
        mean = statistics.fmean(series)
        row = {"hits": math.log1p(hits), "cv": statistics.pstdev(series) / mean if mean else 0.0,
               "active": 100 * sum(1 for v in series if v) / len(series), "raw_hits": hits}
        if volumes and volumes.get(m):
            row["volume"] = volumes[m]
        out[m] = row
    return out


def _standardize(rows, keys):
    stats = {}
    for k in keys:
        vals = [r[k] for r in rows]
        mu, sd = statistics.fmean(vals), statistics.pstdev(vals) or 1.0
        stats[k] = (mu, sd)
    return [[(r[k] - stats[k][0]) / stats[k][1] for k in keys] for r in rows], stats


def _dist2(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b, strict=True))


def kmeans(points, k, seed=42, iters=60):
    """k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego ziarna."""
    rng = random.Random(seed)
    centers = [points[rng.randrange(len(points))]]
    while len(centers) < k:
        d2 = [min(_dist2(p, c) for c in centers) for p in points]
        total = sum(d2)
        if not total:
            break
        r, acc = rng.random() * total, 0.0
        for p, w in zip(points, d2, strict=True):
            acc += w
            if acc >= r:
                centers.append(p)
                break
    assign = [0] * len(points)
    for _ in range(iters):
        new = [min(range(len(centers)), key=lambda c, p=p: _dist2(p, centers[c])) for p in points]
        if new == assign and _ > 0:
            break
        assign = new
        for c in range(len(centers)):
            members = [p for p, a in zip(points, assign, strict=True) if a == c]
            if members:
                centers[c] = [statistics.fmean(col) for col in zip(*members, strict=True)]
    inertia = sum(_dist2(p, centers[a]) for p, a in zip(points, assign, strict=True))
    return assign, centers, inertia


def _name(profile, ranks):
    """Nazwa i rekomendacja z pozycji centroidu wśród segmentów (rotacja, regularność)."""
    rot = ["Rotujące szybko", "Rotacja średnia", "Rotacja niska", "Sporadyczne"][min(ranks["hits"], 3)]
    regular = "stabilne" if profile["cv"] < 1.0 else "zmienne"
    if ranks["hits"] == 0:
        place = "Strefa szybka przy kompletacji/wydaniu, poziom 1 (złota strefa)"
    elif ranks["hits"] == 1:
        place = "Poziomy 1–2 blisko czoła rzędu"
    else:
        place = "Wyższe poziomy / głąb hali (VNA)"
    if profile["cv"] >= 1.5 and ranks["hits"] <= 1:
        place += "; bufor na szczyty (zmienny popyt)"
    return f"{rot}, {regular}", place


def segment(material_days, days, volumes=None, k=4, abc=None, xyz=None):
    """→ wynik do zapisu w ModelRun: segmenty z profilem, liczebnością, udziałem pobrań,
    krzyżówka z ABC×XYZ (gdy podane) i przypisanie materiałów."""
    feats = features(material_days, days, volumes)
    if len(feats) < k * 3:
        return {"ok": False, "reason": f"Za mało materiałów z ruchem ({len(feats)}) na {k} segmenty."}
    mats = sorted(feats)
    keys = ["hits", "cv", "active"] + (["volume"] if all("volume" in feats[m] for m in mats) else [])
    rows = [feats[m] for m in mats]
    pts, _ = _standardize(rows, keys)
    assign, _, inertia = kmeans(pts, k)
    total_hits = sum(r["raw_hits"] for r in rows) or 1
    segs = []
    for c in range(k):
        members = [i for i, a in enumerate(assign) if a == c]
        if not members:
            continue
        prof = {key: round(statistics.fmean(rows[i][key] for i in members), 3) for key in keys}
        hits = sum(rows[i]["raw_hits"] for i in members)
        segs.append({"id": c, "skus": len(members), "hits": hits, "share_pct": round(100 * hits / total_hits, 1),
                     "profile": prof, "avg_hits": round(hits / len(members), 1),
                     "examples": [mats[i] for i in sorted(members, key=lambda i: -rows[i]["raw_hits"])[:5]]})
    order = sorted(segs, key=lambda s: -s["avg_hits"])
    for rank, s in enumerate(order):
        s["name"], s["placement"] = _name(s["profile"], {"hits": rank})
    remap = {s["id"]: i for i, s in enumerate(order)}
    for i, s in enumerate(order):
        s["id"] = i
    assignment = {m: remap[a] for m, a in zip(mats, assign, strict=True)}
    cross = None
    if abc and xyz:
        cross = [{"segment": s["id"], "cells": {f"{a}{x}": 0 for a in "ABC" for x in "XYZ"}} for s in order]
        for m, sid in assignment.items():
            key = f"{abc.get(m, 'C')}{xyz.get(m, 'Z')}"
            cross[sid]["cells"][key] += 1
    return {"ok": True, "version": VERSION, "k": k, "features": keys, "inertia": round(inertia, 1),
            "skus": len(mats), "segments": order, "cross": cross, "assignment": assignment}


def _demo():
    rng = random.Random(3)
    days = list(range(60))
    md = {}
    for i in range(40):                       # szybkie, regularne
        md[f"F{i}"] = {d: 20 + rng.randrange(5) for d in days}
    for i in range(40):                       # wolne, sporadyczne
        md[f"S{i}"] = {d: 1 for d in rng.sample(days, 4)}
    r = segment(md, days, k=2)
    seg_of = r["assignment"]
    assert len({seg_of[f"F{i}"] for i in range(40)}) == 1 and seg_of["F0"] == 0
    assert seg_of["S0"] == 1 and r["segments"][0]["share_pct"] > 90


if __name__ == "__main__":
    _demo()
    print("segmentation OK")
