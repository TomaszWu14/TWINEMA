"""Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do dnia projektowego)."""
from django.db import transaction

from . import importers, packaging
from .models import Carrier, ImportLog, Material, PalletClass, StockItem

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
    if kind == "materials":
        ok, extra = _resolve_refs(ok)
        n_rej += len(extra)
        rejects = (rejects + extra)[:importers.REJECT_SAMPLE]
    with transaction.atomic():
        log = ImportLog.objects.create(
            kind=kind, name=name[:200], uploaded_by=user if user and user.is_authenticated else None,
            rows_total=len(rows), rows_ok=len(ok), rows_rejected=n_rej, rejects=rejects,
            columns={f: headers[i] for f, i in cols.items()})
        if kind == "materials":
            _save_materials(log, ok, present=set(cols))
        else:
            {"locations": _save_locations, "stock": _save_stock}[kind](log, ok)
    return log


def _resolve_refs(rows):
    """Nazwy nośnika i klas → id (bez rozróżniania wielkości liter). Nieznana nazwa = odrzucony
    wiersz z powodem; pusta = brak (klasy dobierze `classify_materials`)."""
    refs = {"carrier": {c.name.lower(): c.pk for c in Carrier.objects.all()},
            "height_class": {c.label.lower(): c.pk for c in PalletClass.objects.filter(kind="height")},
            "weight_class": {c.label.lower(): c.pk for c in PalletClass.objects.filter(kind="weight")}}
    ok, rejects = [], []
    for r in rows:
        bad = None
        for f in importers.MATERIAL_REFS:
            name = r.pop(f, "")
            pk = refs[f].get(name.lower()) if name else None
            if name and pk is None:
                bad = f"{importers.LABELS[f]}: nie ma „{name}” w katalogu (Dane → Nośniki i klasy)"
            r[f"{f}_id"] = pk
        if bad:
            rejects.append({"row": None, "reason": f"{r['code']}: {bad}"})
        else:
            ok.append(r)
    return ok, rejects


def classify_materials(materials):
    """Uzupełnia brakujące klasy wysokości/wagi z wyliczonej palety (nośnik albo domyślny EUR).
    Działa na obiektach Material w pamięci — zapis robi wołający."""
    carriers = {c.pk: c.as_dict() for c in Carrier.objects.all()}
    default = next((c.pk for c in Carrier.objects.filter(is_default=True)), None)
    classes = {k: [(c.pk, c.limit) for c in PalletClass.objects.filter(kind=k)] for k in ("height", "weight")}
    for m in materials:
        d = m.as_dict()
        carrier = carriers.get(m.carrier_id or default)
        if m.height_class_id is None:
            m.height_class_id = packaging.classify(packaging.pallet_height_cm(d, carrier), classes["height"])
        if m.weight_class_id is None:
            m.weight_class_id = packaging.classify(packaging.pallet_weight_kg(d, carrier), classes["weight"])


def _save_materials(log, rows, present=None):
    """Upsert po kodzie — ostatni wiersz pliku wygrywa. Istniejącym materiałom zmieniamy tylko
    pola z kolumn obecnych w pliku (`present`) — import samej listy kodów i nazw nie zeruje
    opakowań ani flag."""
    by_code = {r["code"]: r for r in rows}
    existing = {m.code: m for m in Material.objects.filter(code__in=by_code)}
    fields = [f for f in next(iter(by_code.values()), {}) if f != "code"
              and (present is None or f.removesuffix("_id") in present)]
    new, upd = [], []
    for code, r in by_code.items():
        m = existing.get(code)
        if m is None:
            m = Material(**r)
            new.append(m)
        else:
            for f in fields:
                setattr(m, f, r[f])
            for f in ("height_class_id", "weight_class_id"):     # bez kolumny klasy → przelicz od nowa
                if f not in fields:
                    setattr(m, f, None)
            upd.append(m)
    classify_materials(new + upd)
    Material.objects.bulk_create(new, batch_size=BULK)
    Material.objects.bulk_update(upd, list(dict.fromkeys(fields + ["height_class_id", "weight_class_id"])),
                                 batch_size=BULK)


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


def _stock_pallets():
    """{materiał: palet na aktualnym stanie} — pozycja stanu = jedna paleta (jak w scenie 3D)."""
    from django.db.models import Count

    log = current_stock_log()
    return dict(log.stock_items.values_list("material_code").annotate(n=Count("pk"))) if log else {}


def cartons_per_pallet_distribution():
    """[(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na materiał bez stanu).
    → (rozkład, liczba materiałów, podstawa) albo None, gdy materiały nie mają przeliczników."""
    from collections import Counter

    cpp = {code: packaging.cartons_per_pallet({"cartons_per_layer": lay, "layers_per_pallet": n,
                                               "cartons_per_pallet": c})
           for code, lay, n, c in Material.objects.values_list(
               "code", "cartons_per_layer", "layers_per_pallet", "cartons_per_pallet")}
    cpp = {k: v for k, v in cpp.items() if v}
    if not cpp:
        return None
    weights = {m: w for m, w in _stock_pallets().items() if m in cpp}
    basis = "stan magazynu" if weights else "materiały"
    weights = weights or dict.fromkeys(cpp, 1)
    dist = Counter()
    for m, w in weights.items():
        dist[cpp[m]] += w
    return sorted(dist.items()), len(weights), basis


def cartons_per_pallet_hint():
    """Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą palet na
    aktualnym stanie (albo prosta średnia po materiałach, gdy brak stanu) → (wartość, liczba
    materiałów, podstawa) albo None."""
    d = cartons_per_pallet_distribution()
    return (packaging.weighted_cartons_per_pallet(d[0]), d[1], d[2]) if d else None


def stock_profile():
    """Palety na stanie per materiał z wagą i flagami stref specjalnych (dla reguł rozmieszczenia S3b):
    [{code, pallets, kg, heavy, adr, temp_controlled, oversize, high_value}]. `heavy` = najwyższa klasa wagi.
    Bez listy materiałów na zewnątrz — wynik trafia tylko do zagregowanych reguł."""
    stock = _stock_pallets()
    if not stock:
        return []
    weight_classes = sorted(PalletClass.objects.filter(kind="weight").values_list("pk", "limit"), key=lambda c: c[1])
    top = weight_classes[-1][0] if weight_classes else None
    objs = list(Carrier.objects.all())
    carriers = {c.pk: c.as_dict() for c in objs}
    default = next((carriers[c.pk] for c in objs if c.is_default), None)
    out = []
    for m in Material.objects.filter(code__in=stock.keys()):
        d = m.as_dict()
        kg = packaging.pallet_weight_kg(d, carriers.get(m.carrier_id) or default)
        wc = m.weight_class_id or packaging.classify(kg, weight_classes)
        out.append({"code": m.code, "pallets": stock[m.code], "kg": kg, "heavy": top is not None and wc == top,
                    "adr": m.adr, "temp_controlled": m.temp_controlled, "oversize": m.oversize,
                    "high_value": m.high_value})
    return out


def abc_from_history():
    """{materiał: A/B/C} z ostatniej segmentacji (Prognozy i ML); {} gdy nie liczona."""
    from ml.models import ModelRun

    run = ModelRun.objects.filter(kind="segmentation").first()
    return (run.result or {}).get("abc", {}) if run else {}


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
