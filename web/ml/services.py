"""Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły forecast/segmentation → ModelRun."""
import statistics
from datetime import date

from twin.blender_stock import abc_by_hits
from twin.design_day import STREAMS, XYZ_CUTS, load_inputs, working_days
from twin.design_forecast import weekly

from . import forecast, segmentation
from .models import ModelRun

STREAM_LABELS = {k: v for k, v in STREAMS if k != "orders"}


def run_forecast(batch, stream="total", years=5, user=None):
    inputs = load_inputs(batch)
    series = [(date.fromordinal(w).isoformat(), v) for w, v in weekly(inputs["daily"], stream)]
    res = forecast.run(series, years=years)
    metrics = ({"mape": res["ranking"][0]["mape"], "baseline_mape": res["baseline_mape"],
                "growth_p50_pct": res["growth_p50_pct"], "weeks": res["weeks"]} if res["ok"] else {})
    return ModelRun.objects.create(kind="forecast", batch=batch, version=forecast.VERSION,
                                   params={"stream": stream, "years": years}, metrics=metrics, result=res,
                                   created_by=_user(user))


def run_segmentation(batch, k=4, user=None):
    from masterdata.models import Material

    inputs = load_inputs(batch)
    days = working_days(inputs["daily"])
    md = inputs["material_days"]
    volumes = {m: round(l * w * h / 1000, 2) for m, l, w, h in
               Material.objects.filter(code__in=list(md)).exclude(carton_l_cm=None)
               .values_list("code", "carton_l_cm", "carton_w_cm", "carton_h_cm") if w and h}
    day_set = set(days)
    hits = {m: sum(n for d, n in pd.items() if d in day_set) for m, pd in md.items()}
    hits = {m: n for m, n in hits.items() if n}
    abc = abc_by_hits(hits)
    xyz = {}
    for m in hits:
        series = [md[m].get(d, 0) for d in days]
        mean = statistics.fmean(series)
        cv = statistics.pstdev(series) / mean if mean else 0.0
        xyz[m] = "X" if cv < XYZ_CUTS[0] else ("Y" if cv < XYZ_CUTS[1] else "Z")
    # objętość wchodzi jako cecha tylko, gdy znamy ją dla każdego materiału (pilnuje segment())
    res = segmentation.segment(md, days, volumes=volumes, k=k, abc=abc, xyz=xyz)
    metrics = {"skus": res["skus"], "inertia": res["inertia"], "k": k} if res["ok"] else {}
    return ModelRun.objects.create(kind="segmentation", batch=batch, version=segmentation.VERSION,
                                   params={"k": k}, metrics=metrics, result=res, created_by=_user(user))


def _user(user):
    return user if user is not None and user.is_authenticated else None
