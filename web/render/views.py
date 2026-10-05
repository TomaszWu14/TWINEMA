from urllib.parse import urlencode

from django import forms
from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.roles import any_role, designer
from twin.models import WarehouseModel

from .models import RenderJob

SOURCES = [("demo", "Symulacja demo (wózki i kompletacja)"), ("wt", "Ostatni import zadań magazynowych"),
           ("stock", "Sam stan magazynu (bez ruchu)")]


class RenderJobForm(forms.ModelForm):
    source = forms.ChoiceField(choices=SOURCES, initial="demo", label="Ruch w scenie")
    pallets = forms.BooleanField(required=False, initial=True, label="Palety na stanie")

    class Meta:
        model = RenderJob
        fields = ["model", "preset", "kind", "resolution", "seconds", "title"]
        widgets = {"seconds": forms.NumberInput(attrs={"min": 2, "max": 60})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f in self.fields.values():
            if not isinstance(f.widget, forms.CheckboxInput):
                f.widget.attrs.setdefault("class", "form-control")

    def clean_seconds(self):
        s = self.cleaned_data["seconds"]
        if not 2 <= s <= 60:
            raise forms.ValidationError("Długość klipu: 2–60 s.")
        return s

    def scene_query(self):
        """Parametry sceny jak w odtwarzaczu 3D — budowane tu, nie wpisywane ręcznie."""
        q = {}
        src = self.cleaned_data["source"]
        if src == "wt":
            q["wt"] = "latest"
        elif src == "stock":
            q.update({"forklifts": 0, "pickers": 1, "picks": 1})
        if not self.cleaned_data["pallets"]:
            q["pallets"] = 0
        return urlencode(q)


@any_role
def jobs(request):
    initial = {}
    if (m := request.GET.get("model", "")).isdigit():
        initial["model"] = int(m)
    form = RenderJobForm(initial=initial)
    form.fields["model"].queryset = WarehouseModel.objects.order_by("-created_at")
    last = RenderJob.objects.exclude(worker="").order_by("-claimed_at").first()
    return render(request, "render/jobs.html", {
        "form": form, "jobs": RenderJob.objects.select_related("model", "created_by")[:40],
        "worker_enabled": bool(settings.RENDER_WORKER_TOKEN), "last_worker": last,
        "active": RenderJob.objects.filter(status__in=("queued", "running")).exists(),
    })


@designer
@require_POST
def create(request):
    form = RenderJobForm(request.POST)
    form.fields["model"].queryset = WarehouseModel.objects.all()
    if not form.is_valid():
        for errors in form.errors.values():
            messages.error(request, " ".join(errors))
        return redirect("render:jobs")
    job = form.save(commit=False)
    job.scene_query = form.scene_query()
    job.created_by = request.user
    job.save()
    messages.success(request, f"Zlecenie „{job}” w kolejce — worker z Blenderem pobierze je przy następnym odpytaniu.")
    return redirect("render:jobs")


@any_role
def result_file(request, pk):
    job = get_object_or_404(RenderJob, pk=pk, status="done")
    if not job.result:
        raise Http404
    ctype = "video/mp4" if job.kind == "video" else "image/png"
    resp = FileResponse(job.result.open("rb"), content_type=ctype)
    disp = "attachment" if request.GET.get("pobierz") else "inline"
    resp["Content-Disposition"] = f'{disp}; filename="twinema_render_{job.pk}.{job.extension}"'
    resp["X-Content-Type-Options"] = "nosniff"
    return resp


@designer
@require_POST
def delete(request, pk):
    job = get_object_or_404(RenderJob, pk=pk)
    if job.result:
        job.result.delete(save=False)
    job.delete()
    messages.success(request, "Usunięto zlecenie renderu.")
    return redirect("render:jobs")


@any_role
def status_json(request):
    """Stan zleceń w toku — strona odpytuje i przeładowuje się, gdy coś się zmieni."""
    rows = RenderJob.objects.filter(status__in=("queued", "running")).values_list("pk", "status")
    return JsonResponse({"active": [f"{pk}:{st}" for pk, st in rows]})
