"""Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)."""
import time

from equipment.catalog import move_minutes
from equipment.models import CostRate
from masterdata.packaging import weighted_cartons_per_pallet
from masterdata.services import cartons_per_pallet_distribution as cartons_distribution
from masterdata.services import stock_profile
from twin.blender_scene import model_floor, model_racks
from twin.design_kpi import rack_to_element, travel_stats
from twin.layout import feature_row, rack_row
from twin.shared import hall_feature_dict

from . import costs
from .models import ScenarioRun
from .placement import check_placement
from .sim import run_many
from .sim.places import needed_roles, places_from_features

MAX_RUNS = 30
KEEP_RUNS = 20                  # ostatnie symulacje na scenariusz; starsze (z dużym JSON zdarzeń) usuwamy


def simulate(day, wm, *, runs=12, user=None):
    sc = day.scenario
    sim_day = day.sim_day()
    places = places_from_features([hall_feature_dict(f) for f in wm.features.all()], needed_roles(sim_day))
    t0 = time.perf_counter()
    params, cpp = sc.sim_params(), cartons_distribution()
    if cpp:
        # kartonów/paletę z master daty (rozkład po stanie) zastępuje średnią normę scenariusza
        params.update(cpp_dist=cpp[0], cartons_per_pallet=weighted_cartons_per_pallet(cpp[0]))
    fleet = fleet_from_catalog(sc.fleet_equipment, wm) if sc.fleet_equipment_id else None
    if fleet:
        params.update(fleet_min_per_move=fleet["min_per_move"], battery_h=fleet["battery_h"], charge_h=fleet["charge_h"])
    res = run_many(sim_day, params, sc.shift_dicts(), places, sc.seed, runs=runs)
    res["fleet"] = fleet
    res["cpp"] = {"value": params["cartons_per_pallet"], "source": f"master data ({cpp[2]})" if cpp else "norma"}
    res["placement"] = placement_for(wm, sc.growth)
    res["bottlenecks"] = placement_bottlenecks(res["placement"]) + res["bottlenecks"]
    run = ScenarioRun.objects.create(
        scenario=sc, day_kind=day.kind, model=wm, runs=runs, seed=sc.seed,
        duration_s=round(time.perf_counter() - t0, 2), events=res.pop("events"), result=res, created_by=user)
    old = ScenarioRun.objects.filter(scenario=sc).values_list("pk", flat=True)[KEEP_RUNS:]
    ScenarioRun.objects.filter(pk__in=list(old)).delete()
    return run


def fleet_from_catalog(eq, wm):
    """Sprzęt floty z katalogu (K1) → czas ruchu palety na tym layoucie: średnia droga od punktów obsługi
    (doki, stanowiska) do miejsc paletowych (`travel_stats`) tam i z powrotem + podniesienie na średnią wysokość
    belki + pobranie/odłożenie; bateria i ładowanie z katalogu. Półki (kompletacja ręczna) pomijamy."""
    racks = [r for r in model_racks(wm) if (r.get("equipment") or "reach") != "shelf"]
    p = eq.params()
    if not racks:
        dist, lift = 0.0, 0.0
    else:
        floor = model_floor(wm, racks)
        tr = travel_stats([rack_to_element(r) for r in racks], [hall_feature_dict(f) for f in wm.features.all()],
                          floor["width"], floor["depth"])
        w = [r["n_bays"] * r["n_levels"] for r in racks]
        dist = tr["avg_m"] or 0.0
        lift = sum((r["n_levels"] - 1) / 2 * r["level_h"] * k for r, k in zip(racks, w, strict=True)) / sum(w)
    return {"name": eq.name, "dist_m": round(dist, 1), "lift_m": round(lift, 2),
            "min_per_move": round(move_minutes(p, dist, lift), 2),
            "battery_h": p["battery_h"] or 8.0, "charge_h": p["charge_h"] or 1.5}


def placement_for(wm, growth):
    """Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie (`placement`)."""
    return check_placement([rack_row(r) for r in wm.racks.order_by("pk")],
                           [feature_row(f) for f in wm.features.order_by("pk")], stock_profile(), growth)


FIX = {"capacity": "dołóż regały / poziomy w edytorze albo zmniejsz zapas (mnożnik, dni zapasu)",
       "zone": "powiększ strefę w edytorze albo przesuń do niej regały",
       "load": "podnieś nośność belek w części regałów (pole „nośność” regału) albo obniż palety",
       "heavy": "zarezerwuj dolne poziomy na ciężkie palety albo dodaj regały niskie"}


def placement_bottlenecks(pl):
    """Problemy pojemności/rozmieszczenia w formacie wąskich gardeł symulacji (na górze listy)."""
    def fix(code):
        return FIX["capacity" if code.startswith("capacity") else "load" if code == "load_over"
                   else "heavy" if code == "heavy_high" else "zone"]
    return [{"severity": i["severity"], "area": "Pojemność i rozmieszczenie", "where": "", "window": "",
             "problem": i["message"], "suggestion": fix(i["code"])} for i in pl["issues"]]


def _shift_hours(sh):
    length = sh["end_h"] - sh["start_h"] + (24 if sh["end_h"] <= sh["start_h"] else 0)
    return max(0.0, length - sh["break_min"] / 60) * sh["people"]


def run_costs(run, rates=None):
    """Koszty wyniku symulacji (C1) — liczone przy wyświetleniu, więc zmiana stawek działa od razu.
    Layout = aktualny stan modelu hali (jak pojemność w `placement_for`)."""
    rates = rates or CostRate.as_dict()
    sc, wm, agg = run.scenario, run.model, run.result["agg"]
    positions = {"reach": 0, "vna": 0, "shelf": 0}
    for r in model_racks(wm):
        p = rack_to_element(r)["params"]
        positions[r.get("equipment") or "reach"] += p["bays"] * p["levels"] * p["pallets_per_bay"]
    kinds = list(wm.features.values_list("kind", flat=True))
    eq = sc.fleet_equipment
    fleet = {"name": eq.name if eq else "wózki", "units": sc.fleet_units,
             "purchase": eq.cost_range("cost_purchase", "cost_purchase_max") if eq else None,
             "hour": eq.cost_range("cost_per_hour", "cost_per_hour_max") if eq else None}
    day = sc.days.filter(kind=run.day_kind).first()
    return costs.compute(
        rates, {"positions": positions, "docks": kinds.count("dock"), "stations": kinds.count("station"),
                "area_m2": wm.floor_width_m * wm.floor_depth_m},
        fleet, sum(_shift_hours(s) for s in sc.shift_dicts()),
        agg["fleet_util_pct"]["mean"] / 100 * sc.fleet_units * 24, sc.work_days,
        {"pallets": agg["pallets_in"]["mean"] + agg["pallets_out"]["mean"], "parcels": agg["parcels"]["mean"],
         "orders": (day.orders_avg * sc.growth) if day else 0})
