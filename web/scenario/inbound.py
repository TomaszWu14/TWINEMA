"""Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez bazy).

Deterministyczne oszacowanie (symulacja zdarzeniowa = S3): przyjazdy rozłożone równomiernie w oknie
awizacji, dok zajęty przez czas rozładunku z norm wydajności. Liczymy dla poziomu „avg” (dzień
w średnich) i „max” (każda wartość na maksimum). Mnożnik wzrostu zwiększa liczbę przyjazdów — auto
33-paletowe dalej wiezie tyle palet, ile fizycznie się mieści.

stream: {kind, arrivals:(min,avg,max), pallets:(min,avg,max), window:(od_h, do_h),
         mono_pct, inspect_pct, inspect_min}
norms:  {container_cartons_per_h, container_people, cartons_per_pallet, truck_min_per_pallet,
         palletize_cartons_per_h, repack_min_per_pallet}
"""
import math

CONTAINER = "container40"
DOCK_OF = {CONTAINER: "container", "truck33": "pallet", "solo": "pallet", "crossdock": "pallet"}
LEVELS = {"avg": 1, "max": 2}


def _pick(triple, level):
    return triple[LEVELS[level]]


def arrivals_count(value, growth):
    """Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go nie ma)."""
    return math.ceil(value * growth - 1e-9) if value > 0 else 0


def unload_hours(stream, pallets, norms):
    if stream["kind"] == CONTAINER:
        cartons = pallets * norms["cartons_per_pallet"]
        return cartons / (norms["container_cartons_per_h"] * norms["container_people"])
    return pallets * norms["truck_min_per_pallet"] / 60


def starts(n, window):
    """n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków."""
    a, b = window
    return [a + (b - a) * (i + 0.5) / n for i in range(n)]


def peak_concurrency(intervals):
    """Maks. liczba jednoczesnych przedziałów [start, koniec) i moment szczytu."""
    events = sorted([(s, 1) for s, _ in intervals] + [(e, -1) for _, e in intervals],
                    key=lambda x: (x[0], x[1]))           # koniec przed startem w tej samej chwili
    cur = best = 0
    at = None
    for t, d in events:
        cur += d
        if cur > best:
            best, at = cur, t
    return best, at


def day_demand(streams, norms, *, growth=1.0, level="avg", shift_h=8.0):
    rows, docks = [], {"container": [], "pallet": []}
    ph = {"unload": 0.0, "palletize": 0.0, "repack": 0.0, "inspect": 0.0}
    pallets_in = cartons_in = xdock = 0.0
    for s in streams:
        n = arrivals_count(_pick(s["arrivals"], level), growth)
        p = _pick(s["pallets"], level)
        hours = unload_hours(s, p, norms)
        for t in starts(n, s["window"]) if n else []:
            docks[DOCK_OF[s["kind"]]].append((t, t + hours))
        pallets = n * p
        pallets_in += pallets
        if s["kind"] == "crossdock":            # z doku prosto na pole odkładcze wydań
            xdock += pallets
        if s["kind"] == CONTAINER:
            cartons = pallets * norms["cartons_per_pallet"]
            cartons_in += cartons
            ph["unload"] += cartons / norms["container_cartons_per_h"]
            ph["palletize"] += cartons / norms["palletize_cartons_per_h"]
        else:
            ph["unload"] += n * hours
            ph["repack"] += pallets * (1 - s["mono_pct"] / 100) * norms["repack_min_per_pallet"] / 60
        ph["inspect"] += pallets * s["inspect_pct"] / 100 * s["inspect_min"] / 60
        rows.append({"kind": s["kind"], "arrivals": n, "pallets_per": p, "pallets": round(pallets),
                     "unload_min": round(hours * 60)})
    peaks = {k: peak_concurrency(v) for k, v in docks.items()}
    ph = {k: round(v, 1) for k, v in ph.items()}
    ph["total"] = round(sum(ph.values()), 1)
    return {
        "level": level, "rows": rows, "pallets_in": round(pallets_in), "cartons_in": round(cartons_in),
        "pallets_xdock": round(xdock),
        "docks_peak": {k: v[0] for k, v in peaks.items()},
        "docks_peak_at": {k: _hhmm(v[1]) for k, v in peaks.items()},
        "person_hours": ph,
        # ponytail: stanowiska = osobogodziny / zmiana; rozkład w czasie dnia policzy symulacja S3
        "palletize_stations": math.ceil(ph["palletize"] / shift_h - 1e-9) if ph["palletize"] else 0,
    }


def _hhmm(h):
    if h is None:
        return ""
    m = round(h * 60)
    return f"{m // 60:02d}:{m % 60:02d}"
