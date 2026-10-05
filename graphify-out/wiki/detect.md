# detect

> 16 nodes · cohesion 0.21

## Key Concepts

- **detect()** (14 connections) — `web/twin/ewm_detect.py`
- **ewm_detect.py** (13 connections) — `web/twin/ewm_detect.py`
- **parse_code()** (8 connections) — `web/twin/addressing.py`
- **letter_rank()** (5 connections) — `web/twin/addressing.py`
- **_grid()** (5 connections) — `web/twin/ewm_detect.py`
- **_shape()** (5 connections) — `web/twin/ewm_detect.py`
- **_distance()** (4 connections) — `web/twin/ewm_detect.py`
- **_template_sig()** (3 connections) — `web/twin/ewm_detect.py`
- **_new_template()** (2 connections) — `web/twin/ewm_detect.py`
- **Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu.** (1 connections) — `web/twin/addressing.py`
- **Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None.** (1 connections) — `web/twin/addressing.py`
- **„Wykryj z EWM”: kody lokalizacji z mastera → propozycja szablonów gniazd, reguł…** (1 connections) — `web/twin/ewm_detect.py`
- **k pozycji × [(litera, split)] → zbiór komórek (pozycja, litera, połówka).** (1 connections) — `web/twin/ewm_detect.py`
- **Komórki gniazda → (sygnatura obrysu, czy siatka regularna). Sygnatura = (k,…** (1 connections) — `web/twin/ewm_detect.py`
- **Liczba różnic gniazda od szablonu: brakujące + nadmiarowe komórki + inne typy…** (1 connections) — `web/twin/ewm_detect.py`
- **rows: [{"zone", "rack_id", "n_bays"}]; master: [(kod, typ_ewm, wysokość_mm,…** (1 connections) — `web/twin/ewm_detect.py`

## Relationships

- [addressing.py](addressing.py.md) (6 shared connections)
- [test_ewm_detect.py](test_ewm_detect.py.md) (4 shared connections)
- [model_racks](model_racks.md) (3 shared connections)
- [ewm_tasks.py](ewm_tasks.py.md) (2 shared connections)
- [test_addressing.py](test_addressing.py.md) (1 shared connections)

## Source Files

- `web/twin/addressing.py`
- `web/twin/ewm_detect.py`

## Audit Trail

- EXTRACTED: 64 (97%)
- INFERRED: 2 (3%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*