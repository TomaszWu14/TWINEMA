# design_catalog.py

> 24 nodes · cohesion 0.15

## Key Concepts

- **design_catalog.py** (20 connections) — `web/twin/design_catalog.py`
- **params_for()** (19 connections) — `web/twin/design_catalog.py`
- **test_design_catalog.py** (13 connections) — `web/twin/tests/test_design_catalog.py`
- **footprint()** (11 connections) — `web/twin/design_catalog.py`
- **variant_summary()** (9 connections) — `web/twin/design_catalog.py`
- **block_rows()** (8 connections) — `web/twin/design_catalog.py`
- **element_summary()** (7 connections) — `web/twin/design_catalog.py`
- **CatalogTests** (7 connections) — `web/twin/tests/test_design_catalog.py`
- **pallet_positions()** (5 connections) — `web/twin/design_catalog.py`
- **_geometry()** (4 connections) — `tools/blender/twinema_design_kit.py`
- **_span()** (4 connections) — `web/twin/design_catalog.py`
- **height()** (3 connections) — `web/twin/design_catalog.py`
- **.test_every_element_has_label_and_params()** (3 connections) — `web/twin/tests/test_design_catalog.py`
- **.test_footprint()** (3 connections) — `web/twin/tests/test_design_catalog.py`
- **.test_pallet_positions()** (3 connections) — `web/twin/tests/test_design_catalog.py`
- **.test_block_rows_pairs_and_equipment_aisle()** (2 connections) — `web/twin/tests/test_design_catalog.py`
- **.test_params_override_and_unknown()** (2 connections) — `web/twin/tests/test_design_catalog.py`
- **Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…** (1 connections) — `web/twin/design_catalog.py`
- **Liczba miejsc paletowych elementu (0 dla transportu/kompletacji).** (1 connections) — `web/twin/design_catalog.py`
- **Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…** (1 connections) — `web/twin/design_catalog.py`
- **Rzut obrysu elementu na oś: (początek, koniec) [m]; along=True → szerokość.** (1 connections) — `web/twin/design_catalog.py`
- **Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze).** (1 connections) — `web/twin/design_catalog.py`
- **(szerokość wzdłuż osi elementu, głębokość) [m].** (1 connections) — `web/twin/design_catalog.py`
- **Katalog elementów projektowania wariantów — twin/design_catalog.py (wspólny z…** (1 connections) — `web/twin/tests/test_design_catalog.py`

## Relationships

- [test_dane.py](test_dane.py.md) (13 shared connections)
- [design_kpi.py](design_kpi.py.md) (11 shared connections)
- [twinema_design_kit.py](twinema_design_kit.py.md) (9 shared connections)
- [kpi_facts](kpi_facts.md) (1 shared connections)
- [day_demand](day_demand.md) (1 shared connections)
- [GeneratorTests](GeneratorTests.md) (1 shared connections)

## Source Files

- `tools/blender/twinema_design_kit.py`
- `web/twin/design_catalog.py`
- `web/twin/tests/test_design_catalog.py`

## Audit Trail

- EXTRACTED: 130 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*