# API edytora layoutu (E1, E2b, D1 — działka w polu `site`): odczyt planu hali, sprawdzenie bez zapisu
# (KPI + problemy) i zapis całości w jednej transakcji z blokadą optymistyczną po `version` (= updated_at modelu). Logika w twin/layout.py.
# Podkład (rzut hali PNG/JPG) wgrywany osobno — bez zmiany `version`, żeby nie unieważnić otwartego edytora.
import json

from django.core.files.base import ContentFile
from django.http import FileResponse, Http404
from django.urls import reverse
from django.utils import timezone

from equipment.models import Equipment
from twin.design_catalog import ELEMENTS, SHELF_AISLE_M
from twin.layout import (
    RACK_LIMITS, LayoutError, analyze, clean_layout, column_list, feature_row, rack_row,
)
from twin.site import AREA_KINDS, check_site, clean_site, default_site, site_kpi
from twin.shared import (
    _md_role, _planner, get_object_or_404, HALL_FEATURE_COLORS, hall_feature_kinds, JsonResponse, render,
    require_POST, transaction, WarehouseHallFeature, WarehouseModel, WarehouseModelRack,
)

MAX_BODY = 2 * 1024 * 1024
MAX_UNDERLAY = 10 * 1024 * 1024
MAX_UNDERLAY_PX = 12_000                      # bok obrazu — chroni przed „bombą” dekompresji
RACK_FIELDS = ("zone", "rack_id", "n_bays", "n_levels", "bay_width_cm", "depth_cm", "level_height_cm", "equipment")
SIGNATURES = {"png": b"\x89PNG\r\n\x1a\n", "jpg": b"\xff\xd8\xff"}


def _version(wm):
    return wm.updated_at.isoformat()


def _underlay(wm):
    if not wm.underlay:
        return None
    return {**wm.underlay_meta, "url": reverse("twin:warehouse_layout_underlay", args=[wm.pk])}


def _layout(wm):
    floor = {"width": wm.floor_width_m, "depth": wm.floor_depth_m, "clear_height": wm.clear_height_m}
    return {"floor": floor,
            "racks": [rack_row(r) for r in wm.racks.order_by("zone", "rack_id")],
            "features": [feature_row(f) for f in wm.features.order_by("pk")],
            "columns": wm.columns or {}, "column_list": column_list(wm.columns, floor),
            "underlay": _underlay(wm), "version": _version(wm), "feature_kinds": hall_feature_kinds(),
            "site": wm.site or {}}


def _parse(request):
    """→ (layout, None) albo (None, odpowiedź błędu)."""
    if len(request.body) > MAX_BODY:
        return None, JsonResponse({"error": "Za duży plan (maks. 2 MB)."}, status=413)
    try:
        data = json.loads(request.body)
        layout = clean_layout(data, hall_feature_kinds())
        # brak klucza `site` (stary klient) = działka bez zmian; {} = usuń działkę
        layout["site"] = clean_site(data["site"]) if isinstance(data, dict) and "site" in data else None
        return layout, None
    except (UnicodeDecodeError, json.JSONDecodeError):
        return None, JsonResponse({"error": "To nie jest poprawny JSON."}, status=400)
    except LayoutError as exc:
        return None, JsonResponse({"error": str(exc)}, status=400)


def equipment_catalog():
    """{id: parametry} sprzętu obsługującego regały (reach/VNA) — do walidacji layoutu (K1)."""
    return {e.pk: e.params() for e in Equipment.objects.filter(kind__in=("reach", "counterbalance", "vna"))}


def _analyze(layout):
    """analyze + lista słupów do rysowania; zła siatka słupów (za gęsta) → (None, odpowiedź 400)."""
    try:
        kpi, issues = analyze(layout, equipment_catalog())
        if layout["site"]:
            kpi["site"] = site_kpi(layout["site"], layout["floor"], layout["racks"])
            issues += check_site(layout["site"], layout["floor"], layout["racks"], layout["features"])
        return (kpi, issues, column_list(layout["columns"], layout["floor"])), None
    except LayoutError as exc:
        return None, JsonResponse({"error": str(exc)}, status=400)


