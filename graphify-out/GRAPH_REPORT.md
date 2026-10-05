# Graph Report - agent-ab80ddfde62265b49  (2026-10-05)

## Corpus Check
- 251 files · ~159,920 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2856 nodes · 5990 edges · 173 communities (140 shown, 33 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 210 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c0601508`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- shared.py
- scenario/models.py
- studio/api.py
- views_compare.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- design_kpi.py
- blender_scene.py
- Material
- check_layout
- design_catalog.py
- test_ewm_service.py
- ml/views.py
- test_design_sim_scene.py
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- test_addressing.py
- WarehouseTask
- flow-player.js
- TasksEndpointAndImportTests
- ViewFloatLocalizationTests
- Agent
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- test_design_compare.py
- warehouse_model_ewm.py
- warehouse_variants.py
- scenario/services.py
- StudioViewTests
- scenario/views.py
- day-timeline.js
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- Scenario
- test_ewm_tasks_flow.py
- Scan
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- test_deck.py
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-editor.js
- DaneViewTests
- sim/__init__.py
- VoiceViewTests
- roles.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- staffing.py
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- blender_stock.py
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- BlenderExportViewTests
- test_design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- LoadAndViewTests
- ewm_service.py
- segmentation.py
- SimViewTests
- icon
- warehouse_model.py
- DesignHubTests
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- warehouse_blender.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- map_columns
- test_ewm_tasks_parser.py
- .slot
- parse_overrides
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- BuildSceneTests
- StudioConfig
- generate
- studio/migrations/0001_initial.py
- test_ml.py
- SlotLocator
- layout-preview.js
- CalibrationViewTests
- 0003_render_montaz.py
- warehouse_layout.py
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- ewm_tasks.py
- rack_corners
- 0002_wydania_obsada.py
- GeometryUploadTests
- views_play.py
- report.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- 0002_opakowania_nosniki.py
- design_calibration.py
- blender_route.py
- MlRunTests
- fullscreen.test.mjs
- layout.py
- parse_row
- masterdata/views.py
- places_from_features
- simulate_plan
- test_layout_structure.py
- StockItem
- demo_stock
- safe_json
- analyze
- 0004_rola_doku_nosnosc.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 39 edges
2. `SlotLocator` - 33 edges
3. `simulate()` - 29 edges
4. `Scenario` - 26 edges
5. `generate()` - 25 edges
6. `Material` - 24 edges
7. `rack_corners()` - 24 edges
8. `build_scene()` - 24 edges
9. `clean_layout()` - 24 edges
10. `WarehouseModelRack` - 24 edges

## Surprising Connections (you probably didn't know these)
- `bottlenecks()` --calls--> `add()`  [INFERRED]
  web/scenario/sim/report.py → tools/blender/twinema_design_kit.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py
- `synthesize()` --references--> `Api`  [EXTRACTED]
  web/studio/tts.py → tools/render_worker.py
- `Meta` --uses--> `RenderJob`  [INFERRED]
  web/render/views.py → web/render/models.py
- `_geometry()` --calls--> `footprint()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py

## Import Cycles
- None detected.

## Communities (173 total, 33 thin omitted)

### Community 0 - "shared.py"
Cohesion: 0.09
Nodes (39): build_scene_for_model(), model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak). (+31 more)

### Community 1 - "scenario/models.py"
Cohesion: 0.11
Nodes (21): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+13 more)

### Community 2 - "studio/api.py"
Cohesion: 0.09
Nodes (36): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+28 more)

