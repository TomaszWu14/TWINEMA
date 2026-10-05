"""Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)."""
import time

from masterdata.packaging import weighted_cartons_per_pallet
from masterdata.services import cartons_per_pallet_distribution as cartons_distribution
from masterdata.services import stock_profile
from twin.layout import feature_row, rack_row
from twin.shared import hall_feature_dict

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
    res = run_many(sim_day, params, sc.shift_dicts(), places, sc.seed, runs=runs)
    res["cpp"] = {"value": params["cartons_per_pallet"], "source": f"master data ({cpp[2]})" if cpp else "norma"}
    res["placement"] = placement_for(wm, sc.growth)
    res["bottlenecks"] = placement_bottlenecks(res["placement"]) + res["bottlenecks"]
    run = ScenarioRun.objects.create(
        scenario=sc, day_kind=day.kind, model=wm, runs=runs, seed=sc.seed,
        duration_s=round(time.perf_counter() - t0, 2), events=res.pop("events"), result=res, created_by=user)
    old = ScenarioRun.objects.filter(scenario=sc).values_list("pk", flat=True)[KEEP_RUNS:]
    ScenarioRun.objects.filter(pk__in=list(old)).delete()
    return run


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
