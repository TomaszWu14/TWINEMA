# calibrate

> 15 nodes · cohesion 0.21

## Key Concepts

- **calibrate()** (13 connections) — `web/twin/design_calibration.py`
- **CalibrationTests** (11 connections) — `web/twin/tests/test_design_calibration.py`
- **_rows()** (7 connections) — `web/twin/tests/test_design_calibration.py`
- **ideal_cycle()** (6 connections) — `web/twin/design_calibration.py`
- **.test_ratio_tracks_real_pace()** (4 connections) — `web/twin/tests/test_design_calibration.py`
- **.test_breaks_longer_than_limit_are_not_cycles()** (3 connections) — `web/twin/tests/test_design_calibration.py`
- **.test_pairs_only_within_one_resource()** (3 connections) — `web/twin/tests/test_design_calibration.py`
- **.test_unmapped_locations_are_counted()** (3 connections) — `web/twin/tests/test_design_calibration.py`
- **.test_ideal_cycle_includes_lift()** (2 connections) — `web/twin/tests/test_design_calibration.py`
- **.test_picking_is_its_own_group()** (2 connections) — `web/twin/tests/test_design_calibration.py`
- **Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…** (1 connections) — `web/twin/design_calibration.py`
- **rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu).** (1 connections) — `web/twin/design_calibration.py`
- **SimpleTestCase** (1 connections)
- **Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund.** (1 connections) — `web/twin/tests/test_design_calibration.py`
- **Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie.** (1 connections) — `web/twin/tests/test_design_calibration.py`

## Relationships

- [TWINEMA — zakres i plan](TWINEMA_%E2%80%94_zakres_i_plan.md) (4 shared connections)
- [twin/models.py](twin-models.py.md) (4 shared connections)
- [warehouse_blender.py](warehouse_blender.py.md) (2 shared connections)
- [CalibrationViewTests](CalibrationViewTests.md) (2 shared connections)
- [resolve_moves](resolve_moves.md) (1 shared connections)
- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (1 shared connections)
- [simulate](simulate.md) (1 shared connections)

## Source Files

- `web/twin/design_calibration.py`
- `web/twin/tests/test_design_calibration.py`

## Audit Trail

- EXTRACTED: 58 (98%)
- INFERRED: 1 (2%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*