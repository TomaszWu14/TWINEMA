# API edytora layoutu (E1): odczyt planu hali, sprawdzenie bez zapisu (KPI + problemy) i zapis całości
# w jednej transakcji z blokadą optymistyczną po `version` (= updated_at modelu). Logika w twin/layout.py.
import json

from django.urls import reverse
from django.utils import timezone

from twin.design_catalog import ELEMENTS
from twin.layout import RACK_LIMITS, LayoutError, analyze, clean_layout, feature_row, rack_row
from twin.shared import (
    _md_role, _planner, get_object_or_404, HALL_FEATURE_COLORS, hall_feature_kinds, JsonResponse, render,
    require_POST, transaction, WarehouseHallFeature, WarehouseModel, WarehouseModelRack,
)

MAX_BODY = 2 * 1024 * 1024
RACK_FIELDS = ("zone", "rack_id", "n_bays", "n_levels", "bay_width_cm", "depth_cm", "level_height_cm")


def _version(wm):
    return wm.updated_at.isoformat()


def _layout(wm):
    return {"floor": {"width": wm.floor_width_m, "depth": wm.floor_depth_m},
            "racks": [rack_row(r) for r in wm.racks.order_by("zone", "rack_id")],
            "features": [feature_row(f) for f in wm.features.order_by("pk")],
            "version": _version(wm), "feature_kinds": hall_feature_kinds()}


def _parse(request):
    """→ (layout, None) albo (None, odpowiedź błędu)."""
    if len(request.body) > MAX_BODY:
        return None, JsonResponse({"error": "Za duży plan (maks. 2 MB)."}, status=413)
    try:
        return clean_layout(json.loads(request.body), hall_feature_kinds()), None
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None, JsonResponse({"error": "To nie jest poprawny JSON."}, status=400)
    except LayoutError as exc:
        return None, JsonResponse({"error": str(exc)}, status=400)


@_md_role
def warehouse_layout_editor(request, pk):
    """Edytor planu hali (E2): dane przez uklad.json, sprawdzanie i zapis przez API powyżej."""
    wm = get_object_or_404(WarehouseModel, pk=pk)
    config = {
        "urls": {"layout": reverse("twin:warehouse_layout_json", args=[pk]),
                 "check": reverse("twin:warehouse_layout_check", args=[pk]),
                 "save": reverse("twin:warehouse_layout_save", args=[pk])},
        "limits": RACK_LIMITS, "featureColors": HALL_FEATURE_COLORS,
        "aisle": ELEMENTS["rack_std"]["aisle_m"],
    }
    return render(request, "twin/warehouse_model/editor.html", {"wm": wm, "config": config})


@_planner
def warehouse_layout_json(request, pk):
    return JsonResponse(_layout(get_object_or_404(WarehouseModel, pk=pk)), json_dumps_params={"ensure_ascii": False})


@require_POST
@_md_role
def warehouse_layout_check(request, pk):
    get_object_or_404(WarehouseModel, pk=pk)
    layout, err = _parse(request)
    if err:
        return err
    kpi, issues = analyze(layout)
    return JsonResponse({"kpi": kpi, "issues": issues}, json_dumps_params={"ensure_ascii": False})


@require_POST
@_md_role
def warehouse_layout_save(request, pk):
    layout, err = _parse(request)
    if err:
        return err
    kpi, issues = analyze(layout)
    if any(i["severity"] == "error" for i in issues):
        return JsonResponse({"error": "Plan ma błędy — popraw je przed zapisem.", "issues": issues}, status=422)
    with transaction.atomic():
        wm = get_object_or_404(WarehouseModel.objects.select_for_update(), pk=pk)
        if layout["version"] != _version(wm):
            return JsonResponse({"error": "Ktoś zmienił ten model w międzyczasie. Wczytaj plan ponownie "
                                          "(Twoje zmiany nie zostały zapisane)."}, status=409)
        racks = {r.pk: r for r in wm.racks.all()}
        feats = {f.pk: f for f in wm.features.all()}
        wanted_r = {r["id"] for r in layout["racks"] if r["id"]}
        wanted_f = {f["id"] for f in layout["features"] if f["id"]}
        if not wanted_r <= racks.keys() or not wanted_f <= feats.keys():
            return JsonResponse({"error": "Plan zawiera elementy spoza tego modelu. Wczytaj plan ponownie."},
                                status=409)
        WarehouseModelRack.objects.filter(pk__in=racks.keys() - wanted_r).delete()
        WarehouseHallFeature.objects.filter(pk__in=feats.keys() - wanted_f).delete()
        # Przeniesienie/zamiana adresów (strefa, numer) — najpierw tymczasowe numery, żeby
        # unikalność (model, strefa, regał) nie pękła w połowie zapisu.
        moved = [r["id"] for r in layout["racks"]
                 if r["id"] and (racks[r["id"]].zone, racks[r["id"]].rack_id) != (r["zone"], r["rack_id"])]
        for rid in moved:
            WarehouseModelRack.objects.filter(pk=rid).update(rack_id=f"~{rid}")
        updated, created = [], []
        for r in layout["racks"]:
            obj = racks[r["id"]] if r["id"] else WarehouseModelRack(model=wm)
            for f in RACK_FIELDS:
                setattr(obj, f, r[f])
            obj.x_m, obj.y_m, obj.angle_deg = r["x"], r["y"], r["angle"]
            (updated if r["id"] else created).append(obj)
        WarehouseModelRack.objects.bulk_update(updated, [*RACK_FIELDS, "x_m", "y_m", "angle_deg"])
        WarehouseModelRack.objects.bulk_create(created)
        f_updated, f_created = [], []
        for f in layout["features"]:
            obj = feats[f["id"]] if f["id"] else WarehouseHallFeature(model=wm)
            obj.kind, obj.label = f["kind"], f["label"]
            obj.x_m, obj.y_m, obj.width_m, obj.depth_m, obj.angle_deg = f["x"], f["y"], f["width"], f["depth"], f["angle"]
            (f_updated if f["id"] else f_created).append(obj)
        WarehouseHallFeature.objects.bulk_update(f_updated, ["kind", "label", "x_m", "y_m", "width_m", "depth_m",
                                                             "angle_deg"])
        WarehouseHallFeature.objects.bulk_create(f_created)
        wm.floor_width_m, wm.floor_depth_m, wm.updated_at = layout["floor"]["width"], layout["floor"]["depth"], timezone.now()
        wm.save(update_fields=["floor_width_m", "floor_depth_m", "updated_at"])
    out = _layout(wm)
    out.update(kpi=kpi, issues=issues)
    return JsonResponse(out, json_dumps_params={"ensure_ascii": False})
