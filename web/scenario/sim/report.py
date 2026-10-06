"""Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów (średnia / najgorszy) i wąskie
gardła z podpowiedziami (czysty Python). Podpowiedź „+N” wyznaczamy ponowną symulacją z tym samym ziarnem
(najmniejsze N, przy którym problem znika) — nie wzorem na oko."""
import math

from .engine import M2_PER_PALLET

STEP_H = 0.25
HORIZON_H = 26.0
NB = int(HORIZON_H / STEP_H)
PROCS = [("unload", "Rozładunek"), ("palletize", "Paletyzacja i przepakowanie"), ("inspect", "Kontrola"),
         ("pick", "Kompletacja"), ("pack", "Pakowanie i nadanie"), ("load", "Załadunek i owijanie"),
         ("returns", "Zwroty")]
SIDES = [("in_container", "Doki kontenerowe (IN)"), ("in_pallet", "Doki paletowe (IN)"), ("out", "Doki wydań (OUT)")]
# (klucz, etykieta, jednostka, co jest złe: "high" = dużo, "low" = mało)
KPI_SPEC = [
    ("pallets_in", "Palet przyjętych", "", "low"), ("pallets_out", "Palet wydanych", "", "low"),
    ("parcels", "Paczek spakowanych", "", "low"), ("parcels_late", "Paczek po odbiorze kuriera", "", "high"),
    ("trucks_out_late", "Aut OUT po cut-off", "", "high"), ("out_delay_max_min", "Max spóźnienie auta OUT", "min", "high"),
    ("wait_in_container_p95_min", "Czekanie kontenerów P95", "min", "high"),
    ("wait_in_pallet_p95_min", "Czekanie aut paletowych IN P95", "min", "high"),
    ("wait_out_p95_min", "Czekanie aut OUT P95", "min", "high"),
    ("queue_in_container_max", "Max kontenerów w kolejce", "", "high"),
    ("queue_in_pallet_max", "Max aut IN w kolejce", "", "high"), ("queue_out_max", "Max aut OUT w kolejce", "", "high"),
    ("staging_in_max", "Max palet na polu przyjęć", "", "high"), ("staging_out_max", "Max palet na polu wydań", "", "high"),
    ("fleet_util_pct", "Flota: wykorzystanie dnia", "%", "high"), ("fleet_peak_pct", "Flota: szczyt", "%", "high"),
    ("fleet_wait_p95_min", "Flota: czekanie zadań P95", "min", "high"), ("unfinished", "Zadań bez obsady", "", "high"),
    ("fleet_busy_h", "Flota: godzin pracy", "h", "high"),
    ("fleet_charge_h", "Flota: godzin ładowania", "h", "high"), ("fleet_effective", "Flota efektywna (bez ładowania)", "", "low"),
] + [(f"util_{p}", f"{lbl}: wykorzystanie", "%", "high") for p, lbl in PROCS] \
  + [(f"wait_{p}_p95_min", f"{lbl}: czekanie P95", "min", "high") for p, lbl in PROCS]


def p95(xs, q=0.95):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, max(0, math.ceil(q * len(xs)) - 1))] if xs else 0.0


def series(intervals, horizon_end=HORIZON_H):
    """Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min."""
    out = [0] * NB
    for s, e in intervals:
        e = horizon_end if e is None else e
        for i in range(max(0, math.ceil(s / STEP_H - 1e-9)), min(NB, math.ceil(e / STEP_H - 1e-9))):
            out[i] += 1
    return out


def hhmm(h):
    m = round(h * 60)
    return f"{m // 60:02d}:{m % 60:02d}"


