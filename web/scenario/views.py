from django import forms
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.roles import GROUP_ADMIN, GROUP_DESIGNER, any_role, designer, has_role

from .models import InboundStream, Scenario, ScenarioDay

KIND_LABEL = dict(InboundStream._meta.get_field("kind").choices)


def _fc(widget):
    widget.attrs.setdefault("class", "form-control")
    return widget


class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ["name", "description", "growth", "seed", "shift_h", *Scenario.NORM_FIELDS]
        widgets = {"description": forms.Textarea(attrs={"rows": 2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            _fc(f.widget)


class NewScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ["name"]
        widgets = {"name": forms.TextInput(attrs={"class": "form-control", "maxlength": 200})}


STREAM_FIELDS = ["kind", "arrivals_min", "arrivals_avg", "arrivals_max", "pallets_min", "pallets_avg",
                 "pallets_max", "window_from", "window_to", "mono_pct", "inspect_pct", "inspect_min"]
StreamFormSet = forms.modelformset_factory(
    InboundStream, fields=STREAM_FIELDS, extra=1, can_delete=True,
    widgets={f: _fc(forms.NumberInput(attrs={"step": "any", "min": 0})) for f in STREAM_FIELDS if f != "kind"}
    | {"kind": _fc(forms.Select())})


def _results(day):
    return {"day": day, "avg": day.demand("avg"), "max": day.demand("max")}


def _arrival_rows(results):
    """Wiersz na typ dostawy: komórki w kolejności kolumn tabeli (dzień × poziom)."""
    out = {}
    for r in results:
        for level in ("avg", "max"):
            for row in r[level]["rows"]:
                out.setdefault(row["kind"], {"label": KIND_LABEL[row["kind"]], "cells": {}})
                out[row["kind"]]["cells"][(r["day"].kind, level)] = row
    cols = [(r["day"].kind, lvl) for r in results for lvl in ("avg", "max")]
    return [{"label": v["label"], "cells": [v["cells"].get(c) for c in cols]} for v in out.values()]


@any_role
def scenario_list(request):
    return render(request, "scenario/list.html", {
        "form": NewScenarioForm(), "scenarios": Scenario.objects.select_related("created_by")[:50]})


@designer
@require_POST
def scenario_create(request):
    form = NewScenarioForm(request.POST)
    if not form.is_valid():
        messages.error(request, "Wpisz nazwę scenariusza.")
        return redirect("scenario:list")
    sc = form.save(commit=False)
    sc.created_by = request.user
    sc.save()
    sc.ensure_days()
    messages.success(request, f"Utworzono scenariusz „{sc}” z przykładowym planem przyjęć — popraw liczby.")
    return redirect("scenario:detail", pk=sc.pk)


@any_role
def scenario_detail(request, pk):
    sc = get_object_or_404(Scenario, pk=pk)
    sc.ensure_days(with_defaults=False)
    days = list(sc.days.prefetch_related("inbound"))
    results = [_results(d) for d in days]
    ctx = {"sc": sc, "results": results, "arrival_rows": _arrival_rows(results)}
    if has_role(request.user, GROUP_ADMIN, GROUP_DESIGNER):
        ctx["form"] = ScenarioForm(instance=sc)
        ctx["formsets"] = [(d, StreamFormSet(queryset=d.inbound.all(), prefix=d.kind)) for d in days]
    return render(request, "scenario/detail.html", ctx)


@designer
@require_POST
def scenario_save(request, pk):
    sc = get_object_or_404(Scenario, pk=pk)
    form = ScenarioForm(request.POST, instance=sc)
    if form.is_valid():
        form.save()
        messages.success(request, "Zapisano parametry i normy — wyniki przeliczone.")
    else:
        for errs in form.errors.values():
            messages.error(request, " ".join(errs))
    return redirect("scenario:detail", pk=pk)


@designer
@require_POST
def day_save(request, pk, kind):
    day = get_object_or_404(ScenarioDay, scenario_id=pk, kind=kind)
    fs = StreamFormSet(request.POST, queryset=day.inbound.all(), prefix=kind)
    if not fs.is_valid():
        for i, errs in enumerate(fs.errors):
            for msg in [e for v in errs.values() for e in v]:
                messages.error(request, f"{day.get_kind_display()}, wiersz {i + 1}: {msg}")
        return redirect("scenario:detail", pk=pk)
    with transaction.atomic():
        for s in fs.save(commit=False):
            s.day = day
            s.save()
        for s in fs.deleted_objects:
            s.delete()
        day.scenario.save(update_fields=["updated_at"])
    messages.success(request, f"Zapisano plan przyjęć: {day.get_kind_display().lower()} — wyniki przeliczone.")
    return redirect("scenario:detail", pk=pk)


@designer
@require_POST
def scenario_copy(request, pk):
    src = get_object_or_404(Scenario, pk=pk)
    with transaction.atomic():
        days = list(src.days.prefetch_related("inbound"))
        sc = Scenario.objects.get(pk=pk)
        sc.pk, sc.name, sc.created_by = None, f"{src.name} (kopia)"[:200], request.user
        sc.save()
        for d in days:
            nd = ScenarioDay.objects.create(scenario=sc, kind=d.kind)
            for s in d.inbound.all():
                s.pk, s.day = None, nd
                s.save()
    messages.success(request, f"Skopiowano scenariusz jako „{sc}”.")
    return redirect("scenario:detail", pk=sc.pk)


@designer
@require_POST
def scenario_delete(request, pk):
    sc = get_object_or_404(Scenario, pk=pk)
    name = sc.name
    sc.delete()
    messages.success(request, f"Usunięto scenariusz „{name}”.")
    return redirect("scenario:list")
