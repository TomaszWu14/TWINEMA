"""Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).

Zadania trafiają do kolejki w porządku chwili zwolnienia (heapq); każde bierze zasób, który najwcześniej
może zacząć: dok (wolny od), ludzi procesu (zmiany z przerwą na końcu zmiany) albo wózek (bateria →
ładowanie). Kolejki aut przy dokach, palety na polach odkładczych i opóźnienia wynikają z tego wprost.
ponytail: zasoby zachłanne (pierwszy wolny), bez priorytetów i bez tras w hali — czas wózka = norma
na ruch; trasy i blokady korytarzy są w `twin.design_sim`, gdy kalibracja pokaże rozjazd.

Przepływy: IN — rozładunek (dok + osoby) → paletyzacja kontenera / przepakowanie mix → kontrola (%)
→ pole odkładcze przyjęć → wózek na regał; cross-dock IN → pole wydań → auto cross-dock OUT.
OUT — wózek z regału (pełne) albo kompletacja + owijanie → pole wydań → załadunek (dok + osoba);
zamówienia → kompletacja → pakowanie i nadanie → odbiór kuriera (cut-off); zwroty → stanowisko → regał.
"""
import heapq
import math
import zlib

from ..staffing import span

M2_PER_PALLET = 1.5             # paleta EUR 0,96 m² + odstępy i dojazd na polu odkładczym


class Pool:
    """Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).
    ponytail: przerwa rozłożona — czas zadania × długość / (długość − przerwa); osobny blok przerwy, gdy
    animacja ma pokazać pustą halę w południe."""

    def __init__(self, shifts):
        self.w = []
        for s in shifts:
            a, b = span(s)
            stretch = (b - a) / max(1e-6, b - a - s["break_min"] / 60)
            for _ in range(s["people"]):
                self.w.append([a, a, b, stretch])                   # [wolny od, od, do, rozciągnięcie]
        self.busy, self.waits, self.prod = [], [], 0.0

    def take(self, release, dur, k=1):
        cand = sorted(((max(release, w[0], w[1]), w) for w in self.w if max(release, w[0], w[1]) < w[2]),
                      key=lambda c: c[0])[:k]
        if len(cand) < k:
            return None
        start = cand[-1][0]
        end = start + dur * max(w[3] for _, w in cand)
        for _, w in cand:
            w[0] = end
        self.busy += [(start, end)] * k
        self.waits.append((release, start, dur))
        return start, end

    def available(self):
        return [(w[1], w[2]) for w in self.w]


class Fleet:
    def __init__(self, units, battery_h, charge_h):
        self.u = [[0.0, 0.0] for _ in range(max(1, units))]       # [wolny od, praca od ładowania]
        self.battery, self.charge = battery_h, charge_h
        self.busy, self.waits, self.charging = [], [], []

    def take(self, release, dur):
        u = min(self.u, key=lambda x: max(release, x[0]))
        start = max(release, u[0])
        u[0], u[1] = start + dur, u[1] + dur
        if u[1] >= self.battery:
            self.charging.append((u[0], u[0] + self.charge))
            u[0], u[1] = u[0] + self.charge, 0.0
        self.busy.append((start, start + dur))
        self.waits.append((release, start, dur))
        return start, start + dur


class Docks:
    def __init__(self, docks):
        self.free = {d["id"]: 0.0 for d in docks}
        self.busy = {d["id"]: [] for d in docks}

    def take(self, ids, release, dur):
        did = min(ids, key=lambda i: (max(release, self.free[i]), str(i)))
        start = max(release, self.free[did])
        self.free[did] = start + dur
        self.busy[did].append((start, start + dur))
        return did, start