### Community 3 - "views_compare.py"
Cohesion: 0.14
Nodes (16): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`. (+8 more)

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.11
Nodes (31): never_cache, location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie., Zapis uploadu na dysk kawałkami → token (nazwa pliku) do podglądu i importu., Ścieżka pliku po tokenie z formularza — tylko nasz format nazwy (bez path… (+23 more)

### Community 7 - "simulate"
Cohesion: 0.09
Nodes (26): _is_shelf(), Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _vna_racks(), _Agent, _kpi(), Layout, _manh() (+18 more)

### Community 8 - "twin/models.py"
Cohesion: 0.06
Nodes (28): Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka…, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, Meta, WarehouseModelForm, Migration (+20 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.12
Nodes (20): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, import_file(), _level_of(), load_demo() (+12 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.10
Nodes (19): anchor_count(), anchors(), clean_elements(), compute_kpi(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, Punkty obsługi: doki/bramy/stanowiska z hali + stanowiska kompletacji z… (+11 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.11
Nodes (32): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), _aisle_m(), build_scene(), _carry(), _container_flow() (+24 more)

### Community 12 - "Material"
Cohesion: 0.08
Nodes (17): PureTestCase, Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów… (+9 more)

### Community 13 - "check_layout"
Cohesion: 0.20
Nodes (12): check_layout(), _column_corners(), _fname(), _name(), Lista problemów: error blokuje zapis, warning tylko ostrzega., CheckLayoutTests, CleanLayoutTests, codes() (+4 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.07
Nodes (46): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+38 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.07
Nodes (19): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., Master data for a single warehouse location., WarehouseLocationMaster, WarehouseLocationMasterBatch, load_sample() (+11 more)

### Community 16 - "ml/views.py"
Cohesion: 0.25
Nodes (8): detail(), home(), _int(), any_role, designer, require_POST, run(), segments_csv()

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.16
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "importers.py"
Cohesion: 0.18
Nodes (22): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+14 more)

### Community 20 - "scene-data.js"
Cohesion: 0.16
Nodes (20): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, effectiveQuality(), extents(), FAST_ABOVE, hallWalls(), hash01() (+12 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.13
Nodes (20): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+12 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "test_addressing.py"
Cohesion: 0.13
Nodes (16): expand_row(), parse_bay_numbers(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers() (+8 more)

### Community 26 - "WarehouseTask"
Cohesion: 0.12
Nodes (19): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+11 more)

### Community 27 - "flow-player.js"
Cohesion: 0.10
Nodes (12): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s (+4 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "ViewFloatLocalizationTests"
Cohesion: 0.10
Nodes (10): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "Agent"
Cohesion: 0.15
Nodes (9): Agent, Item, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT). (+1 more)

### Community 31 - "design_day.py"
Cohesion: 0.09
Nodes (26): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, _abc_xyz(), build_profile(), _groups(), load_groups(), _order_profile(), percentile() (+18 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.17
Nodes (30): makeBlock(), mode(), nextRackIds(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf() (+22 more)

### Community 34 - "kpi_facts"
Cohesion: 0.13
Nodes (15): estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy)., Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta. (+7 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.09
Nodes (18): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests (+10 more)

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "test_design_compare.py"
Cohesion: 0.19
Nodes (11): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+3 more)

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.14
Nodes (19): apply_proposal(), atomic, Zapis propozycji: nowe szablony, szablon domyślny + numeracja rzędów, wyjątki…, _compliance_xlsx(), _md_role, _planner, require_POST, „Wykryj z EWM” (podgląd propozycji → zapis) i raport zgodności modelu z EWM (+… (+11 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.24
Nodes (13): _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze…, Wiersze tabeli: wartości per wariant + oznaczenie najlepszej + różnica do…, _save_variant() (+5 more)

### Community 41 - "scenario/services.py"
Cohesion: 0.16
Nodes (17): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), {materiał: palet na aktualnym stanie} — pozycja stanu = jedna paleta (jak w…, [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, Palety na stanie per materiał z wagą i flagami stref specjalnych (dla reguł… (+9 more)

### Community 42 - "StudioViewTests"
Cohesion: 0.09
Nodes (22): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+14 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.15
Nodes (24): has_role(), True dla superusera albo członka którejś z grup., _arrival_rows(), day_save(), _errors(), _fc(), _hours_rows(), _num() (+16 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.19
Nodes (23): createDayPlayer(), fleet(), PARTS, buildTracks(), countersAt(), dayRange(), hashId(), hhmm() (+15 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.20
Nodes (7): EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "Scenario"
Cohesion: 0.08
Nodes (29): Command, demo_zones(), atomic, BaseCommand, _r(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, check_triples() (+21 more)

### Community 49 - "test_ewm_tasks_flow.py"
Cohesion: 0.24
Nodes (7): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, Zadania EWM (WT) w animacji przepływów: ruchy wózków z realnych zadań (agenci z…, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "layout-core.js"
Cohesion: 0.15
Nodes (14): axes(), BACK_GAP_M, bbox(), center(), corners(), History, rad(), rotateAround() (+6 more)

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (34): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+26 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "test_deck.py"
Cohesion: 0.11
Nodes (15): FPDF, PlainTestCase, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact() (+7 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "layout-editor.js"
Cohesion: 0.13
Nodes (25): svgTransform(), applyIssues(), CFG, check(), drawItem(), el(), fit(), fullscreen (+17 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.17
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "sim/__init__.py"
Cohesion: 0.19
Nodes (11): Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”). (+3 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.09
Nodes (19): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+11 more)

### Community 62 - "roles.py"
Cohesion: 0.07
Nodes (21): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), S1 — master data materiału: opakowania, nośniki, klasy, ABC, strefy specjalne,…, Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,… (+13 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-hall.js"
Cohesion: 0.29
Nodes (15): render(), status(), viewCenter(), CFG, deleteSelectedColumn(), drawColumns(), drawUnderlay(), el() (+7 more)

### Community 68 - "staffing.py"
Cohesion: 0.21
Nodes (11): cutoff_risk(), process_hours(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy…, span(), staffing() (+3 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.16
Nodes (6): EwmTasksPollingTests, MetaRefreshGuardTests, SimpleTestCase, TestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.17
Nodes (9): FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), SimpleTestCase, _rack() (+1 more)

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "blender_stock.py"
Cohesion: 0.20
Nodes (13): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), abc_by_hits(), load_stock_inputs() (+5 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "packaging.py"
Cohesion: 0.24
Nodes (14): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+6 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "test_design_calibration.py"
Cohesion: 0.17
Nodes (11): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund. (+3 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.08
Nodes (18): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne). (+10 more)

### Community 82 - "ewm_service.py"
Cohesion: 0.08
Nodes (40): expand_model(), format_bay_numbers(), letter_rank(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None. (+32 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.09
Nodes (32): active_master(), Aktywny (najnowszy) import mastera lokalizacji albo None., floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma). (+24 more)

### Community 95 - "warehouse_blender.py"
Cohesion: 0.14
Nodes (20): default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją). (+12 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - ".slot"
Cohesion: 0.24
Nodes (6): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.15
Nodes (20): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+12 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 128 - "generate"
Cohesion: 0.05
Nodes (26): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+18 more)

### Community 132 - "test_ml.py"
Cohesion: 0.33
Nodes (4): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.

### Community 133 - "SlotLocator"
Cohesion: 0.14
Nodes (11): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, BuildPalletsTests, ParseCodeTests (+3 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.27
Nodes (11): zoneColors(), S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode() (+3 more)

### Community 138 - "warehouse_layout.py"
Cohesion: 0.15
Nodes (24): column_list(), rack_row(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, hall_feature_kinds(), _analyze(), _image_size(), _layout(), _parse() (+16 more)

### Community 141 - "test_container_inbound.py"
Cohesion: 0.29
Nodes (6): ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 154 - "rack_corners"
Cohesion: 0.10
Nodes (28): bbox(), near_pairs(), overlap_depth(), rack_corners(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, apply_zone_edit(), _box() (+20 more)

### Community 158 - "views_play.py"
Cohesion: 0.09
Nodes (22): staging_side(), PlacesTests, PlayViewTests, SimpleTestCase, TestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places() (+14 more)

### Community 159 - "report.py"
Cohesion: 0.17
Nodes (16): aggregate(), bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, [kpi przebiegu] → {klucz: {mean, worst}}; najgorszy = P95 (gdy złe „dużo”) albo…, Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze… (+8 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.24
Nodes (9): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests (+1 more)

### Community 170 - "design_calibration.py"
Cohesion: 0.28
Nodes (6): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).

### Community 171 - "blender_route.py"
Cohesion: 0.15
Nodes (15): Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, _dedupe(), heading_deg(), path_length() (+7 more)

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 174 - "layout.py"
Cohesion: 0.28
Nodes (15): clean_columns(), clean_layout(), clean_underlay(), _dock_role(), _id(), _int(), LayoutError, _num() (+7 more)

### Community 175 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 176 - "masterdata/views.py"
Cohesion: 0.13
Nodes (19): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), abc_from_history(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., {materiał: A/B/C} z ostatniej segmentacji (Prognozy i ML); {} gdy nie liczona., catalog(), _counts() (+11 more)

### Community 177 - "places_from_features"
Cohesion: 0.19
Nodes (8): dock_role(), needed_roles(), places_from_features(), Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`)., features: dicty jak `twin.shared.hall_feature_dict` (kind, label, dock_role,…, PlacesTests, guess_dock_role(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…

### Community 178 - "simulate_plan"
Cohesion: 0.14
Nodes (11): Docks, Fleet, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan(), EngineTests (+3 more)

### Community 179 - "test_layout_structure.py"
Cohesion: 0.20
Nodes (8): ColumnTests, EquipmentAisleTests, FeatureKindTests, grid(), HeightTests, PerformanceTests, TestCase, E2b — konstrukcja hali w silniku layoutu: słupy, wysokość w świetle, drogi…

### Community 182 - "StockItem"
Cohesion: 0.17
Nodes (5): Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, DockRoleTests, TestCase, SimS3bTests

### Community 183 - "demo_stock"
Cohesion: 0.17
Nodes (11): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+3 more)

### Community 184 - "safe_json"
Cohesion: 0.28
Nodes (8): JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), _md_role, _planner, require_POST, warehouse_rack_type_delete(), warehouse_rack_type_form(), warehouse_rack_type_list()

### Community 186 - "analyze"
Cohesion: 0.17
Nodes (11): skipUnless, analyze(), height_kpi(), _issue(), rack_geom(), Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, Wysokość w świetle → maks. poziomów per strefa (przy wysokości poziomu jej…, (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a… (+3 more)

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

## Knowledge Gaps
- **89 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+84 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **33 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `shared.py`, `generate`, `studio/api.py`, `scenario/views.py`, `blender_route.py`, `test_design_calibration.py`, `test_ewm_service.py`, `masterdata/views.py`, `Scenario`, `studio/models.py`, `test_ewm_tasks_flow.py`, `studio/views.py`, `warehouse_model.py`, `test_deck.py`, `rack_corners`, `views_play.py`, `VoiceViewTests`, `roles.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.029) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _89 weakly-connected nodes found - possible documentation gaps or missing edges._