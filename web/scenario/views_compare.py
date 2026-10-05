"""Tabela porównania layout × scenariusz (E7) i eksport xlsx (E8)."""
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from core.roles import any_role

from equipment.models import CostRate

from .compare import compare_columns
from .export import compare_workbook, run_workbook
from .models import ScenarioRun
from .services import run_costs

MAX_COLS = 6
XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"


def _label(run):
    return f"{run.scenario} · {run.get_day_kind_display().lower()} · {run.model}"


def _xlsx(data, name):
    resp = HttpResponse(data, content_type=XLSX)
    resp["Content-Disposition"] = f'attachment; filename="{name}"'
    return resp


@any_role
def compare(request):
    runs = list(ScenarioRun.objects.defer("events").select_related("scenario__fleet_equipment", "model")[:40])
    by_pk = {r.pk: r for r in runs}
    ids = [int(x) for x in request.GET.getlist("ids") if x.isdigit()]
    chosen = [by_pk[i] for i in dict.fromkeys(ids) if i in by_pk][:MAX_COLS]
    rates = CostRate.as_dict()
    rows = compare_columns([{**r.result, "costs": run_costs(r, rates)} for r in chosen]) if chosen else []
    if chosen and request.GET.get("xlsx"):
        return _xlsx(compare_workbook([_label(r) for r in chosen], rows), "twinema_porownanie.xlsx")
    return render(request, "scenario/compare.html", {
        "runs": runs, "chosen": chosen, "chosen_ids": {r.pk for r in chosen}, "rows": rows,
        "labels": [_label(r) for r in chosen], "max_cols": MAX_COLS, "query": request.GET.urlencode()})


@any_role
def run_xlsx(request, pk):
    run = get_object_or_404(ScenarioRun.objects.defer("events").select_related("scenario", "model"), pk=pk)
    day = run.scenario.days.prefetch_related("inbound", "outbound").get(kind=run.day_kind)
    return _xlsx(run_workbook(run, day), f"twinema_symulacja_{run.pk}.xlsx")
