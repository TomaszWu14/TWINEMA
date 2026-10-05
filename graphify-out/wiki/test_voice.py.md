# test_voice.py

> 17 nodes · cohesion 0.13

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

## Relationships

- [test_showcase.py](test_showcase.py.md) (7 shared connections)
- [masterdata/importers.py](masterdata-importers.py.md) (6 shared connections)
- [test_fleet_catalog.py](test_fleet_catalog.py.md) (5 shared connections)
- [LayoutApiTests](LayoutApiTests.md) (4 shared connections)
- [test_ewm_service.py](test_ewm_service.py.md) (4 shared connections)
- [test_sim.py](test_sim.py.md) (3 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [shared.py](shared.py.md) (1 shared connections)
- [views_sim.py](views_sim.py.md) (1 shared connections)
- [ml/services.py](ml-services.py.md) (1 shared connections)
- [equipment/importers.py](equipment-importers.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)

## Source Files

- `web/masterdata/importers.py`
- `web/masterdata/management/commands/demo_dane.py`
- `web/masterdata/services.py`
- `web/twin/shared.py`

## Audit Trail

- EXTRACTED: 99 (94%)
- INFERRED: 6 (6%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*