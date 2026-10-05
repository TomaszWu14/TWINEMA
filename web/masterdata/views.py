from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from core.roles import any_role, designer

from . import importers, services
from .models import ImportLog, Material

MAX_UPLOAD_MB = 25
KINDS = dict(ImportLog.KIND_CHOICES)
KIND_HELP = {
    "materials": "Kod, nazwa, grupa towarowa, karton (wymiary, waga, szt.), paletyzacja. Istniejące kody są aktualizowane.",
    "locations": "Kody lokalizacji z typem, poziomem i wymiarami. Każdy import tworzy nowy aktywny master.",
    "stock": "Lokalizacja, materiał, ilość, HU, partia, data ważności. Najnowszy import = aktualny stan w scenie 3D.",
}


@any_role
def home(request):
    from twin.models import WarehouseLocationMasterBatch, WarehouseModel

    stock_log = services.current_stock_log()
    return render(request, "masterdata/home.html", {
        "kinds": [(k, label, KIND_HELP[k]) for k, label in ImportLog.KIND_CHOICES],
        "n_materials": Material.objects.count(),
        "n_groups": Material.objects.exclude(group="").values("group").distinct().count(),
        "stock_log": stock_log,
        "stock_locations": stock_log.stock_items.values("location_code").distinct().count() if stock_log else 0,
        "master": WarehouseLocationMasterBatch.objects.filter(is_active=True).first(),
        "logs": ImportLog.objects.select_related("uploaded_by")[:20],
        "models": WarehouseModel.objects.order_by("-created_at")[:20],
        "max_mb": MAX_UPLOAD_MB,
    })


@designer
@require_POST
def upload(request, kind):
    if kind not in KINDS:
        return redirect("masterdata:home")
    f = request.FILES.get("file")
    if not f:
        messages.error(request, "Wybierz plik do importu.")
        return redirect("masterdata:home")
    if f.size > MAX_UPLOAD_MB * 1024 * 1024:
        messages.error(request, f"Plik jest większy niż {MAX_UPLOAD_MB} MB — podziel go.")
        return redirect("masterdata:home")
    try:
        log = services.import_file(kind, f.name, f.read(), request.user)
    except importers.ImportFileError as exc:
        messages.error(request, f"{KINDS[kind]}: {exc}")
        return redirect("masterdata:home")
    level = messages.WARNING if log.rows_rejected else messages.SUCCESS
    messages.add_message(request, level, f"{KINDS[kind]}: zapisano {log.rows_ok} z {log.rows_total} wierszy"
                         + (f", odrzucono {log.rows_rejected}." if log.rows_rejected else "."))
    return redirect("masterdata:log_detail", pk=log.pk)


@any_role
def log_detail(request, pk):
    log = get_object_or_404(ImportLog, pk=pk)
    labels = importers.LABELS
    return render(request, "masterdata/log_detail.html", {
        "log": log,
        "columns": [(labels.get(f, f), header) for f, header in log.columns.items()],
        "unmapped": [labels[f] for f in importers.ALIASES[log.kind] if f not in log.columns],
        "stock_preview": log.stock_items.all()[:50] if log.kind == "stock" else None,
    })


@any_role
def template(request, kind):
    if kind not in KINDS:
        return redirect("masterdata:home")
    resp = HttpResponse("﻿" + importers.template_csv(kind), content_type="text/csv; charset=utf-8")
    resp["Content-Disposition"] = f'attachment; filename="twinema_wzor_{kind}.csv"'
    return resp


@any_role
def materials(request):
    q = (request.GET.get("q") or "").strip()
    qs = Material.objects.all()
    if q:
        qs = qs.filter(Q(code__icontains=q) | Q(name__icontains=q) | Q(group__icontains=q))
    page = Paginator(qs, 50).get_page(request.GET.get("page"))
    groups = Material.objects.exclude(group="").values("group").annotate(n=Count("pk")).order_by("-n")[:12]
    return render(request, "masterdata/materials.html", {"page": page, "q": q, "groups": groups})


@designer
@require_POST
def demo(request):
    from twin.models import WarehouseModel

    wm = WarehouseModel.objects.filter(pk=request.POST.get("model") or 0).first()
    if wm is None:
        messages.error(request, "Wybierz model hali — dane demo rozkładają stan po jego regałach.")
        return redirect("masterdata:home")
    n_mat, log = services.load_demo(wm, user=request.user)
    messages.success(request, f"Dane demo: {n_mat} materiałów, {log.rows_ok} palet na stanie w „{wm.name}”.")
    return redirect("twin:warehouse_model_view", pk=wm.pk)
