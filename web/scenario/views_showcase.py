"""Prezentacje 3D (P1): lista, tworzenie (ze szablonem startowym), odtwarzacz + edytor slajdów, dane JSON.

Podgląd ogląda (odtwarzacz i dane: layout 3D + wyniki, bez danych źródłowych), Projektant tworzy i edytuje.
Udostępnienie = adres strony prezentacji dla zalogowanych (bez publicznego linku)."""
import json

from django import forms
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.decorators.http import require_POST

from core.roles import any_role, designer
from twin.layout import rack_row
from twin.models import WarehouseModel
from twin.shared import safe_json
from twin.site import site_kpi
from twin.views.warehouse_model import model_scene_data

from .models import ScenarioRun, Showcase
from .showcase import CARDS, SlideError, clean_slides, kpi_cards, template_slides
from .views_play import bottleneck_focus, layout_places, peak_index
from .views_sim import _sim_view

MAX_BODY = 512 * 1024


class ShowcaseForm(forms.ModelForm):
    class Meta:
        model = Showcase
        fields = ["title", "model", "run"]
        widgets = {"title": forms.TextInput(attrs={"class": "form-control", "maxlength": 200}),
                   "model": forms.Select(attrs={"class": "form-control"}),
                   "run": forms.Select(attrs={"class": "form-control"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["run"].queryset = ScenarioRun.objects.select_related("scenario", "model")
        self.fields["run"].required = False
        self.fields["run"].empty_label = "— bez wyników symulacji —"

    def clean(self):
        d = super().clean()
        if d.get("run") and d.get("model") and d["run"].model_id != d["model"].pk:
            raise forms.ValidationError("Wynik symulacji musi dotyczyć wybranego modelu hali.")
        return d


def _context(sc):
    """Wszystko, czego potrzebuje odtwarzacz i szablon startowy (jedno źródło)."""
    wm = sc.model
    racks, features, _ = model_scene_data(wm)
    floor = {"width": wm.floor_width_m, "depth": wm.floor_depth_m}
    places = layout_places(features, floor)
    site = site_kpi(wm.site, {**floor, "clear_height": wm.clear_height_m},
                    [rack_row(r) for r in wm.racks.all()]) if wm.site else None
    run, view, bns, peak = sc.run, None, [], 0
    if run:
        view = _sim_view(run)
        bns = [{**b, **bottleneck_focus(b, places)} for b in run.result.get("bottlenecks", [])]
        peak = peak_index(run.result.get("rep", {}).get("timeline") or {"t": []}) * 900
    cards = kpi_cards(view["groups"] if view else (), view and view["capacity"], site)
    return {"wm": wm, "racks": racks, "features": features, "floor": floor, "places": places, "site_kpi": site,
            "run": run, "view": view, "bottlenecks": bns, "peak": peak, "cards": cards}


def _template(sc, ctx):
    run, agg = ctx["run"], (ctx["run"].result.get("agg", {}) if ctx["run"] else {})
    cap, site = (ctx["view"] or {}).get("capacity") or {}, ctx["site_kpi"] or {}
    mean = lambda k: agg[k]["mean"] if k in agg else None             # noqa: E731
    facts = {"positions": cap.get("positions"), "need": cap.get("need"), "fill_pct": cap.get("fill_pct"),
             "day": {"typical": "typowym", "peak": "szczytowym"}.get(run.day_kind) if run else None,
             "pallets_in": mean("pallets_in"), "pallets_out": mean("pallets_out"), "parcels": mean("parcels"),
             "bottlenecks": len(ctx["bottlenecks"]) if run else None,
             "errors": sum(b["severity"] == "error" for b in ctx["bottlenecks"]),
             "coverage_pct": site.get("coverage_pct"), "reserve_m2": site.get("reserve_m2")}
    return template_slides(
        title=sc.title, floor=ctx["floor"], racks=ctx["racks"], places=ctx["places"], site_kpi_=ctx["site_kpi"],
        cards=ctx["cards"], facts=facts,
        run={"day": run.get_day_kind_display().lower(), "has_events": bool(run.events), "peak_t": ctx["peak"],
             "bottlenecks": ctx["bottlenecks"]} if run else None)


@any_role
def showcase_list(request):
    raw = request.GET.get("run", "")
    run = ScenarioRun.objects.filter(pk=int(raw)).select_related("scenario").first() if raw.isdigit() else None
    form = ShowcaseForm(initial={
        "model": run.model_id if run else WarehouseModel.objects.values_list("pk", flat=True).first(),
        "run": run.pk if run else None, "title": f"{run.scenario.name} — prezentacja" if run else ""})
    return render(request, "scenario/showcase_list.html", {
        "form": form, "items": Showcase.objects.select_related("model", "run", "created_by")[:60]})


@designer
@require_POST
def showcase_create(request):
    form = ShowcaseForm(request.POST)
    if not form.is_valid():
        for errs in form.errors.values():
            messages.error(request, " ".join(errs))
        return redirect("scenario:showcase_list")
    sc = form.save(commit=False)
    sc.created_by = request.user
    sc.save()
    sc.slides = _template(sc, _context(sc))
    sc.save(update_fields=["slides"])
    messages.success(request, f"Utworzono prezentację „{sc}” — {len(sc.slides)} slajdów ze szablonu. "
                              "Popraw podpisy, dodaj własne ujęcia i zapisz.")
    return redirect("scenario:showcase", pk=sc.pk)


@any_role
def showcase_detail(request, pk):
    sc = get_object_or_404(Showcase.objects.select_related("model", "run__scenario"), pk=pk)
    ctx = _context(sc)
    return render(request, "scenario/showcase.html", {
        "sc": sc, "cards": ctx["cards"], "card_names": CARDS, "bottlenecks": ctx["bottlenecks"],
        "share_url": request.build_absolute_uri(reverse("scenario:showcase", args=[pk])),
        "config_json": safe_json({"data": reverse("scenario:showcase_data", args=[pk]),
                                  "save": reverse("scenario:showcase_save", args=[pk]),
                                  "events": reverse("scenario:run_events", args=[sc.run_id]) if sc.run_id else None}),
    })


@any_role
def showcase_data(request, pk):
    """Dane odtwarzacza: scena (layout + działka), miejsca, wyniki (karty KPI, wąskie gardła, oś czasu), slajdy."""
    sc = get_object_or_404(Showcase.objects.select_related("model", "run"), pk=pk)
    ctx = _context(sc)
    tl = (sc.run.result.get("rep", {}).get("timeline") if sc.run else None) or {"t": []}
    return JsonResponse({
        "format": "twinema.showcase", "version": 1, "title": sc.title, "slides": sc.slides,
        "floor": ctx["floor"], "racks": ctx["racks"], "features": ctx["features"], "site": sc.model.site or {},
        "places": ctx["places"], "cards": ctx["cards"], "bottlenecks": ctx["bottlenecks"], "peak_t": ctx["peak"],
        "has_events": bool(sc.run and sc.run.events),
        "timeline": {"step_s": 900, "fleet_busy": tl.get("fleet_busy", []),
                     "people": {p: v["busy"] for p, v in (tl.get("people") or {}).items()}},
    }, json_dumps_params={"ensure_ascii": False})


@designer
@require_POST
def showcase_save(request, pk):
    sc = get_object_or_404(Showcase, pk=pk)
    if len(request.body) > MAX_BODY:
        return JsonResponse({"error": "Za dużo danych (maks. 512 KB)."}, status=413)
    try:
        data = json.loads(request.body)
        slides = clean_slides(data.get("slides") if isinstance(data, dict) else None)
    except (UnicodeDecodeError, json.JSONDecodeError):
        return JsonResponse({"error": "To nie jest poprawny JSON."}, status=400)
    except SlideError as exc:
        return JsonResponse({"error": str(exc)}, status=400)
    sc.slides = slides
    sc.save(update_fields=["slides", "updated_at"])
    return JsonResponse({"ok": True, "slides": slides})


@designer
@require_POST
def showcase_reset(request, pk):
    sc = get_object_or_404(Showcase.objects.select_related("model", "run"), pk=pk)
    sc.slides = _template(sc, _context(sc))
    sc.save(update_fields=["slides", "updated_at"])
    messages.success(request, "Slajdy zastąpione szablonem startowym.")
    return redirect("scenario:showcase", pk=pk)


@designer
@require_POST
def showcase_delete(request, pk):
    sc = get_object_or_404(Showcase, pk=pk)
    title = sc.title
    sc.delete()
    messages.success(request, f"Usunięto prezentację „{title}”.")
    return redirect("scenario:showcase_list")
