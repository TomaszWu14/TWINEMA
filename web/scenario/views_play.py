"""Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu reprezentatywnego z S3a.

Zdarzenia JS pobiera z `run_events` (format `twinema.scenario-events` v1); tu tylko miejsca z layoutu
(gdzie stoi brama, doki, pola odkładcze, stanowiska) i mapowanie wąskich gardeł na miejsca + okna czasu.
Funkcje `layout_places` i `bottleneck_focus` są czyste (bez Django) — testowane osobno."""
import re

from django.shortcuts import get_object_or_404, render

from core.roles import any_role
from twin.blender_containers import outward
from twin.design_kpi import _center
from twin.shared import HALL_FEATURE_COLORS, safe_json
from twin.views.warehouse_model import model_scene_data

from .models import ScenarioRun
from .sim.places import places_from_features, staging_side

SPEEDS = (10, 30, 60, 120, 300)


def _rect(f):
    return {"x": f["x"], "y": f["y"], "w": f["width"] or 1.0, "d": f["depth"] or 1.0, "angle": f.get("angle") or 0.0}


def _station(features, words):
    return [_rect(f) for f in features
            if f["kind"] == "station" and any(w in (f.get("label") or "").lower() for w in words)]


def layout_places(features, floor):
    """features: dicty `hall_feature_dict` (+ słupy), floor {width, depth} → miejsca dla odtwarzacza:
    docks {id: {x, y, out, wall, role}} (środek doku, kierunek „na zewnątrz” hali, punkt doku na ścianie),
    gate [x, y] (przed ścianą z największą liczbą doków),
    staging_in / staging_out / palletize / pack / returns / charging: listy prostokątów."""
    pl = places_from_features([f for f in features if f["kind"] != "column"])
    role = {str(d["id"]): d["role"] for d in pl["docks"]}
    docks = {}
    for f in features:
        if f["kind"] not in ("dock", "gate") or f.get("id") is None:
            continue
        c = _center(f["x"], f["y"], f.get("angle") or 0, f["width"] or 0, f["depth"] or 0)
        o = outward(c, floor)
        wall = [floor["width"] if o[0] > 0 else 0 if o[0] < 0 else c[0],
                floor["depth"] if o[1] > 0 else 0 if o[1] < 0 else c[1]]
        docks[str(f["id"])] = {"x": round(c[0], 2), "y": round(c[1], 2), "out": o,
                               "wall": [round(v, 2) for v in wall], "role": role.get(str(f["id"]), "out")}
    if docks:
        # Średnia doków z dwóch ścian wypada w środku hali — brama przed ścianą z większością doków.
        sides = {}
        for d in docks.values():
            sides.setdefault(d["out"], []).append(d)
        o, side = max(sides.items(), key=lambda kv: len(kv[1]))
        mid = (sum(d["wall"][0] for d in side) / len(side), sum(d["wall"][1] for d in side) / len(side))
        gate = [round(mid[0] + o[0] * 35, 2), round(mid[1] + o[1] * 35, 2)]
    else:
        gate = [floor["width"] / 2, floor["depth"] + 30]
    staging = {"in": [], "out": []}
    for f in features:
        if f["kind"] == "staging":
            side = staging_side(f.get("label"))
            for s in ([side] if side else ["in", "out"]):
                staging[s].append(_rect(f))
    return {"docks": docks, "gate": gate, "staging_in": staging["in"], "staging_out": staging["out"],
            "palletize": _station(features, ("paletyz", "przepak")),
            "pack": _station(features, ("pakow", "pacz")),
            "returns": [_rect(f) for f in features if f["kind"] == "returns"],
            "charging": [_rect(f) for f in features if f["kind"] == "charging"]}


# Obszar wąskiego gardła (S3a `report.bottlenecks` → `area`) → klucze miejsc w scenie.
AREA_PLACES = [("Doki kontenerowe", "role:in_container"), ("Doki paletowe", "role:in_pallet"),
               ("Doki wydań", "role:out"), ("Pole odkładcze przyjęć", "staging_in"),
               ("Pole odkładcze wydań", "staging_out"), ("Pakowanie", "pack"), ("Paletyzacja", "palletize"),
               ("Rozładunek", "role:in_container role:in_pallet"), ("Załadunek", "role:out"),
               ("Zwroty", "returns"), ("Flota", "charging"), ("Wydania", "role:out")]
_WIN = re.compile(r"(\d{1,2}):(\d{2})\s*[–-]\s*(\d{1,2}):(\d{2})")


def bottleneck_focus(b, places):
    """Wąskie gardło → {t0, t1 [s], keys: ['dock:<id>' | 'staging_in' | …]} dla podświetlenia w 3D."""
    keys = []
    for prefix, spec in AREA_PLACES:
        if b["area"].startswith(prefix):
            for k in spec.split():
                if k.startswith("role:"):
                    keys += [f"dock:{i}" for i, d in places["docks"].items() if d["role"] in (k[5:], "shared")]
                elif places.get(k):
                    keys.append(k)
            break
    m = _WIN.search(b.get("window") or "")
    t0, t1 = ((int(m[1]) * 60 + int(m[2])) * 60, (int(m[3]) * 60 + int(m[4])) * 60) if m else (None, None)
    if t0 is not None and t1 <= t0:
        t1 += 24 * 3600
    return {"t0": t0, "t1": t1, "keys": keys}


def peak_index(timeline):
    """Indeks kroku osi czasu (co 15 min) z największym obciążeniem: auta w kolejce + palety na polach."""
    n = len(timeline["t"])
    load = [sum(timeline.get(k, [0] * n)[i] for k in ("queue_in_container", "queue_in_pallet", "queue_out",
                                                     "staging_in", "staging_out")) for i in range(n)]
    return max(range(n), key=lambda i: (load[i], -i)) if n else 0


@any_role
def run_play(request, pk):
    run = get_object_or_404(ScenarioRun.objects.select_related("model", "scenario"), pk=pk)
    wm = run.model
    racks, features, _ = model_scene_data(wm)
    floor = {"width": wm.floor_width_m, "depth": wm.floor_depth_m}
    places = layout_places(features, floor)
    tl = run.result.get("rep", {}).get("timeline") or {"t": []}
    bns = [{**b, **bottleneck_focus(b, places)} for b in run.result.get("bottlenecks", [])]
    peak = peak_index(tl)
    people = {p: v["busy"] for p, v in (tl.get("people") or {}).items()}
    return render(request, "scenario/play.html", {
        "run": run, "wm": wm, "bottlenecks": bns, "peak_t": peak * 900, "speeds": SPEEDS,
        "has_events": bool(run.events),
        "data_json": safe_json({
            "floor": floor, "racks": racks, "features": features, "places": places, "bottlenecks": bns,
            "site": wm.site or {},
            "timeline": {"step_s": 900, "fleet_busy": tl.get("fleet_busy", []), "people": people},
            "peak_t": peak * 900, "colors": {"staging": HALL_FEATURE_COLORS["staging"]},
        }),
    })
