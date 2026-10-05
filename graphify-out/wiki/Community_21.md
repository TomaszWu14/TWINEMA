# Community 21

> 22 nodes · cohesion 0.13

## Key Concepts

- **masterdata/services.py** (25 connections) — `web/masterdata/services.py`
- **import_file()** (12 connections) — `web/masterdata/services.py`
- **load_demo()** (10 connections) — `web/masterdata/services.py`
- **_parse_loc_code()** (7 connections) — `web/twin/shared.py`
- **demo_dane.py** (5 connections) — `web/masterdata/management/commands/demo_dane.py`
- **_save_materials()** (5 connections) — `web/masterdata/services.py`
- **Command** (4 connections) — `web/masterdata/management/commands/demo_dane.py`
- **_save_locations()** (4 connections) — `web/masterdata/services.py`
- **_save_stock()** (4 connections) — `web/masterdata/services.py`
- **parse_rows()** (3 connections) — `web/masterdata/importers.py`
- **_level_of()** (3 connections) — `web/masterdata/services.py`
- **missing_required()** (2 connections) — `web/masterdata/importers.py`
- **.handle()** (2 connections) — `web/masterdata/management/commands/demo_dane.py`
- **→ (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…** (1 connections) — `web/masterdata/importers.py`
- **.add_arguments()** (1 connections) — `web/masterdata/management/commands/demo_dane.py`
- **BaseCommand** (1 connections)
- **Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…** (1 connections) — `web/masterdata/services.py`
- **Materiały demo (upsert) + import stanów demo dla modelu hali → (liczba…** (1 connections) — `web/masterdata/services.py`
- **Plik → ImportLog z raportem. ImportFileError, gdy pliku nie da się czytać albo…** (1 connections) — `web/masterdata/services.py`
- **Upsert po kodzie — ostatni wiersz pliku wygrywa.** (1 connections) — `web/masterdata/services.py`
- **Nowy aktywny master lokalizacji (poprzednie nieaktywne) — ten sam, którego…** (1 connections) — `web/masterdata/services.py`
- **B0-01-100A → (aisle, stack, col_code, col_idx, level); aisle zawiera strefę…** (1 connections) — `web/twin/shared.py`

## Relationships

- [Community 9](Community_9.md) (7 shared connections)
- [Community 19](Community_19.md) (6 shared connections)
- [Community 41](Community_41.md) (5 shared connections)
- [Community 66](Community_66.md) (4 shared connections)
- [Community 15](Community_15.md) (4 shared connections)
- [Community 0](Community_0.md) (3 shared connections)
- [Community 8](Community_8.md) (2 shared connections)
- [Community 86](Community_86.md) (1 shared connections)
- [Community 62](Community_62.md) (1 shared connections)
- [Community 22](Community_22.md) (1 shared connections)
- [Community 74](Community_74.md) (1 shared connections)

## Source Files

- `web/masterdata/importers.py`
- `web/masterdata/management/commands/demo_dane.py`
- `web/masterdata/services.py`
- `web/twin/shared.py`

## Audit Trail

- EXTRACTED: 87 (92%)
- INFERRED: 8 (8%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*