def simulate_plan(plan, params, shifts, places):
    """plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h, end_h, break_min, people}];
    places: `places.places_from_features`. Zwraca surowe zapisy przebiegu (do `report`)."""
    pools = {p: Pool([s for s in shifts if s["process"] == p]) for p in
             ("unload", "palletize", "inspect", "pick", "pack", "load", "returns")}
    fleet = Fleet(params["fleet_units"], params["battery_h"], params["charge_h"])
    docks = Docks(places["docks"])
    role = places["roles"]
    move_h = params["fleet_min_per_move"] / 60
    rec = {"trucks": [], "staging_in": [], "staging_out": [], "parcels": [], "events": [], "unfinished": {},
           "unfinished_last": {}}
    heap, seq = [], [0]

    def push(t, kind, data):
        seq[0] += 1
        heapq.heappush(heap, (t, seq[0], kind, data))

    def ev(t, obj, kind, what, place, n=None):
        rec["events"].append((round(t * 3600), obj, kind, what, place) + ((n,) if n is not None else ()))

    def lost(proc):
        """Zadanie bez obsady do końca dnia (po ostatniej zmianie procesu)."""
        rec["unfinished"][proc] = rec["unfinished"].get(proc, 0) + 1
        rec["unfinished_last"][proc] = max(rec["unfinished_last"].get(proc, 0.0), t)

    for v in plan["out"]:
        v["remaining"] = v["pallets"]
        v["ready"] = v["arrive"]
        if v["kind"] == "courier":
            push(v["arrive"], "courier", v)
        elif v["pallets"] == 0:
            push(v["arrive"], "load", v)
        elif v["kind"] != "crossdock":
            for k in range(v["pallets"]):
                push(v["prepare_from"], "retrieve", (v, k, k < v["picked"]))
    xdock_to = {}
    for v in plan["out"]:
        for vid, k in v.get("xdock", []):
            xdock_to[(vid, k)] = v
    for v in plan["in"]:
        push(v["arrive"], "unload", v)
    for o in plan["orders"]:
        push(o["release"], "pick", o)
    for r in plan["returns"]:
        push(r["release"], "return", r)

    n = params
    while heap:
        t, _, kind, d = heapq.heappop(heap)
        if kind == "unload":
            v = d
            cont = v["kind"] == "container40"
            hours = (v["pallets"] * n["cartons_per_pallet"] / (n["container_cartons_per_h"] * n["container_people"])
                     if cont else v["pallets"] * n["truck_min_per_pallet"] / 60)
            ids = role["in_container"] if cont else role["in_pallet"]
            did, dock_free = docks.take(ids, t, 0.0)
            got = pools["unload"].take(dock_free, hours, n["container_people"] if cont else 1)
            if got is None:
                lost("unload")
                continue
            start, end = got
            docks.free[did] = end
            docks.busy[did][-1] = (start, end)
            rec["trucks"].append({"id": v["id"], "side": "in_container" if cont else "in_pallet", "kind": v["kind"],
                                  "arrive": t, "start": start, "end": end, "dock": did, "pallets": v["pallets"]})
            ev(t, v["id"], "container" if cont else "truck", "arrive", "gate")
            ev(start, v["id"], "container" if cont else "truck", "dock", f"dock:{did}")
            ev(end, v["id"], "container" if cont else "truck", "depart", f"dock:{did}")
            for k in range(v["pallets"]):
                emerge = start + (end - start) * (k + 0.5) / v["pallets"]
                key = (v["id"], k)
                pid = f"{v['id']}-p{k + 1}"
                if key in xdock_to:
                    x = xdock_to[key]
                    rec["staging_out"].append([emerge, None, pid, x["id"]])
                    ev(emerge, pid, "pallet", "staging", "staging_out")
                    push(emerge, "staged_out", (x, pid))
                elif cont:
                    push(emerge, "palletize", (v, pid, n["cartons_per_pallet"] / n["palletize_cartons_per_h"]))
                elif k >= round(v["pallets"] * v["mono_pct"] / 100):
                    push(emerge, "palletize", (v, pid, n["repack_min_per_pallet"] / 60))
                else:
                    push(emerge, "inspect", (v, pid))
        elif kind == "palletize":
            v, pid, hours = d
            got = pools["palletize"].take(t, hours)
            if got is None:
                lost("palletize")
                continue
            ev(got[1], pid, "pallet", "built", "palletize")
            push(got[1], "inspect", (v, pid))
        elif kind == "inspect":
            v, pid = d
            if zlib.crc32(pid.encode()) % 100 < v["inspect_pct"]:   # deterministycznie per paleta
                got = pools["inspect"].take(t, v["inspect_min"] / 60)
                if got is None:
                    lost("inspect")
                    continue
                t = got[1]
            rec["staging_in"].append([t, None, pid])
            ev(t, pid, "pallet", "staging", "staging_in")
            push(t, "putaway", (len(rec["staging_in"]) - 1, pid))
        elif kind == "putaway":
            i, pid = d
            start, end = fleet.take(t, move_h)
            rec["staging_in"][i][1] = start
            ev(start, pid, "pallet", "move", "staging_in")
            ev(end, pid, "pallet", "stored", "rack")
        elif kind == "retrieve":
            v, k, picked = d
            pid = f"{v['id']}-p{k + 1}"
            start, end = fleet.take(t, move_h)
            ev(end, pid, "pallet", "retrieved", "rack" if not picked else "pick")
            if picked:
                got = pools["load"].take(end, n["wrap_min_per_pallet"] / 60)
                if got is None:
                    lost("load")
                    continue
                end = got[1]
            rec["staging_out"].append([end, None, pid, v["id"]])
            ev(end, pid, "pallet", "staging", "staging_out")
            push(end, "staged_out", (v, pid))
        elif kind == "staged_out":
            v, _pid = d
            v["remaining"] -= 1
            v["ready"] = max(v["ready"], t)
            if v["remaining"] == 0:
                push(max(t, v["arrive"]), "load", v)
        elif kind == "load":
            v = d
            hours = v["pallets"] * n["load_min_per_pallet"] / 60
            did, dock_free = docks.take(role["out"], t, 0.0)
            got = pools["load"].take(dock_free, hours) if hours else (dock_free, dock_free)
            if got is None:
                lost("load")
                continue
            start, end = got
            docks.free[did] = end
            docks.busy[did][-1] = (start, end)
            for row in rec["staging_out"]:
                if row[3] == v["id"] and row[1] is None:
                    row[1] = start
                    ev(start, row[2], "pallet", "loaded", f"dock:{did}")
            rec["trucks"].append({"id": v["id"], "side": "out", "kind": v["kind"], "arrive": v["arrive"],
                                  "start": start, "end": end, "dock": did, "pallets": v["pallets"],
                                  "cutoff": v["cutoff"], "late_h": max(0.0, end - v["cutoff"])})
            ev(v["arrive"], v["id"], "truck", "arrive", "gate")
            ev(start, v["id"], "truck", "dock", f"dock:{did}")
            ev(end, v["id"], "truck", "depart", f"dock:{did}")
        elif kind == "courier":
            v = d
            did, start = docks.take(role["courier"], t, n["courier_dock_min"] / 60)
            v["pickup"] = start
            ev(t, v["id"], "courier", "arrive", "gate")
            ev(start, v["id"], "courier", "dock", f"dock:{did}")
            ev(start + n["courier_dock_min"] / 60, v["id"], "courier", "depart", f"dock:{did}")
        elif kind == "pick":
            o = d
            got = pools["pick"].take(t, o["lines"] / n["pick_lines_per_h"])
            if got is None:
                lost("pick")
                continue
            if o["parcels"]:
                push(got[1], "pack", o)
        elif kind == "pack":
            o = d
            hours = (o["parcels"] * (n["pack_min_per_parcel"] + n["label_min_per_parcel"])
                     + o["lines"] * n["pack_min_per_line"]) / 60
            got = pools["pack"].take(t, hours)
            if got is None:
                lost("pack")
                continue
            rec["parcels"].append({"order": o["id"], "n": o["parcels"], "ready": got[1], "courier": o["courier"]})
            ev(got[1], o["id"], "parcel", "packed", "pack", o["parcels"])
        elif kind == "return":
            r = d
            got = pools["returns"].take(t, n["return_min"] / 60)
            if got is None:
                lost("returns")
                continue
            if r["restock"]:
                fleet.take(got[1], move_h)

    couriers = {v["id"]: v for v in plan["out"] if v["kind"] == "courier"}
    for p in rec["parcels"]:
        c = couriers.get(p["courier"])
        p["cut"] = c.get("pickup", c["cutoff"]) if c else math.inf
        p["late"] = p["ready"] > p["cut"]
    rec.update(pools=pools, fleet=fleet, docks=docks, places=places)
    return rec
