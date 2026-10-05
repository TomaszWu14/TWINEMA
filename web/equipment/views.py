from django import forms
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.roles import GROUP_ADMIN, any_role, designer, has_role

from .catalog import KINDS, capacity_at
from .models import PARAM_FIELDS, Equipment


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ["kind", "name", *PARAM_FIELDS, "cost_purchase", "cost_per_hour", "notes"]
        widgets = {"lift_curve": forms.Textarea(attrs={"rows": 2}), "notes": forms.Textarea(attrs={"rows": 2})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            f.widget.attrs.setdefault("class", "form-control")

    def clean_lift_curve(self):
        pts = self.cleaned_data["lift_curve"] or []
        if not isinstance(pts, list) or not all(isinstance(p, list) and len(p) == 2 and all(
                isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0 for v in p) for p in pts):
            raise forms.ValidationError("Lista punktów [wysokość m, udźwig kg], np. [[6, 1600], [10, 1000]].")
        return sorted(pts)

    def clean(self):
        data = super().clean()
        for f in ("speed_loaded_kmh", "speed_empty_kmh"):
            if data.get(f) is not None and data[f] <= 0:
                self.add_error(f, "Prędkość musi być dodatnia.")
        return data


def _can_edit(user, eq):
    """Klasy systemowe zmienia tylko administrator; własne modele — Projektant i administrator."""
    return has_role(user, GROUP_ADMIN) if eq.is_system else True


def _curve(eq):
    """Punkty wykresu udźwigu: od 0 do maks. wysokości (albo ostatniego punktu krzywej)."""
    top = eq.max_lift_m or max([p[0] for p in eq.lift_curve] or [0])
    if not top or not eq.lift_curve:
        return []
    return [{"h": round(top * i / 10, 2), "kg": round(capacity_at(eq.capacity_kg, eq.lift_curve, top * i / 10))}
            for i in range(11)]


@any_role
def catalog_list(request):
    kind = request.GET.get("typ", "")
    items = Equipment.objects.all()
    if kind in dict(KINDS):
        items = items.filter(kind=kind)
    return render(request, "equipment/list.html", {"items": items, "kinds": KINDS, "kind": kind})


@any_role
def catalog_detail(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    rows = [(Equipment._meta.get_field(f).verbose_name, getattr(eq, f)) for f in PARAM_FIELDS if f != "lift_curve"]
    curve = _curve(eq)
    top = max([c["kg"] for c in curve] or [1])
    return render(request, "equipment/detail.html", {
        "eq": eq, "rows": rows, "curve": curve, "can_edit": _can_edit(request.user, eq),
        "bars": [{**c, "pct": round(100 * c["kg"] / top)} for c in curve],
        "racks": eq.racks.count(), "scenarios": eq.scenarios.count()})


@designer
def catalog_form(request, pk=None):
    eq = get_object_or_404(Equipment, pk=pk) if pk else None
    if eq and not _can_edit(request.user, eq):
        return render(request, "core/403.html", status=403)
    form = EquipmentForm(request.POST or None, instance=eq)
    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=False)
        if not eq:
            obj.created_by = request.user
        obj.save()
        messages.success(request, f"Zapisano „{obj}”.")
        return redirect("equipment:detail", pk=obj.pk)
    return render(request, "equipment/form.html", {"form": form, "eq": eq})


@designer
@require_POST
def catalog_copy(request, pk):
    src = get_object_or_404(Equipment, pk=pk)
    src.pk, src.is_system, src.created_by = None, False, request.user
    src.name = f"{src.name} (kopia)"[:120]
    src.save()
    messages.success(request, "Skopiowano jako własny model — wpisz parametry z karty katalogowej.")
    return redirect("equipment:edit", pk=src.pk)


@designer
@require_POST
def catalog_delete(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    if eq.is_system:
        return render(request, "core/403.html", status=403)
    name = eq.name
    eq.delete()
    messages.success(request, f"Usunięto „{name}” (regały i scenariusze z tym sprzętem wracają do ustawień ogólnych).")
    return redirect("equipment:list")
