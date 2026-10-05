# Porównanie wariantów hali na dniu projektowym (plan 2026-10-02, etap 7): pojemność + flota
# dobrana symulacją + droga, czekanie, zadania po 21:00 — obok siebie, najlepsza wartość wyróżniona.


from django.core.cache import cache

from core.roles import GROUP_ADMIN, GROUP_DESIGNER, has_role
from twin.shared import _planner, cache_digest, get_object_or_404, hall_feature_dict, render, WarehouseModel
from twin.blender_scene import model_floor, model_racks
from twin.design_compare import capacity, comparison, required_fleet, variant_row
from twin.design_day import PERCENTILES
from twin.design_sim import load_day_tasks
from twin.models_tasks import WarehouseTaskBatch
from twin.views.warehouse_design_day import CACHE_TTL
from twin.views.warehouse_design_sim import design_day, sim_params

__all__ = ["ewm_tasks_compare"]

MAX_VARIANTS = 4


@_planner
def ewm_tasks_compare(request, pk):
    batch = get_object_or_404(WarehouseTaskBatch, pk=pk, status="done")
    prm = sim_params(request.GET)
    models = list(WarehouseModel.objects.order_by("-created_at")[:50])
    ids = [int(x) for x in request.GET.getlist("models") if x.isdigit()][:MAX_VARIANTS]
    chosen = [m for i in dict.fromkeys(ids) for m in models if m.pk == i]
    day = design_day(batch, prm["p"])
    # Kilka symulacji dnia na wariant — liczy tylko Projektant, wynik w cache; Podgląd widzi tylko policzone.
    may_compute = has_role(request.user, GROUP_ADMIN, GROUP_DESIGNER)
    rows, skipped, missing, tasks = [], [], [], None
    if day and chosen:
        for wm in chosen:
            key = "cmp:" + cache_digest(batch.pk, wm.pk, wm.updated_at.timestamp(), day, prm)
            hit = cache.get(key)
            if hit is None and may_compute:
                if tasks is None:
                    tasks = load_day_tasks(batch, day)
                racks = model_racks(wm)
                features = [hall_feature_dict(f) for f in wm.features.all()]
                result, fleet = required_fleet(tasks, racks, features, dict(prm["fleet"]),
                                               multiplier=prm["mult"], calib=prm["calib"])
                hit = (variant_row(capacity(racks, features, model_floor(wm, racks)), result, fleet), result is None)
                cache.set(key, hit, CACHE_TTL)
            if hit is None:
                missing.append(wm)
                continue
            rows.append(hit[0])
            if hit[1]:
                skipped.append(wm.name)
        chosen = [m for m in chosen if m not in missing]
    return render(request, "twin/ewm_tasks/compare.html", {
        "missing": [m.name for m in missing],
        "batch": batch, "p": prm["p"], "percentiles": PERCENTILES, "mult": prm["mult"], "calib": prm["calib"],
        "models": models, "chosen": chosen, "chosen_ids": {m.pk for m in chosen}, "day": day,
        "table": comparison(rows) if rows else [], "skipped": skipped, "max_variants": MAX_VARIANTS,
    })
