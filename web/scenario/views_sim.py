"""Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI, wąskie gardła, zdarzenia."""
from django import forms
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST

from core.roles import any_role, designer
from twin.models import WarehouseModel

from . import services
from .models import Scenario, ScenarioDay, ScenarioRun
from .sim.engine import M2_PER_PALLET
from .sim.report import PROCS


class SimForm(forms.Form):
    model = forms.ModelChoiceField(queryset=WarehouseModel.objects.all(), label="Model hali (layout)",
                                   widget=forms.Select(attrs={"class": "form-control"}))
    day = forms.ChoiceField(choices=[("both", "Oba dni"), *ScenarioDay.KIND_CHOICES], initial="both",
                            label="Dzień", widget=forms.Select(attrs={"class": "form-control"}))
    runs = forms.IntegerField(min_value=1, max_value=services.MAX_RUNS, initial=12, label="Przebiegów",
                              widget=forms.NumberInput(attrs={"class": "form-control", "min": 1,
                                                              "max": services.MAX_RUNS}))


def kpi_num(value, unit):
    """Liczba KPI do wyświetlenia: sztuki (bez jednostki — palety, paczki, auta, zadania) jako całe,
    czasy i procenty z jednym miejscem po przecinku. Średnie z przebiegów bywają ułamkowe („917,5 palet”)."""
    return f"{round(value):d}" if not unit else f"{round(value, 1):g}"


def _cell(agg, key):
    a = agg[key]
    return {"label": a["label"], "unit": a["unit"], "mean": kpi_num(a["mean"], a["unit"]),
            "worst": kpi_num(a["worst"], a["unit"])}


def _sim_view(run, memo=None):
    """Wynik zapisany w ScenarioRun → grupy karty KPI (#21), wykres osi czasu i wąskie gardła."""
    r = run.result
    agg, pl, tl = r["agg"], r["places"], r["rep"]["timeline"]
    need = {s: agg[f"staging_{s}_max"]["worst"] * M2_PER_PALLET for s in ("in", "out")}
    groups = [
        ("Przepustowość dnia", [_cell(agg, k) for k in ("pallets_in", "pallets_out", "parcels", "parcels_late",
                                                         "trucks_out_late", "out_delay_max_min")]),
        ("Doki i pole odkładcze", [_cell(agg, k) for k in (
            "wait_in_container_p95_min", "wait_in_pallet_p95_min", "wait_out_p95_min", "queue_in_container_max",
            "queue_in_pallet_max", "queue_out_max", "staging_in_max", "staging_out_max")]),
        ("Obsada i flota", [_cell(agg, k) for k in ("fleet_util_pct", "fleet_peak_pct", "fleet_wait_p95_min",
                                                     "fleet_effective", "fleet_charge_h", "unfinished") if k in agg]
         + [_cell(agg, f"util_{p}") for p, _ in PROCS] + [_cell(agg, f"wait_{p}_p95_min") for p, _ in PROCS]),
    ]
    queue = [a + b + c for a, b, c in zip(tl["queue_in_container"], tl["queue_in_pallet"], tl["queue_out"],
                                          strict=True)]
    chart = {"t": tl["t"], "series": [
        {"name": "Auta w kolejce", "data": queue},
        {"name": "Palety na polu przyjęć", "data": tl["staging_in"]},
        {"name": "Palety na polu wydań", "data": tl["staging_out"]},
        {"name": "Wózki w pracy", "data": tl["fleet_busy"]},
    ]}
    hourly = [{"t": tl["t"][i], "queue": queue[i], "staging_in": tl["staging_in"][i],
               "staging_out": tl["staging_out"][i], "fleet": tl["fleet_busy"][i]}
              for i in range(0, len(tl["t"]), 4) if queue[i] or tl["staging_in"][i] or tl["staging_out"][i]
              or tl["fleet_busy"][i]]
    return {"run": run, "groups": groups, "bottlenecks": r["bottlenecks"], "chart": chart, "hourly": hourly,
            "docks": pl["counts"], "warnings": pl["warnings"],
            "staging": [{"side": "przyjęć", "need": round(need["in"]), "drawn": pl["staging_m2"]["in"]},
                        {"side": "wydań", "need": round(need["out"]), "drawn": pl["staging_m2"]["out"]}],
            "errors": sum(b["severity"] == "error" for b in r["bottlenecks"]),
            "capacity": (r.get("placement") or {}).get("capacity"), "cpp": r.get("cpp"), "fleet": r.get("fleet"),
            "costs": services.run_costs(run, memo=memo)}


@designer
@require_POST
def scenario_simulate(request, pk):
    sc = get_object_or_404(Scenario, pk=pk)
    form = SimForm(request.POST)
    if not form.is_valid():
        messages.error(request, f"Wybierz model hali i liczbę przebiegów (1–{services.MAX_RUNS}).")
        return redirect("scenario:detail", pk=pk)
    sc.ensure_days(with_defaults=False)
    kinds = [k for k, _ in ScenarioDay.KIND_CHOICES] if form.cleaned_data["day"] == "both" \
        else [form.cleaned_data["day"]]
    done = []
    for day in sc.days.filter(kind__in=kinds).prefetch_related("inbound", "outbound"):
        run = services.simulate(day, form.cleaned_data["model"], runs=form.cleaned_data["runs"], user=request.user)
        n_err = sum(b["severity"] == "error" for b in run.result["bottlenecks"])
        done.append(f"{day.get_kind_display().lower()}: {len(run.result['bottlenecks'])} wąskich gardeł"
                    f"{f' ({n_err} krytycznych)' if n_err else ''}, {run.duration_s:g} s")
    messages.success(request, f"Symulacja na „{form.cleaned_data['model']}” ({form.cleaned_data['runs']} "
                              f"przebiegów) — " + "; ".join(done) + ".")
    return redirect(reverse("scenario:detail", args=[pk]) + "#sc-sim-h")


@any_role
def run_events(request, pk):
    """Zdarzenia przebiegu reprezentatywnego dla odtwarzacza 3D (format: `scenario.sim` docstring)."""
    run = get_object_or_404(ScenarioRun.objects.select_related("model"), pk=pk)
    return JsonResponse({"format": "twinema.scenario-events", "version": 1, "run": run.pk,
                         "model": run.model_id, "day": run.day_kind, "seed": run.result["rep"]["seed"],
                         "columns": ["t_s", "obj", "kind", "what", "place"], "events": run.events})