@_md_role
def warehouse_layout_editor(request, pk):
    """Edytor planu hali (E2): dane przez uklad.json, sprawdzanie i zapis przez API powyżej."""
    wm = get_object_or_404(WarehouseModel, pk=pk)
    config = {
        "urls": {"layout": reverse("twin:warehouse_layout_json", args=[pk]),
                 "check": reverse("twin:warehouse_layout_check", args=[pk]),
                 "save": reverse("twin:warehouse_layout_save", args=[pk]),
                 "underlay": reverse("twin:warehouse_layout_underlay_upload", args=[pk])},
        "limits": RACK_LIMITS, "featureColors": HALL_FEATURE_COLORS,
        "aisle": ELEMENTS["rack_std"]["aisle_m"],
        "equipment": dict(WarehouseModelRack.EQUIPMENT_CHOICES),
        "dockRoles": dict(WarehouseHallFeature.DOCK_ROLE_CHOICES),
        "aisles": {"reach": ELEMENTS["rack_std"]["aisle_m"], "vna": ELEMENTS["rack_vna"]["aisle_m"],
                   "shelf": SHELF_AISLE_M},
        "areaKinds": AREA_KINDS,
        "catalog": [{"id": e["id"], "name": e["name"], "kind": e["kind"], "aisle_m": e["aisle_m"],
                     "max_lift_m": e["max_lift_m"]} for e in equipment_catalog().values()],
        "defaultSite": default_site({"width": wm.floor_width_m, "depth": wm.floor_depth_m,
                                     "clear_height": wm.clear_height_m}),
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
    res, err = _analyze(layout)
    if err:
        return err
    kpi, issues, cols = res
    return JsonResponse({"kpi": kpi, "issues": issues, "column_list": cols}, json_dumps_params={"ensure_ascii": False})


@require_POST
@_md_role
def warehouse_layout_save(request, pk):
    layout, err = _parse(request)
    if err:
        return err
    res, err = _analyze(layout)
    if err:
        return err
    kpi, issues, _ = res
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
            if r["load_kg"] is not None:
                obj.load_kg = r["load_kg"]
            if r["equipment_given"]:
                obj.equipment_model_id = r["equipment_id"]
            obj.x_m, obj.y_m, obj.angle_deg = r["x"], r["y"], r["angle"]
            (updated if r["id"] else created).append(obj)
        WarehouseModelRack.objects.bulk_update(updated, [*RACK_FIELDS, "load_kg", "equipment_model", "x_m", "y_m",
                                                         "angle_deg"])
        WarehouseModelRack.objects.bulk_create(created)
        f_updated, f_created = [], []
        for f in layout["features"]:
            obj = feats[f["id"]] if f["id"] else WarehouseHallFeature(model=wm)
            obj.kind, obj.label = f["kind"], f["label"]
            if f["dock_role"] is not None:
                obj.dock_role = f["dock_role"]
            obj.x_m, obj.y_m, obj.width_m, obj.depth_m, obj.angle_deg = f["x"], f["y"], f["width"], f["depth"], f["angle"]
            (f_updated if f["id"] else f_created).append(obj)
        WarehouseHallFeature.objects.bulk_update(f_updated, ["kind", "label", "dock_role", "x_m", "y_m", "width_m",
                                                             "depth_m",
                                                             "angle_deg"])
        WarehouseHallFeature.objects.bulk_create(f_created)
        wm.floor_width_m, wm.floor_depth_m = layout["floor"]["width"], layout["floor"]["depth"]
        wm.clear_height_m, wm.columns = layout["floor"]["clear_height"], layout["columns"]
        if layout["site"] is not None:
            wm.site = layout["site"]
        if wm.underlay and layout["underlay"]:
            wm.underlay_meta = {**wm.underlay_meta, **layout["underlay"]}
        wm.updated_at = timezone.now()
        wm.save(update_fields=["floor_width_m", "floor_depth_m", "clear_height_m", "columns", "underlay_meta",
                               "site", "updated_at"])
    out = _layout(wm)
    out.update(kpi=kpi, issues=issues)
    return JsonResponse(out, json_dumps_params={"ensure_ascii": False})


def _image_size(data):
    """(szer., wys.) obrazu PNG/JPG albo None. Pillow przychodzi z fpdf2 (requirements)."""
    import io

    from PIL import Image, UnidentifiedImageError

    try:
        with Image.open(io.BytesIO(data)) as im:
            im.verify()
            return im.size
    except (UnidentifiedImageError, OSError, SyntaxError, Image.DecompressionBombError, ValueError):
        return None


@require_POST
@_md_role
def warehouse_layout_underlay_upload(request, pk):
    """Wgranie (plik) albo usunięcie (`delete`) podkładu. Skala startowa: obraz na całą szerokość hali."""
    wm = get_object_or_404(WarehouseModel, pk=pk)
    if request.POST.get("delete"):
        if wm.underlay:
            wm.underlay.delete(save=False)
        WarehouseModel.objects.filter(pk=pk).update(underlay="", underlay_meta={})
        return JsonResponse({"underlay": None})
    f = request.FILES.get("file")
    if f is None:
        return JsonResponse({"error": "Wybierz plik PNG albo JPG z rzutem hali."}, status=400)
    if f.size > MAX_UNDERLAY:
        return JsonResponse({"error": "Plik większy niż 10 MB — zmniejsz rozdzielczość rzutu."}, status=413)
    data = f.read()
    ext = next((e for e, sig in SIGNATURES.items() if data.startswith(sig)), None)
    size = _image_size(data) if ext else None
    if not size:
        return JsonResponse({"error": "To nie jest obraz PNG ani JPG (PDF: zapisz stronę rzutu jako PNG)."},
                            status=400)
    w, h = size
    if max(w, h) > MAX_UNDERLAY_PX:
        return JsonResponse({"error": f"Obraz za duży ({w}×{h} px); maks. {MAX_UNDERLAY_PX} px na bok."}, status=400)
    old = wm.underlay.name if wm.underlay else ""
    wm.underlay.save(f"podklad_{wm.pk}.{ext}", ContentFile(data), save=False)
    if old and old != wm.underlay.name:
        wm.underlay.storage.delete(old)
    keep = {k: wm.underlay_meta[k] for k in ("x", "y", "opacity") if k in wm.underlay_meta}
    meta = {"scale": round(wm.floor_width_m / w, 6), "x": 0.0, "y": 0.0, "opacity": 0.5, **keep, "w_px": w, "h_px": h}
    WarehouseModel.objects.filter(pk=pk).update(underlay=wm.underlay.name, underlay_meta=meta)   # bez zmiany version
    wm.underlay_meta = meta
    return JsonResponse({"underlay": _underlay(wm)})


@_md_role
def warehouse_layout_underlay(request, pk):
    wm = get_object_or_404(WarehouseModel, pk=pk)
    if not wm.underlay:
        raise Http404
    ctype = "image/png" if wm.underlay.name.endswith(".png") else "image/jpeg"
    resp = FileResponse(wm.underlay.open("rb"), content_type=ctype)
    resp["X-Content-Type-Options"] = "nosniff"
    return resp
