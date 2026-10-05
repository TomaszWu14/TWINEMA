"""Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład w oknach.

Liczby z planu losujemy rozkładem trójkątnym (min, max, moda = średnia), z ziarnem — ta sama
wartość ziarna daje ten sam dzień. Przyjazdy i wyjazdy: n aut równo w oknie (środki n odcinków)
z rozrzutem ±40 % odcinka — tak wygląda dzień na awizacjach. Wzrost: więcej aut / zamówień / paczek.
"""
import random

JITTER = 0.4                    # rozrzut przyjazdu: ± tyle długości odcinka okna
LEAD_H = 2.0                    # palety OUT zaczynamy przygotowywać tyle przed przyjazdem auta


def tri(rng, triple):
    lo, mid, hi = triple
    return lo if hi <= lo else rng.triangular(lo, hi, min(max(mid, lo), hi))


def count(rng, triple, growth=1.0):
    return max(0, round(tri(rng, triple) * growth))


def times_in_window(rng, n, window):
    """n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane."""
    a, b = window
    step = (b - a) / n if n else 0
    return sorted(min(b, max(a, a + step * (i + 0.5) + rng.uniform(-JITTER, JITTER) * step)) for i in range(n))


def build_plan(day, params, seed):
    """day: {inbound:[stream], outbound:[stream], profile:{orders,lines,parcels,returns,full_pallet_pct}}
    (formaty jak `inbound.day_demand` / `outbound.day_outbound`). Zwraca listy aut, zamówień, zwrotów."""
    rng = random.Random(seed)
    g = params.get("growth", 1.0)
    vehicles_in, vehicles_out = [], []
    for s in day["inbound"]:
        n = count(rng, s["arrivals"], g)
        for t in times_in_window(rng, n, s["window"]):
            vehicles_in.append({"id": f"in{len(vehicles_in) + 1}", "kind": s["kind"], "arrive": t,
                                "pallets": max(0, round(tri(rng, s["pallets"]))), "mono_pct": s["mono_pct"],
                                "inspect_pct": s["inspect_pct"], "inspect_min": s["inspect_min"]})
    for s in day["outbound"]:
        n = count(rng, s["departures"], g)
        # auto podjeżdża tak, żeby średni załadunek (+15 min) skończył się przed cut-off
        a, b = s["window"]
        load_h = (params["courier_dock_min"] / 60 if s["kind"] == "courier"
                  else s["pallets"][1] * params["load_min_per_pallet"] / 60) + 0.25
        for t in times_in_window(rng, n, (a, max(a, b - load_h))):
            vehicles_out.append({"id": f"out{len(vehicles_out) + 1}", "kind": s["kind"], "arrive": t,
                                 "cutoff": s["window"][1],
                                 "pallets": 0 if s["kind"] == "courier" else max(0, round(tri(rng, s["pallets"])))})
    vehicles_in.sort(key=lambda v: v["arrive"])
    vehicles_out.sort(key=lambda v: v["arrive"])
    prof = day["profile"]
    n_orders = count(rng, prof["orders"], g)
    n_parcels = count(rng, prof["parcels"], g)
    couriers = [v for v in vehicles_out if v["kind"] == "courier"]
    last_cut = max((v["cutoff"] for v in couriers), default=18.0)
    orders = []
    for i, t in enumerate(sorted(rng.uniform(5.0, max(5.5, last_cut - 1.5)) for _ in range(n_orders))):
        # paczki jadą pierwszym kurierem, który przyjeżdża ≥ 1 h po wpłynięciu zamówienia
        c = next((v for v in couriers if v["arrive"] >= t + 1.0), couriers[-1] if couriers else None)
        orders.append({"id": f"o{i + 1}", "release": t, "lines": max(1, round(tri(rng, prof["lines"]))),
                       "parcels": n_parcels // n_orders + (1 if i < n_parcels % n_orders else 0) if n_orders else 0,
                       "courier": c["id"] if c else None})
    returns = [{"id": f"r{i + 1}", "release": t, "restock": rng.random() * 100 < params["return_restock_pct"]}
               for i, t in enumerate(times_in_window(rng, count(rng, prof["returns"], g),
                                                     params.get("returns_window", (7.0, 14.0))))]
    # cross-dock: palety z aut IN cross-dock przydzielone po kolei do aut OUT cross-dock
    xin = [v for v in vehicles_in if v["kind"] == "crossdock"]
    xout = [v for v in vehicles_out if v["kind"] == "crossdock"]
    pool = [(v["id"], k) for v in xin for k in range(v["pallets"])]
    for v in xout:
        take, pool = pool[:v["pallets"]], pool[v["pallets"]:]
        v["xdock"], v["pallets"] = take, len(take)
    full_pct = prof["full_pallet_pct"]
    for v in vehicles_out:
        if v["kind"] in ("courier", "crossdock"):
            continue
        v["picked"] = sum(rng.random() * 100 >= full_pct for _ in range(v["pallets"]))
        v["prepare_from"] = max(0.0, v["arrive"] - LEAD_H)
    return {"in": vehicles_in, "out": vehicles_out, "orders": orders, "returns": returns,
            "xdock_spare": [vid for vid, _ in pool]}
