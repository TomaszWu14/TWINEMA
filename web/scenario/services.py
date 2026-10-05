"""Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)."""
import time

from twin.shared import hall_feature_dict

from .models import ScenarioRun
from .sim import run_many
from .sim.places import places_from_features

MAX_RUNS = 30
KEEP_RUNS = 20                  # ostatnie symulacje na scenariusz; starsze (z dużym JSON zdarzeń) usuwamy


def simulate(day, wm, *, runs=12, user=None):
    sc = day.scenario
    places = places_from_features([hall_feature_dict(f) for f in wm.features.all()])
    t0 = time.perf_counter()
    res = run_many(day.sim_day(), sc.sim_params(), sc.shift_dicts(), places, sc.seed, runs=runs)
    run = ScenarioRun.objects.create(
        scenario=sc, day_kind=day.kind, model=wm, runs=runs, seed=sc.seed,
        duration_s=round(time.perf_counter() - t0, 2), events=res.pop("events"), result=res, created_by=user)
    old = ScenarioRun.objects.filter(scenario=sc).values_list("pk", flat=True)[KEEP_RUNS:]
    ScenarioRun.objects.filter(pk__in=list(old)).delete()
    return run
