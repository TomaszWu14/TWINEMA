# blender_stock.py

> 10 nodes · cohesion 0.24

## Key Concepts

- **.slot()** (11 connections) — `web/twin/blender_stock.py`
- **parse_code()** (6 connections) — `web/twin/locations.py`
- **._parse()** (5 connections) — `web/twin/blender_stock.py`
- **_half()** (3 connections) — `web/twin/blender_stock.py`
- **.__init__()** (3 connections) — `web/twin/blender_stock.py`
- **.rack_and_bay()** (3 connections) — `web/twin/blender_stock.py`
- **_deg()** (2 connections) — `web/twin/blender_stock.py`
- **1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…** (1 connections) — `web/twin/blender_stock.py`
- **dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…** (1 connections) — `web/twin/blender_stock.py`
- **Kod → (zone, rack_id, bay, col_idx, level) albo None.** (1 connections) — `web/twin/locations.py`

## Relationships

- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (4 shared connections)
- [blender_route.py](blender_route.py.md) (3 shared connections)
- [ewm_levels.py](ewm_levels.py.md) (2 shared connections)
- [design_kpi.py](design_kpi.py.md) (1 shared connections)
- [TWINEMA — zakres i plan](TWINEMA_%E2%80%94_zakres_i_plan.md) (1 shared connections)
- [Scenario](Scenario.md) (1 shared connections)
- [test_ewm_service.py](test_ewm_service.py.md) (1 shared connections)
- [test_voice.py](test_voice.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_stock.py`
- `web/twin/locations.py`

## Audit Trail

- EXTRACTED: 36 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*