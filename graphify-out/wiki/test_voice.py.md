# test_voice.py

> 18 nodes · cohesion 0.13

## Key Concepts

- **masterdata/services.py** (38 connections) — `web/masterdata/services.py`
- **import_file()** (13 connections) — `web/masterdata/services.py`
- **load_demo()** (10 connections) — `web/masterdata/services.py`
- **_parse_loc_code()** (7 connections) — `web/twin/shared.py`
- **_save_materials()** (6 connections) — `web/masterdata/services.py`
- **demo_dane.py** (5 connections) — `web/masterdata/management/commands/demo_dane.py`
- **Command** (4 connections) — `web/masterdata/management/commands/demo_dane.py`
- **_save_locations()** (4 connections) — `web/masterdata/services.py`
- **_save_stock()** (4 connections) — `web/masterdata/services.py`
- **parse_rows()** (3 connections) — `web/masterdata/importers.py`
- **_level_of()** (3 connections) — `web/masterdata/services.py`
- **missing_required()** (2 connections) — `web/masterdata/importers.py`
- **.handle()** (2 connections) — `web/masterdata/management/commands/demo_dane.py`
- **.add_arguments()** (1 connections) — `web/masterdata/management/commands/demo_dane.py`
- **BaseCommand** (1 connections)
- **Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…** (1 connections) — `web/masterdata/services.py`
- **Plik → ImportLog z raportem. ImportFileError, gdy pliku nie da się czytać albo…** (1 connections) — `web/masterdata/services.py`
- **B0-01-100A → (aisle, stack, col_code, col_idx, level); aisle zawiera strefę…** (1 connections) — `web/twin/shared.py`

## Relationships

- [masterdata/services.py](masterdata-services.py.md) (7 shared connections)
- [importers.py](importers.py.md) (6 shared connections)
- [scenario/services.py](scenario-services.py.md) (5 shared connections)
- [LayoutApiTests](LayoutApiTests.md) (4 shared connections)
- [test_ewm_service.py](test_ewm_service.py.md) (4 shared connections)
- [WarehouseTaskBatch](WarehouseTaskBatch.md) (3 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [shared.py](shared.py.md) (1 shared connections)
- [roles.py](roles.py.md) (1 shared connections)
- [ml/services.py](ml-services.py.md) (1 shared connections)
- [ewm_levels.py](ewm_levels.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)

## Source Files

- `web/masterdata/importers.py`
- `web/masterdata/management/commands/demo_dane.py`
- `web/masterdata/services.py`
- `web/twin/shared.py`

## Audit Trail

- EXTRACTED: 100 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*