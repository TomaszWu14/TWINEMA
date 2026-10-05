from django import forms
from django.conf import settings
from django.contrib import messages
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_POST

from core.roles import any_role, designer
from twin.blender_scene import model_floor, model_racks
from twin.design_kpi import compute_kpi, rack_to_element
from twin.models import WarehouseModel
from twin.shared import hall_feature_dict

from . import script_ai
from .models import Presentation, Shot
from .script import TARGET_WORDS, WORDS_PER_SECOND, kpi_facts, template_script


def model_kpi(wm):
    """KPI modelu hali tym samym wzorem co wariant bazowy w porównaniu wariantów."""
    racks = model_racks(wm)
    if not racks:
        return {}
    floor = model_floor(wm, racks)
    features = [hall_feature_dict(f) for f in wm.features.all()]
    return compute_kpi([rack_to_element(r) for r in racks], features, floor["width"], floor["depth"])


def _replace_shots(p, shots):
    with transaction.atomic():
        p.shots.all().delete()
        Shot.objects.bulk_create(Shot(presentation=p, order=(i + 1) * 10, **s) for i, s in enumerate(shots))


class PresentationForm(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ["model", "title"]
        widgets = {"model": forms.Select(attrs={"class": "form-control"}),
                   "title": forms.TextInput(attrs={"class": "form-control", "maxlength": 200})}


ShotFormSet = forms.modelformset_factory(
    Shot, fields=["order", "preset", "text"], extra=1, can_delete=True,
    widgets={"order": forms.NumberInput(attrs={"class": "form-control", "min": 0, "max": 999}),
             "preset": forms.Select(attrs={"class": "form-control"}),
             "text": forms.Textarea(attrs={"class": "form-control", "rows": 3, "maxlength": 600})})


@any_role
def presentation_list(request):
    newest = WarehouseModel.objects.first()             # ordering: -created_at
    form = PresentationForm(initial={"model": newest.pk if newest else None})
    form.fields["model"].queryset = WarehouseModel.objects.all()
    return render(request, "studio/list.html", {
        "form": form,
        "presentations": Presentation.objects.select_related("model", "created_by").prefetch_related("shots")[:50],
    })


@designer
@require_POST
def presentation_create(request):
    form = PresentationForm(request.POST)
    form.fields["model"].queryset = WarehouseModel.objects.all()
    if not form.is_valid():
        messages.error(request, "Wybierz model hali i wpisz tytuł filmu.")
        return redirect("studio:list")
    p = form.save(commit=False)
    p.created_by = request.user
    p.save()
    _replace_shots(p, template_script(model_kpi(p.model)))
    messages.success(request, f"Utworzono prezentację „{p}” ze szkicem kwestii z KPI modelu — popraw tekst "
                              "i zatwierdź go przed nagraniem lektora.")
    return redirect("studio:detail", pk=p.pk)


@any_role
def presentation_detail(request, pk):
    p = get_object_or_404(Presentation.objects.select_related("model"), pk=pk)
    formset = ShotFormSet(queryset=p.shots.all()) if p.is_draft else None
    shots = list(p.shots.all())
    words = sum(len(s.text.split()) for s in shots)
    return render(request, "studio/detail.html", {
        "p": p, "formset": formset, "shots": shots, "facts": kpi_facts(model_kpi(p.model)),
        "ai_enabled": script_ai.enabled(), "claude_model": settings.CLAUDE_MODEL,
        "words": words, "seconds": round(words / WORDS_PER_SECOND), "target_words": TARGET_WORDS,
        "steps": Presentation.STATUS_CHOICES,
        "step_index": [k for k, _ in Presentation.STATUS_CHOICES].index(p.status),
    })


def _draft_or_back(request, p):
    if not p.is_draft:
        messages.error(request, "Tekst jest zatwierdzony — najpierw „Wróć do edycji”.")
        return False
    return True


@designer
@require_POST
def shots_save(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    if not _draft_or_back(request, p):
        return redirect("studio:detail", pk=pk)
    formset = ShotFormSet(request.POST, queryset=p.shots.all())
    if not formset.is_valid():
        for err in [e for f in formset.errors for e in f.values()] + list(formset.non_form_errors()):
            messages.error(request, " ".join(err))
        return redirect("studio:detail", pk=pk)
    for shot in formset.save(commit=False):
        shot.presentation = p
        shot.save()
    for shot in formset.deleted_objects:
        shot.delete()
    p.save(update_fields=["updated_at"])
    messages.success(request, "Zapisano kwestie.")
    return redirect("studio:detail", pk=pk)


@designer
@require_POST
def shots_ai(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    if not _draft_or_back(request, p):
        return redirect("studio:detail", pk=pk)
    try:
        shots, warnings = script_ai.draft_script(kpi_facts(model_kpi(p.model)))
    except script_ai.ScriptAIError as exc:
        messages.error(request, str(exc))
        return redirect("studio:detail", pk=pk)
    if not shots:
        messages.error(request, "Szkic z AI nie zawierał żadnej poprawnej kwestii — obecne kwestie bez zmian.")
        return redirect("studio:detail", pk=pk)
    _replace_shots(p, shots)
    messages.success(request, f"Claude napisał szkic: {len(shots)} kwestii. Przeczytaj, popraw i zatwierdź.")
    for w in warnings:
        messages.warning(request, w)
    return redirect("studio:detail", pk=pk)


@designer
@require_POST
def shots_template(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    if _draft_or_back(request, p):
        _replace_shots(p, template_script(model_kpi(p.model)))
        messages.success(request, "Wstawiono szkic z szablonu (KPI modelu).")
    return redirect("studio:detail", pk=pk)


@designer
@require_POST
def approve(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    if not _draft_or_back(request, p):
        return redirect("studio:detail", pk=pk)
    if not p.shots.exclude(text__regex=r"^\s*$").exists():
        messages.error(request, "Dodaj co najmniej jedną kwestię, zanim zatwierdzisz tekst.")
        return redirect("studio:detail", pk=pk)
    p.shots.filter(text__regex=r"^\s*$").delete()
    p.status, p.approved_at = "approved", timezone.now()
    p.save(update_fields=["status", "approved_at", "updated_at"])
    messages.success(request, "Tekst zatwierdzony — można nagrać lektora.")
    return redirect("studio:detail", pk=pk)


@designer
@require_POST
def reopen(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    p.status, p.approved_at = "draft", None
    p.save(update_fields=["status", "approved_at", "updated_at"])
    messages.success(request, "Tekst wrócił do edycji.")
    return redirect("studio:detail", pk=pk)


@designer
@require_POST
def presentation_delete(request, pk):
    p = get_object_or_404(Presentation, pk=pk)
    title = p.title
    p.delete()
    messages.success(request, f"Usunięto prezentację „{title}”.")
    return redirect("studio:list")
