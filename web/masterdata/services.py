"""Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do dnia projektowego)."""
from django.db import transaction

from . import importers
from .models import ImportLog, Material, StockItem

BULK = 5000


def _level_of(code):
    from twin.shared import _parse_loc_code
    parsed = _parse_loc_code(code)
    return parsed[4] if parsed else None


def import_file(kind, name, data, user=None):
    """Plik → ImportLog z raportem. ImportFileError, gdy pliku nie da się czytać albo brak
    wymaganych kolumn (nic nie zapisujemy). Odrzucone wiersze nie blokują reszty."""
    headers, rows = importers.read_table(name, data)
    cols = importers.map_columns(kind, headers)
    missing = importers.missing_required(kind, cols)
    if missing:
        raise importers.ImportFileError("Brak wymaganych kolumn: " + ", ".join(missing)
                                        + ". Pobierz wzór pliku z ekranu Dane.")
    kw = {"level_of": _level_of} if kind == "locations" else {}
    ok, rejects, n_rej = importers.parse_rows(kind, rows, cols, **kw)
    with transaction.atomic():
        log = ImportLog.objects.create(
            kind=kind, name=name[:200], uploaded_by=user if user and user.is_authenticated else None,
            rows_total=len(rows), rows_ok=len(ok), rows_rejected=n_rej, rejects=rejects,
            columns={f: headers[i] for f, i in cols.items()})
        {"materials": _save_materials, "locations": _save_locations, "stock": _save_stock}[kind](log, ok)
    return log


def _save_materials(log, rows):
    """Upsert po kodzie — ostatni wiersz pliku wygrywa."""
    by_code = {r["code"]: r for r in rows}
    existing = {m.code: m for m in Material.objects.filter(code__in=by_code)}
    fields = [f for f in importers.ALIASES["materials"] if f != "code"]
    new, upd = [], []
    for code, r in by_code.items():
        m = existing.get(code)
        if m is None:
            new.append(Material(**r))
        else:
            for f in fields:
                setattr(m, f, r[f])
            upd.append(m)
    Material.objects.bulk_create(new, batch_size=BULK)
    Material.objects.bulk_update(upd, fields, batch_size=BULK)


def _save_locations(log, rows):
    """Nowy aktywny master lokalizacji (poprzednie nieaktywne) — ten sam, którego używa
    „Wykryj z EWM”, zgodność i poziomy palet w scenie."""
    from twin.models import WarehouseLocationMaster, WarehouseLocationMasterBatch
    by_code = {r["location_code"]: r for r in rows}
    WarehouseLocationMasterBatch.objects.filter(is_active=True).update(is_active=False)
    batch = WarehouseLocationMasterBatch.objects.create(name=log.name, location_count=len(by_code), is_active=True)
    WarehouseLocationMaster.objects.bulk_create(
        [WarehouseLocationMaster(batch=batch, **r) for r in by_code.values()], batch_size=BULK)


def _save_stock(log, rows):
    StockItem.objects.bulk_create([StockItem(log=log, **r) for r in rows], batch_size=BULK)


# ── Odczyt dla bliźniaka ─────────────────────────────────────────────────────

def current_stock_log():
    """Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)."""
    return ImportLog.objects.filter(kind="stock").first()


def stock_for_scene(log=None):
    """Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry, qty, unit."""
    log = log or current_stock_log()
    if log is None:
        return []
    items = list(log.stock_items.values_list("location_code", "material_code", "qty", "unit", "hu", "lot", "expiry"))
    names = dict(Material.objects.filter(code__in={i[1] for i in items}).values_list("code", "name"))
    return [{"location": loc, "sku": mat, "name": names.get(mat, "")[:80], "qty": qty, "unit": unit,
             "hu": hu or f"{loc}/{mat}", "lot": lot, "expiry": exp}
            for loc, mat, qty, unit, hu, lot, exp in items]


def groups_for(materials):
    """{materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.
    Dopasowanie po kodzie, potem po kodzie bez wiodących zer (eksporty WMS bywają z zerami)."""
    if not Material.objects.exists():
        return None
    materials = list(materials)
    stripped = {m: m.strip().lstrip("0") for m in materials}
    qs = Material.objects.exclude(group="")
    groups = dict(qs.filter(code__in=set(materials) | set(stripped.values())).values_list("code", "group"))
    return {m: groups.get(m) or groups.get(stripped[m]) for m in materials}


def load_demo(wm, fill=0.7, user=None):
    """Materiały demo (upsert) + import stanów demo dla modelu hali → (liczba materiałów, ImportLog)."""
    from twin.blender_scene import model_racks

    from .demo import demo_materials, demo_stock

    fill = min(max(fill, 0.05), 1.0)
    mats = demo_materials()
    stock = demo_stock(model_racks(wm), fill=fill)
    with transaction.atomic():
        _save_materials(None, mats)
        log = ImportLog.objects.create(kind="stock", name=f"Demo — stany ({wm.name})"[:200],
                                       uploaded_by=user if user and user.is_authenticated else None,
                                       rows_total=len(stock), rows_ok=len(stock))
        _save_stock(log, stock)
    return len(mats), log
