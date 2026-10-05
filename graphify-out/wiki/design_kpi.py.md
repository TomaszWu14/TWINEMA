# design_kpi.py

> 29 nodes · cohesion 0.12

## Key Concepts

- **design_kpi.py** (20 connections) — `web/twin/design_kpi.py`
- **test_design_variants.py** (16 connections) — `web/twin/tests/test_design_variants.py`
- **rack_axes()** (15 connections) — `web/twin/blender_route.py`
- **compute_kpi()** (12 connections) — `web/twin/design_kpi.py`
- **rack_to_element()** (11 connections) — `web/twin/design_kpi.py`
- **_el()** (9 connections) — `web/twin/tests/test_design_variants.py`
- **travel_stats()** (8 connections) — `web/twin/design_kpi.py`
- **KpiTests** (8 connections) — `web/twin/tests/test_design_variants.py`
- **clean_elements()** (7 connections) — `web/twin/design_kpi.py`
- **storage_faces()** (6 connections) — `web/twin/design_kpi.py`
- **anchors()** (5 connections) — `web/twin/design_kpi.py`
- **equipment_capacity()** (5 connections) — `web/twin/design_kpi.py`
- **anchor_count()** (3 connections) — `web/twin/design_kpi.py`
- **_center()** (3 connections) — `web/twin/design_kpi.py`
- **.test_amr_station_is_an_anchor_and_no_anchor_falls_back()** (3 connections) — `web/twin/tests/test_design_variants.py`
- **.test_equipment_capacity_sums()** (3 connections) — `web/twin/tests/test_design_variants.py`
- **.test_rack_to_element()** (3 connections) — `web/twin/tests/test_design_variants.py`
- **.test_storage_faces_per_bay()** (3 connections) — `web/twin/tests/test_design_variants.py`
- **.test_travel_near_rack_beats_far_and_a_zone_is_shorter()** (3 connections) — `web/twin/tests/test_design_variants.py`
- **.test_clean_elements()** (2 connections) — `web/twin/tests/test_design_variants.py`
- **(u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali.** (1 connections) — `web/twin/blender_route.py`
- **Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…** (1 connections) — `web/twin/design_kpi.py`
- **Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,…** (1 connections) — `web/twin/design_kpi.py`
- **Punkty obsługi: doki/bramy/stanowiska z hali + stanowiska kompletacji z…** (1 connections) — `web/twin/design_kpi.py`
- **Liczba rzeczywistych punktów obsługi (0 → droga liczona od przodu hali).** (1 connections) — `web/twin/design_kpi.py`
- *... and 4 more nodes in this community*

## Relationships

- [design_catalog.py](design_catalog.py.md) (11 shared connections)
- [shared.py](shared.py.md) (7 shared connections)
- [ml/services.py](ml-services.py.md) (4 shared connections)
- [blender_scene.py](blender_scene.py.md) (3 shared connections)
- [kpi_facts](kpi_facts.md) (2 shared connections)
- [twin/models.py](twin-models.py.md) (2 shared connections)
- [twinema_design_kit.py](twinema_design_kit.py.md) (1 shared connections)
- [ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie](ADR-0001-_Kopia_kodu_modelowania_magazynu%2C_nie_przeniesienie.md) (1 shared connections)
- [TWINEMA — zakres i plan](TWINEMA_%E2%80%94_zakres_i_plan.md) (1 shared connections)
- [views_sim.py](views_sim.py.md) (1 shared connections)
- [packaging.py](packaging.py.md) (1 shared connections)
- [engine.py](engine.py.md) (1 shared connections)

## Source Files

- `web/twin/blender_route.py`
- `web/twin/design_kpi.py`
- `web/twin/tests/test_design_variants.py`

## Audit Trail

- EXTRACTED: 154 (100%)
- INFERRED: 0 (0%)
- AMBIGUOUS: 0 (0%)

---

*Part of the graphify knowledge wiki. See [index](index.md) to navigate.*