def run_report(rec):
    """Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}."""
    pools, fleet = rec["pools"], rec["fleet"]
    trucks = rec["trucks"]
    kpi, tl = {}, {"t": [hhmm(i * STEP_H) for i in range(NB)]}
    for side, _ in SIDES:
        rows = [t for t in trucks if t["side"] == side]
        waits = [(t["start"] - t["arrive"]) * 60 for t in rows]
        kpi[f"wait_{side}_p95_min"] = round(p95(waits), 1)
        q = series([(t["arrive"], t["start"]) for t in rows if t["start"] > t["arrive"] + 1e-9])
        kpi[f"queue_{side}_max"] = max(q)
        tl[f"queue_{side}"] = q
        tl[f"docks_{side}"] = series([(t["start"], t["end"]) for t in rows])
    out = [t for t in trucks if t["side"] == "out"]
    kpi["pallets_in"] = sum(t["pallets"] for t in trucks if t["side"] != "out")
    kpi["pallets_out"] = sum(t["pallets"] for t in out)
    kpi["trucks_out_late"] = sum(t["late_h"] > 1e-9 for t in out)
    kpi["out_delay_max_min"] = round(max([t["late_h"] * 60 for t in out] or [0]))
    kpi["parcels"] = sum(p["n"] for p in rec["parcels"])
    kpi["parcels_late"] = sum(p["n"] for p in rec["parcels"] if p["late"])
    late_cuts = sorted(p["cut"] for p in rec["parcels"] if p["late"])
    kpi["late_cut_h"] = late_cuts[len(late_cuts) // 2] if late_cuts else None
    for side in ("in", "out"):
        s = series([(r[0], r[1]) for r in rec[f"staging_{side}"]])
        tl[f"staging_{side}"] = s
        kpi[f"staging_{side}_max"] = max(s)
    fb = series(fleet.busy)
    n_units = len(fleet.u)
    tl["fleet_busy"], tl["fleet_units"] = fb, n_units
    kpi["fleet_busy_h"] = round(sum(e - s for s, e in fleet.busy), 1)       # wózko-godziny pracy (koszty OPEX)
    kpi["fleet_util_pct"] = round(100 * kpi["fleet_busy_h"] / (n_units * 24))
    kpi["fleet_peak_pct"] = round(100 * max(fb) / n_units)
    kpi["fleet_wait_p95_min"] = round(p95([(s - r) * 60 for r, s, _ in fleet.waits]), 1)
    charge_h = sum(min(e, 24) - s for s, e in fleet.charging if s < 24)
    kpi["fleet_charge_h"] = round(charge_h, 1)
    kpi["fleet_effective"] = round(n_units - charge_h / 24, 1)      # średnio wózków dostępnych (nie na ładowaniu)
    kpi["fleet_groups"] = [{                                           # K3: per grupa floty (przebieg)
        "name": g["name"], "kind": g.get("kind", ""), "role": g["role"], "units": g["units"],
        "busy_h": round(sum(e - s for s, e in g["fleet"].busy), 1),
        "util_pct": round(100 * sum(e - s for s, e in g["fleet"].busy) / (max(1, g["units"]) * 24)),
        "wait_p95_min": round(p95([(s - r) * 60 for r, s, _ in g["fleet"].waits]), 1)} for g in getattr(fleet, "groups", [])]
    tl["people"] = {}
    for p, _ in PROCS:
        pool = pools[p]
        avail = sum(max(0.0, b - a) for a, b in pool.available())
        busy = sum(e - s for s, e in pool.busy)
        kpi[f"util_{p}"] = round(100 * busy / avail) if avail else 0
        kpi[f"wait_{p}_p95_min"] = round(p95([(s - r) * 60 for r, s, _ in pool.waits]), 1)
        kpi[f"wait_{p}_at"] = max(pool.waits, key=lambda w: w[1] - w[0])[0] if pool.waits else None
        tl["people"][p] = {"busy": series(pool.busy), "avail": series(pool.available())}
    kpi["unfinished"] = sum(rec["unfinished"].values())
    kpi["unfinished_by"] = dict(rec["unfinished"])
    kpi["unfinished_last"] = {k: round(v, 2) for k, v in rec["unfinished_last"].items()}
    return {"kpi": kpi, "timeline": tl}


def aggregate(kpis):
    """[kpi przebiegu] → {klucz: {mean, worst}}; najgorszy = P95 (gdy złe „dużo”) albo P5 (gdy złe „mało”)."""
    out = {}
    for key, label, unit, bad in KPI_SPEC:
        xs = [k[key] for k in kpis]
        out[key] = {"label": label, "unit": unit, "mean": round(sum(xs) / len(xs), 1),
                    "worst": p95(xs) if bad == "high" else p95(xs, 0.05)}
    return out


def window(series_, pred=lambda v: v > 0):
    idx = [i for i, v in enumerate(series_) if pred(v)]
    return f"{hhmm(idx[0] * STEP_H)}–{hhmm((idx[-1] + 1) * STEP_H)}" if idx else ""


def _smallest(fix, ok, limit):
    """Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga."""
    for k in range(1, limit + 1):
        if ok(fix(k)):
            return k
    return None


def bottlenecks(agg, rep, places, shifts, rerun):
    """Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze zmianą:
    ("docks", rola, k) · ("people", indeks zmiany, k) · ("fleet", k)."""
    out, tl = [], rep["timeline"]

    def add(sev, area, where, win, problem, suggestion):
        out.append({"severity": sev, "area": area, "where": where, "window": win, "problem": problem,
                    "suggestion": suggestion})

    def shift_at(proc, at):
        """Zmiana procesu obejmująca chwilę `at` (albo najbliższa), indeks w `shifts`."""
        own = [i for i, s in enumerate(shifts) if s["process"] == proc]
        if not own:
            return None
        at = 12.0 if at is None else at

        def key(j):
            a, b = shifts[j]["start_h"], shifts[j]["end_h"]
            return (not a <= at < (b if b > a else 24), abs(a - at))
        return min(own, key=key)

    for side, label in SIDES:
        w = agg[f"wait_{side}_p95_min"]["worst"]
        if w <= 20:
            continue
        q = agg[f"queue_{side}_max"]["worst"]
        i = shift_at("unload", rep["kpi"].get("wait_unload_at"))
        if side != "out" and max(tl[f"docks_{side}"]) < places["counts"][side] and i is not None:
            # doki nie były pełne naraz — auta czekają na ludzi do rozładunku, nie na dok
            k = _smallest(lambda k, i=i: rerun("people", i, k), lambda kp, s=side: kp[f"wait_{s}_p95_min"] <= 20, 6)
            s = shifts[i]
            add("error" if w > 60 else "warning", label, label.split(" (")[0].lower(), window(tl[f"queue_{side}"]),
                f"Kolejka do {q} aut, czekanie P95 {w:g} min — doki wolne, brakuje ludzi do rozładunku.",
                f"+{k} os. na rozładunku {hhmm(s['start_h'])}–{hhmm(s['end_h'])}." if k
                else "Nawet +6 os. nie wystarcza — rozłóż przyjazdy w oknach awizacji.")
            continue
        k = _smallest(lambda k, s=side: rerun("docks", s, k), lambda kp, s=side: kp[f"wait_{s}_p95_min"] <= 20, 5)
        if k:
            add("error" if w > 60 else "warning", label, label.split(" (")[0].lower(), window(tl[f"queue_{side}"]),
                f"Kolejka do {q} aut, czekanie P95 {w:g} min (dostępne doki: {places['counts'][side]}).",
                f"+{k} {'dok' if k == 1 else 'doki' if k < 5 else 'doków'} tej roli skraca czekanie P95 do ≤ 20 min.")
        elif side == "out":
            add("warning", label, "przygotowanie palet OUT", window(tl[f"queue_{side}"]),
                f"Auta OUT czekają P95 {w:g} min — dodatkowe doki nie pomagają (brakuje gotowych palet).",
                "Sprawdź flotę i załadunek/owijanie poniżej — to one wstrzymują auta.")
    for side, lbl in (("in", "przyjęć"), ("out", "wydań")):
        mx = agg[f"staging_{side}_max"]["worst"]
        need, drawn = mx * M2_PER_PALLET, places["staging_m2"][side]
        if need > drawn + 1:
            peak = max(tl[f"staging_{side}"])
            add("warning" if drawn else "error", f"Pole odkładcze {lbl}", f"pole odkładcze {lbl}",
                window(tl[f"staging_{side}"], lambda v, m=peak: v >= 0.8 * m),
                f"Do {mx:g} palet naraz → potrzeba ~{need:.0f} m², narysowane {drawn:.0f} m².",
                f"+{math.ceil(need - drawn)} m² pola odkładczego {lbl} (w edytorze layoutu).")
    late, parcels = agg["parcels_late"]["worst"], max(1, agg["parcels"]["mean"])
    pack_idx = [i for i, s in enumerate(shifts) if s["process"] == "pack"]
    if late > 0.01 * parcels and pack_idx:
        cut = rep["kpi"].get("late_cut_h") or 18.0          # odbiór, na który paczki nie zdążają
        i = min(pack_idx, key=lambda j: (not shifts[j]["start_h"] <= cut - 0.5 < shifts[j]["end_h"],
                                         -shifts[j]["start_h"]))
        k = _smallest(lambda k: rerun("people", i, k), lambda kp: kp["parcels_late"] <= 0.01 * kp["parcels"], 8)
        s = shifts[i]
        add("error", "Pakowanie i nadanie", "stanowiska pakowania", f"{hhmm(s['start_h'])}–{hhmm(s['end_h'])}",
            f"{late:g} paczek nie zdąży na odbiór kuriera (najgorszy przebieg).",
            f"+{k} os. na zmianie {hhmm(s['start_h'])}–{hhmm(s['end_h'])} (pakowanie)." if k
            else "Nawet +8 os. nie wystarcza — przesuń odbiór kuriera albo dodaj zmianę.")
    fw, fp = agg["fleet_wait_p95_min"]["worst"], agg["fleet_peak_pct"]["worst"]
    if fw > 30:
        # K3: dokładamy do grupy, na którą zadania czekają najdłużej (flota mieszana); jedna flota — do niej
        groups = rep["kpi"].get("fleet_groups") or []
        gi = max(range(len(groups)), key=lambda i: groups[i]["wait_p95_min"]) if groups else 0
        who = f" ({groups[gi]['name']})" if len(groups) > 1 else ""
        k = _smallest(lambda k: rerun("fleet", k, gi), lambda kp: kp["fleet_wait_p95_min"] <= 30, 6)
        add("error" if fw > 90 else "warning", "Flota wózków", f"wózki / AGV{who}",
            window(tl["fleet_busy"], lambda v: v >= tl["fleet_units"]),
            f"Zadania czekają na wózek P95 {fw:g} min, szczyt wykorzystania {fp:g} %, "
            f"ładowanie zabiera {agg['fleet_charge_h']['mean']:g} h wózko-godzin dziennie.",
            f"+{k} {'wózek' if k == 1 else 'wózki' if k < 5 else 'wózków'}{who}." if k
            else "Nawet +6 wózków nie wystarcza — sprawdź normę czasu ruchu i ładowanie.")
    for p, label in PROCS:
        if p == "pack":
            continue
        w, lost = agg[f"wait_{p}_p95_min"]["worst"], rep["kpi"]["unfinished_by"].get(p, 0)
        own = [i for i, s in enumerate(shifts) if s["process"] == p]
        if w <= 60 and not lost:
            continue
        if lost and (not own or w <= 60):
            # zadania przychodzą po ostatniej zmianie procesu — brakuje godzin, nie ludzi
            last = rep["kpi"]["unfinished_last"].get(p, 0.0)
            end = max((s["end_h"] if s["end_h"] > s["start_h"] else s["end_h"] + 24 for s in
                       (shifts[i] for i in own)), default=None)
            add("error", label, label.lower(), f"{hhmm(end)}–{hhmm(last + 0.25)}" if end is not None else "",
                f"{lost} zadań bez obsady — przychodzą po końcu ostatniej zmiany" if own
                else f"{lost} zadań, a proces nie ma żadnej zmiany.",
                f"Dodaj zmianę od {hhmm(end)} do ok. {hhmm(math.ceil((last + 0.5) * 2) / 2)}." if own
                else "Dodaj zmianę z obsadą w scenariuszu.")
            continue
        i = shift_at(p, rep["kpi"].get(f"wait_{p}_at"))
        k = _smallest(lambda k, i=i: rerun("people", i, k),
                      lambda kp, p=p: kp[f"wait_{p}_p95_min"] <= 60 and not kp["unfinished_by"].get(p), 6)
        s = shifts[i]
        add("warning" if w < 180 and not lost else "error", label, label.lower(),
            f"{hhmm(s['start_h'])}–{hhmm(s['end_h'])}",
            f"Zadania czekają P95 {w:g} min" + (f", {lost} bez obsady do końca dnia." if lost else "."),
            f"+{k} os. na zmianie {hhmm(s['start_h'])}–{hhmm(s['end_h'])}." if k
            else "Nawet +6 os. nie wystarcza — dodaj zmianę albo popraw normę.")
    if agg["trucks_out_late"]["worst"] and not any(b["area"].startswith(("Doki wydań", "Flota", "Załadunek"))
                                                   for b in out):
        add("warning", "Wydania", "auta OUT", "", f"{agg['trucks_out_late']['worst']:g} aut odjeżdża po cut-off "
            f"(do {agg['out_delay_max_min']['worst']:g} min).", "Wcześniejsze okno przygotowania palet albo więcej osób na załadunku.")
    return out
