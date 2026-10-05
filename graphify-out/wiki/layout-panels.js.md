# layout-panels.js

> 18 nodes · cohesion 0.14

## Key Concepts

- **addressing.py** (18 connections) — `web/twin/addressing.py`
- **parse_bay_numbers()** (10 connections) — `web/twin/addressing.py`
- **format_bay_numbers()** (6 connections) — `web/twin/addressing.py`
- **row_bay_numbers()** (6 connections) — `web/twin/addressing.py`
- **ParseTests** (6 connections) — `web/twin/tests/test_addressing.py`
- **_bay_locations()** (4 connections) — `web/twin/addressing.py`
- **make_code()** (4 connections) — `web/twin/addressing.py`
- **validate_bay_numbers()** (3 connections) — `web/twin/models.py`
- **.test_bay_numbers_ranges_round_trip()** (3 connections) — `web/twin/tests/test_addressing.py`
- **.test_row_numbers_default_and_truncation()** (3 connections) — `web/twin/tests/test_addressing.py`
- **.test_bay_numbers_invalid()** (2 connections) — `web/twin/tests/test_addressing.py`
- **.test_parse_code_with_half_and_lowercase()** (2 connections) — `web/twin/tests/test_addressing.py`
- **Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…** (1 connections) — `web/twin/addressing.py`
- **„10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError.** (1 connections) — `web/twin/addressing.py`
- **[10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers).** (1 connections) — `web/twin/addressing.py`
- **Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…** (1 connections) — `web/twin/addressing.py`
- **Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…** (1 connections) — `web/twin/addressing.py`
- **Numeracja gniazd rzędu: zakresy „10-47,50”.** (1 connections) — `web/twin/models.py`

## Relationships

- [test_addressing.py](test_addressing.py.md) (10 shared connections)
- [designer](designer.md) (6 shared connections)
- [LayoutApiTests](LayoutApiTests.md) (3 shared connections)
- [twin/models.py](twin-models.py.md) (3 shared connections)
- [scenario/models.py](scenario-models.py.md) (3 shared connections)
- [warehouse_variants.py](warehouse_variants.py.md) (2 shared connections)
- [SimViewTests](SimViewTests.md) (1 shared connections)
- [addressing.py](addressing.py.md) (1 shared connections)

## Source Files

- `web/twin/addressing.py`
- `web/twin/models.py`
- `web/twin/tests/test_addressing.py`

## Audit Trail

- EXTRACTED: 73 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*