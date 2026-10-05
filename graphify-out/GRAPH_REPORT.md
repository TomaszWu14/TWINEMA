# Graph Report - agent-adb24f25d7b6c79d9  (2026-10-05)

## Corpus Check
- 286 files · ~185,479 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3221 nodes · 6870 edges · 197 communities (155 shown, 42 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 213 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `126eb21d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- scenario/services.py
- day_demand
- test_equipment.py
- staffing.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- views_showcase.py
- site.py
- blender_scene.py
- masterdata/services.py
- analyze
- twinema_design_kit.py
- test_ewm_service.py
- ml/services.py
- test_design_sim_scene.py
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- StudioViewTests
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- test_warehouse_model_view.py
- Agent
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- detect
- ewm_service.py
- warehouse_variants.py
- test_fleet_catalog.py
- draft_script
- scenario/views.py
- day-timeline.js
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- scenario/models.py
- test_ewm_tasks_flow.py
- warehouse_blender.py
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- test_deck.py
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-hall.js
- DaneViewTests
- load_demo
- VoiceViewTests
- roles.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-editor.js
- bay_templates.py
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- test_ml.py
- test_design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- LoadAndViewTests
- test_addressing.py
- equipment/views.py
- SimViewTests
- icon
- warehouse_model.py
- studio/api.py
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- shared.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- design_catalog.py
- design_kpi.py
- addressing.py
- test_model_geometry.py
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- Equipment
- StudioConfig
- SimulationViewTests
- studio/migrations/0001_initial.py
- WarehouseTask
- SlotLocator
- layout-preview.js
- test_costs.py
- Scan
- 0003_render_montaz.py
- warehouse_layout.py
- blender_stock.py
- ScenarioConfig
- segmentation.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- VariantViewTests
- CostViewsTests
- layout-site.js
- test_ewm_detect.py
- ewm_tasks.py
- test_model_edit.py
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- CalibrationViewTests
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- site.test.mjs
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- capacity_at
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- params_for
- layout.py
- showcase.js
- 0006_prezentacja_3d.py
- masterdata/views.py
- LayoutError
- DockRoleTests
- LayoutEquipmentSaveTests
- 0006_sprzet_z_katalogu.py
- test_ewm_tasks_parser.py
- 0004_rola_doku_nosnosc.py
- _save
- EquipmentConfig
- 0002_klasy_systemowe.py
- 0004_stawki_domyslne.py
- equipment/migrations/0001_initial.py
- 0003_koszty.py
- 0004_flota_z_katalogu.py
- views_compare.py
- test_container_inbound.py
- parse_overrides
- parse_row
- PlayViewTests
- 0005_dni_szczytowe.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 45 edges
2. `SlotLocator` - 33 edges
3. `generate()` - 30 edges
4. `Scenario` - 29 edges
5. `simulate()` - 29 edges
6. `LayoutError` - 29 edges
7. `analyze()` - 29 edges
8. `rack_corners()` - 26 edges
9. `clean_layout()` - 26 edges
10. `Equipment` - 25 edges

## Surprising Connections (you probably didn't know these)
- `bottlenecks()` --calls--> `add()`  [INFERRED]
  web/scenario/sim/report.py → tools/blender/twinema_design_kit.py
- `start()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `load_variant()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py

## Import Cycles
- None detected.

## Communities (197 total, 42 thin omitted)

### Community 0 - "scenario/services.py"
Cohesion: 0.11
Nodes (26): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), {materiał: palet na aktualnym stanie} — pozycja stanu = jedna paleta (jak w…, [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, Palety na stanie per materiał z wagą i flagami stref specjalnych (dla reguł… (+18 more)

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (20): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+12 more)

### Community 2 - "test_equipment.py"
Cohesion: 0.15
Nodes (9): assign_classes(), pick_class(), Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co…, Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii…, Najmniejsza klasa systemowa danej kategorii regału (reach/vna), która sięga…, CatalogViewTests, TestCase, Katalog sprzętu (K1): czyste funkcje, klasy systemowe z migracji, dobór klasy… (+1 more)

### Community 3 - "staffing.py"
Cohesion: 0.19
Nodes (10): cutoff_risk(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy…, span(), staffing(), TestCase (+2 more)

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.11
Nodes (33): never_cache, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie. (+25 more)

### Community 7 - "simulate"
Cohesion: 0.10
Nodes (24): Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick() (+16 more)

### Community 8 - "twin/models.py"
Cohesion: 0.07
Nodes (25): Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka…, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Meta, WarehouseModelForm, Migration, Meta (+17 more)

### Community 9 - "views_showcase.py"
Cohesion: 0.07
Nodes (41): Prezentacja 3D dla zarządu (P1): model hali (+ działka) i opcjonalnie wynik…, Showcase, _cam(), clean_slides(), _fmt(), _hhmm(), kpi_cards(), ValueError (+33 more)

### Community 10 - "site.py"
Cohesion: 0.10
Nodes (32): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., _area_m2(), building_height(), building_rect(), check_site(), _dock_issues(), entry_point() (+24 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.11
Nodes (31): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), build_scene(), _carry(), _container_flow(), _Ctx (+23 more)

### Community 12 - "masterdata/services.py"
Cohesion: 0.11
Nodes (22): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów). (+14 more)

### Community 13 - "analyze"
Cohesion: 0.11
Nodes (25): analyze(), clean_layout(), column_list(), Dane z przeglądarki → znormalizowany layout. `feature_kinds` = dozwolone…, [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a…, CheckLayoutTests, CleanLayoutTests (+17 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.09
Nodes (14): LocationOverride, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master() (+6 more)

### Community 16 - "ml/services.py"
Cohesion: 0.20
Nodes (12): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail(), home(), _int(), any_role (+4 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.09
Nodes (15): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+7 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.17
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "importers.py"
Cohesion: 0.12
Nodes (31): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), missing_required(), norm() (+23 more)

### Community 20 - "scene-data.js"
Cohesion: 0.13
Nodes (23): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, EDGE_KINDS, effectiveQuality(), extents(), FAST_ABOVE, FLAT_KINDS (+15 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.15
Nodes (18): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+10 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 26 - "test_design_forecast.py"
Cohesion: 0.18
Nodes (15): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+7 more)

### Community 27 - "flow-player.js"
Cohesion: 0.11
Nodes (10): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _p, _s, SIM_KEYS, SKU_PALETTE (+2 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "test_warehouse_model_view.py"
Cohesion: 0.10
Nodes (11): InstancingGuardTests, TestCase, Regression: warehouse model 3D view used a non-existent `get_item` filter → 500., UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.… (+3 more)

### Community 30 - "Agent"
Cohesion: 0.10
Nodes (19): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+11 more)

### Community 31 - "design_day.py"
Cohesion: 0.10
Nodes (22): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok… (+14 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.17
Nodes (29): zoneColors(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected() (+21 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.07
Nodes (24): Następny krok, Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+16 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "detect"
Cohesion: 0.21
Nodes (15): format_bay_numbers(), letter_rank(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.19
Nodes (15): clean_elements(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "test_fleet_catalog.py"
Cohesion: 0.14
Nodes (11): move_minutes(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, fleet_from_catalog(), Sprzęt floty z katalogu (K1) → czas ruchu palety na tym layoucie: średnia droga…, Fleet, FleetCatalogTests (+3 more)

### Community 42 - "draft_script"
Cohesion: 0.17
Nodes (17): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+9 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.15
Nodes (24): has_role(), True dla superusera albo członka którejś z grup., _arrival_rows(), day_save(), _errors(), _fc(), _hours_rows(), _num() (+16 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.10
Nodes (44): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+36 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.15
Nodes (11): _aisle_m(), Najwęższy korytarz przy regale: po każdej stronie najbliższy równoległy regał…, _span(), _vna_racks(), EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w… (+3 more)

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/models.py"
Cohesion: 0.08
Nodes (31): Command, demo_zones(), atomic, BaseCommand, _r(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, check_triples() (+23 more)

### Community 49 - "test_ewm_tasks_flow.py"
Cohesion: 0.22
Nodes (8): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, _racks(), Zadania EWM (WT) w animacji przepływów: ruchy wózków z realnych zadań (agenci z…, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "warehouse_blender.py"
Cohesion: 0.07
Nodes (45): build_scene_for_model(), model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, default_start(), load_window() (+37 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (32): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+24 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "test_deck.py"
Cohesion: 0.11
Nodes (15): FPDF, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact(), BuildDeckTests (+7 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "layout-hall.js"
Cohesion: 0.27
Nodes (14): drawHall(), drawItem(), el(), render(), status(), CFG, deleteSelectedColumn(), drawColumns() (+6 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.17
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "load_demo"
Cohesion: 0.09
Nodes (16): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, Command, BaseCommand (+8 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.09
Nodes (19): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+11 more)

### Community 62 - "roles.py"
Cohesion: 0.10
Nodes (16): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), _cell(), any_role (+8 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-editor.js"
Cohesion: 0.14
Nodes (25): all(), applyIssues(), CFG, check(), fit(), fullscreen, history, load() (+17 more)

### Community 68 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.16
Nodes (6): EwmTasksPollingTests, MetaRefreshGuardTests, SimpleTestCase, TestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.08
Nodes (14): _dedupe(), FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), BlenderExportViewTests (+6 more)

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "SiteApiTests"
Cohesion: 0.27
Nodes (3): GeneratorSiteTests, TestCase, SiteApiTests

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "packaging.py"
Cohesion: 0.20
Nodes (16): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+8 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "test_ml.py"
Cohesion: 0.17
Nodes (6): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, MlRunTests, TestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.

### Community 77 - "test_design_calibration.py"
Cohesion: 0.16
Nodes (14): calibrate(), ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda)., Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu). (+6 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.08
Nodes (18): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne). (+10 more)

### Community 82 - "test_addressing.py"
Cohesion: 0.17
Nodes (12): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), codes(), ExpandModelTests, ExpandRowTests, ov() (+4 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.13
Nodes (16): _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list(), _check_range(), _curve() (+8 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.10
Nodes (28): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), hall_feature_kinds(), model_columns(), _parse_location_code(), Słupy hali jako elementy „column” (format hall_feature_dict + `height`) dla… (+20 more)

### Community 87 - "studio/api.py"
Cohesion: 0.09
Nodes (36): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+28 more)

### Community 95 - "shared.py"
Cohesion: 0.09
Nodes (29): load_groups(), load_inputs(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, hall_feature_dict(), Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze… (+21 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.15
Nodes (19): _geometry(), block_rows(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+11 more)

### Community 118 - "design_kpi.py"
Cohesion: 0.15
Nodes (18): anchor_count(), anchors(), _center(), compute_kpi(), equipment_capacity(), rack_to_element(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,… (+10 more)

### Community 119 - "addressing.py"
Cohesion: 0.16
Nodes (11): _bay_locations(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+3 more)

### Community 120 - "test_model_geometry.py"
Cohesion: 0.12
Nodes (15): floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +…, Najmniejsza hala (szer., głęb.) mieszcząca wszystkie regały + margines. (+7 more)

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.15
Nodes (20): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+12 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "Equipment"
Cohesion: 0.21
Nodes (7): CostRate, Equipment, Meta, (od, do) jako float; brak „do” = „od”; brak obu = None., Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, Meta, RateForm

### Community 128 - "SimulationViewTests"
Cohesion: 0.10
Nodes (16): _is_shelf(), capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet() (+8 more)

### Community 132 - "WarehouseTask"
Cohesion: 0.22
Nodes (4): Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 133 - "SlotLocator"
Cohesion: 0.13
Nodes (13): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., abc_by_hits(), build_pallets(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator (+5 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.31
Nodes (10): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+2 more)

### Community 135 - "test_costs.py"
Cohesion: 0.18
Nodes (10): compute(), _item(), mix_days(), Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy…, Dni w roku: [(typ dnia, liczba dni)]. Brak symulacji jednego typu → cały rok z…, rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf:…, _total(), ComputeTests (+2 more)

### Community 136 - "Scan"
Cohesion: 0.19
Nodes (6): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., Zwalnia plik (Windows nie skasuje otwartego pliku; openpyxl trzyma uchwyt)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.16
Nodes (23): rack_row(), _analyze(), equipment_catalog(), _image_size(), _layout(), _parse(), _md_role, _planner (+15 more)

### Community 139 - "blender_stock.py"
Cohesion: 0.11
Nodes (17): _level_of(), _deg(), _half(), load_stock_inputs(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo… (+9 more)

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 151 - "layout-site.js"
Cohesion: 0.20
Nodes (18): snap(), svgTransform(), setView(), viewCenter(), h(), num(), renderHall(), AREA_COLORS (+10 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 153 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), map_columns(), missing_required(), norm_header() (+5 more)

### Community 154 - "test_model_edit.py"
Cohesion: 0.15
Nodes (18): apply_zone_edit(), collisions(), fit_floor(), {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Pary regałów nachodzących na siebie o więcej niż `tol` m — obrócone prostokąty…, Hala co najmniej tak duża, jak obrys regałów (+ margines), nie mniejsza niż…, zone_summary() (+10 more)

### Community 156 - "generate"
Cohesion: 0.12
Nodes (16): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+8 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.20
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.13
Nodes (16): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, PlacesTests, SimpleTestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places(), peak_index() (+8 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.06
Nodes (46): Docks, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan(), Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny). (+38 more)

### Community 164 - "site.test.mjs"
Cohesion: 0.33
Nodes (5): ENTER_S, TRAVEL_S, sitePlan(), siteToHall(), SITE

### Community 167 - "capacity_at"
Cohesion: 0.33
Nodes (4): capacity_at(), Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, CatalogMathTests, PlainTestCase

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.24
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 172 - "layout.py"
Cohesion: 0.09
Nodes (29): skipUnless, bbox(), near_pairs(), overlap_depth(), rack_corners(), Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —… (+21 more)

### Community 173 - "showcase.js"
Cohesion: 0.16
Nodes (13): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS, camAt(), docksCam(), moveItem(), navigate(), pickCards() (+5 more)

### Community 176 - "masterdata/views.py"
Cohesion: 0.16
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), catalog(), _counts(), demo(), home(), log_detail(), materials() (+7 more)

### Community 177 - "LayoutError"
Cohesion: 0.14
Nodes (18): clean_columns(), clean_underlay(), _dock_role(), _id(), _int(), LayoutError, _num(), ValueError (+10 more)

### Community 182 - "DockRoleTests"
Cohesion: 0.19
Nodes (3): DockRoleTests, TestCase, SimS3bTests

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "test_ewm_tasks_parser.py"
Cohesion: 0.18
Nodes (9): _parse_dt(), parse_number(), parse_stamp(), _parse_time(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, → (datetime naiwny, czy_ma_czas) albo None; ValueError przy nieczytelnym…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,… (+1 more)

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "_save"
Cohesion: 0.43
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 197 - "views_compare.py"
Cohesion: 0.11
Nodes (20): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`. (+12 more)

### Community 199 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 201 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 202 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

## Knowledge Gaps
- **111 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+106 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **42 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `test_costs.py`, `views_showcase.py`, `masterdata/services.py`, `analyze`, `test_ewm_service.py`, `test_model_edit.py`, `generate`, `test_warehouse_model_view.py`, `views_play.py`, `BayTemplate`, `test_fleet_catalog.py`, `draft_script`, `scenario/views.py`, `masterdata/views.py`, `scenario/models.py`, `test_ewm_tasks_flow.py`, `studio/views.py`, `test_deck.py`, `load_demo`, `VoiceViewTests`, `roles.py`, `test_design_calibration.py`, `studio/models.py`, `studio/api.py`, `shared.py`, `test_model_geometry.py`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Why does `SlotLocator` connect `SlotLocator` to `warehouse_tasks.py`, `blender_stock.py`, `test_design_calibration.py`, `test_ewm_tasks_flow.py`, `warehouse_blender.py`, `TasksEndpointAndImportTests`, `shared.py`, `CalibrationViewTests`?**
  _High betweenness centrality (0.025) - this node is a cross-community bridge._
- **Why does `model_racks()` connect `warehouse_blender.py` to `scenario/services.py`, `views_compare.py`, `warehouse_tasks.py`, `warehouse_variants.py`, `test_fleet_catalog.py`, `blender_scene.py`, `masterdata/services.py`, `studio/views.py`, `test_model_edit.py`, `load_demo`, `shared.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _111 weakly-connected nodes found - possible documentation gaps or missing edges._