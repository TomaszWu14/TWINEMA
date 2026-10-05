# Graph Report - agent-adb24f25d7b6c79d9  (2026-10-05)

## Corpus Check
- 281 files · ~182,337 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3168 nodes · 6757 edges · 211 communities (159 shown, 52 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 205 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b1f09d01`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- safe_json
- day_demand
- Equipment
- views_compare.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- site.py
- blender_scene.py
- Material
- layout
- views_showcase.py
- test_ewm_service.py
- ml/views.py
- SimSceneTests
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- studio/models.py
- ForecastTests
- flow-player.js
- TasksEndpointAndImportTests
- ViewFloatLocalizationTests
- blender_route.py
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- bay_templates.py
- ParseTests
- addressing.py
- warehouse_model_ewm.py
- warehouse_variants.py
- Fleet
- draft_script
- studio/api.py
- day-timeline.js
- BayTemplateViewTests
- EquipmentAgentsTests
- middleware.py
- scenario/views.py
- ._scene
- _wt_window
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-editor.js
- DaneViewTests
- test_master_data.py
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-site.js
- staffing.py
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- BlenderExportViewTests
- test_design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- Presentation
- LoadAndViewTests
- test_addressing.py
- LayoutError
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
- shared.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- design_catalog.py
- test_design_variants.py
- CompliancePureTests
- test_model_geometry.py
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- Scan
- StudioConfig
- test_design_compare.py
- studio/migrations/0001_initial.py
- _save
- SlotLocator
- layout-preview.js
- map_columns
- parse_stamp
- 0003_render_montaz.py
- warehouse_layout.py
- .slot
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- StudioViewTests
- WarehouseTask
- design_calibration.py
- test_ewm_detect.py
- test_ewm_tasks_parser.py
- test_model_edit.py
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- segmentation.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- build_pallets
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- PlayViewTests
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- ewm_tasks.py
- build_plan
- showcase.js
- check_placement
- ShowcaseViewTests
- masterdata/views.py
- scenario/services.py
- simulate_plan
- demo_hall
- CompareViewTests
- context_processors.py
- DockRoleTests
- Command
- parse_row
- 0006_sprzet_z_katalogu.py
- layout.py
- 0004_rola_doku_nosnosc.py
- warehouse_variant_edit.py
- EquipmentConfig
- 0002_klasy_systemowe.py
- EwmViewsTests
- equipment/migrations/0001_initial.py
- RackRuleAndOverrideTests
- 0004_flota_z_katalogu.py
- test_dane.py
- WarehouseLocationMasterBatch
- test_design_sim.py
- BuildSceneTests
- site.test.mjs
- GeometryUploadTests
- compare.py
- OutboundTests
- BayTemplate
- CalibrationViewTests
- SimSceneViewTests
- LayoutEquipmentSaveTests
- ClampTests
- 0005_prezentacja_3d.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 44 edges
2. `SlotLocator` - 33 edges
3. `generate()` - 30 edges
4. `simulate()` - 29 edges
5. `LayoutError` - 29 edges
6. `analyze()` - 29 edges
7. `Scenario` - 28 edges
8. `rack_corners()` - 26 edges
9. `clean_layout()` - 26 edges
10. `build_scene()` - 24 edges

## Surprising Connections (you probably didn't know these)
- `bottlenecks()` --calls--> `add()`  [INFERRED]
  web/scenario/sim/report.py → tools/blender/twinema_design_kit.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py
- `synthesize()` --references--> `Api`  [EXTRACTED]
  web/studio/tts.py → tools/render_worker.py
- `Meta` --uses--> `WarehouseModel`  [INFERRED]
  web/twin/forms.py → web/twin/models.py
- `_geometry()` --calls--> `footprint()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py

## Import Cycles
- None detected.

## Communities (211 total, 52 thin omitted)

### Community 0 - "safe_json"
Cohesion: 0.14
Nodes (14): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), ewm_tasks_profile(), _planner (+6 more)

### Community 1 - "day_demand"
Cohesion: 0.15
Nodes (18): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+10 more)

### Community 2 - "Equipment"
Cohesion: 0.06
Nodes (31): capacity_at(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, Equipment, Meta, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, assign_classes(), pick_class() (+23 more)

### Community 3 - "views_compare.py"
Cohesion: 0.21
Nodes (15): compare_columns(), results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook() (+7 more)

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
Nodes (27): Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., _smallest(), Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh() (+19 more)

### Community 8 - "twin/models.py"
Cohesion: 0.05
Nodes (34): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Flota scenariusza z katalogu sprzętu (K1): czas ruchu palety z parametrów,…, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,…, Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, Lektor w aplikacji: nagrywanie po akceptacji, cache po hashu, statusy, SRT. TTS… (+26 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.09
Nodes (26): missing_required(), Command, BaseCommand, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, current_stock_log(), import_file(), _level_of() (+18 more)

### Community 10 - "site.py"
Cohesion: 0.09
Nodes (36): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., guess_dock_role(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…, _area_m2(), building_height(), building_rect(), check_site() (+28 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.10
Nodes (35): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), _aisle_m(), build_scene(), _carry(), _container_flow() (+27 more)

### Community 12 - "Material"
Cohesion: 0.17
Nodes (9): Carrier, Material, Meta, PalletClass, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna., Klasa wysokości albo wagi palety z towarem (np. do 1,4 m / do 600 kg) — do…, Materiał (SKU): hierarchia sztuka → karton → paleta, nośnik, klasy, ABC i…, MaterialForm (+1 more)

### Community 13 - "layout"
Cohesion: 0.12
Nodes (18): CheckLayoutTests, CleanLayoutTests, codes(), LayoutEquipmentTests, PlainTestCase, Layout z katalogiem sprzętu (K1): alejka Ast z katalogu, wysokość podnoszenia,…, feat(), layout() (+10 more)

### Community 14 - "views_showcase.py"
Cohesion: 0.08
Nodes (39): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, Prezentacja 3D dla zarządu (P1): model hali (+ działka) i opcjonalnie wynik…, ScenarioRun, Showcase, _cam(), clean_slides(), _fmt(), _hhmm() (+31 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.20
Nodes (9): Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master(), TestCase, Warstwa ORM części 1: zapis „Wykryj z EWM” + raport zgodności na syntetycznej… (+1 more)

### Community 16 - "ml/views.py"
Cohesion: 0.17
Nodes (11): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, detail(), home(), _int(), any_role, designer (+3 more)

### Community 17 - "SimSceneTests"
Cohesion: 0.11
Nodes (11): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+3 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.17
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "importers.py"
Cohesion: 0.16
Nodes (24): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+16 more)

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

### Community 25 - "studio/models.py"
Cohesion: 0.07
Nodes (23): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., create(), delete(), jobs(), Meta (+15 more)

### Community 26 - "ForecastTests"
Cohesion: 0.29
Nodes (5): _daily(), ForecastTests, SimpleTestCase, Dni robocze (pn–pt) z wykładniczym wzrostem `growth_year` rocznie; weekendy…, _total()

### Community 27 - "flow-player.js"
Cohesion: 0.11
Nodes (10): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _p, _s, SIM_KEYS, SKU_PALETTE (+2 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "ViewFloatLocalizationTests"
Cohesion: 0.10
Nodes (10): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "blender_route.py"
Cohesion: 0.10
Nodes (21): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+13 more)

### Community 31 - "design_day.py"
Cohesion: 0.07
Nodes (40): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), abc_by_hits(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, _abc_xyz(), build_profile() (+32 more)

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

### Community 36 - "bay_templates.py"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "addressing.py"
Cohesion: 0.12
Nodes (24): _bay_locations(), format_bay_numbers(), letter_rank(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None. (+16 more)

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.11
Nodes (25): apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), atomic, [(kod, typ EWM, wysokość mm, udźwig kg)] z mastera — tylko kody stref modelu., Propozycja „Wykryj z EWM” dla rzędów modelu (nic nie zapisuje)., Zapis propozycji: nowe szablony, szablon domyślny + numeracja rzędów, wyjątki… (+17 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.17
Nodes (17): clean_elements(), rack_to_element(), Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,…, Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, _comparison(), _get(), _md_role, _planner (+9 more)

### Community 41 - "Fleet"
Cohesion: 0.24
Nodes (4): Fleet, FleetCatalogTests, FleetChargingTests, TestCase

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "studio/api.py"
Cohesion: 0.18
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.10
Nodes (44): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+36 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "EquipmentAgentsTests"
Cohesion: 0.22
Nodes (6): EquipmentAgentsTests, SimpleTestCase, _rack(), Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.07
Nodes (48): has_role(), True dla superusera albo członka którejś z grup., Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, check_triples(), InboundStream, Meta, OutboundStream, Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz… (+40 more)

### Community 49 - "._scene"
Cohesion: 0.24
Nodes (5): SimpleTestCase, _racks(), ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "_wt_window"
Cohesion: 0.22
Nodes (9): default_start(), load_window(), parse_start(), Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, _clamped_float(), ?wt=<id>|latest — wózki z importu zadań EWM w oknie ?wt_from (czas lokalny,… (+1 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (31): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+23 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "build_deck"
Cohesion: 0.11
Nodes (14): FPDF, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact(), BuildDeckTests (+6 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.18
Nodes (4): override_settings, TestCase, RenderMontageTests, _voice()

### Community 58 - "layout-editor.js"
Cohesion: 0.12
Nodes (33): svgTransform(), all(), applyIssues(), CFG, check(), drawHall(), drawItem(), el() (+25 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.18
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "test_master_data.py"
Cohesion: 0.13
Nodes (11): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+3 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "views_sim.py"
Cohesion: 0.18
Nodes (10): _cell(), any_role, designer, require_POST, Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI,…, Wynik zapisany w ScenarioRun → grupy karty KPI (#21), wykres osi czasu i wąskie…, Zdarzenia przebiegu reprezentatywnego dla odtwarzacza 3D (format:…, run_events() (+2 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-site.js"
Cohesion: 0.17
Nodes (24): snap(), setView(), status(), viewCenter(), CFG, deleteSelectedColumn(), drawColumns(), drawUnderlay() (+16 more)

### Community 68 - "staffing.py"
Cohesion: 0.21
Nodes (10): cutoff_risk(), process_hours(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy…, staffing(), Wydania, paczki, zwroty, obsada i cut-off — liczby policzone ręcznie. (+2 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.15
Nodes (10): _dedupe(), FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), SimpleTestCase (+2 more)

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
Cohesion: 0.21
Nodes (16): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+8 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "test_design_calibration.py"
Cohesion: 0.20
Nodes (10): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund. (+2 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "Presentation"
Cohesion: 0.17
Nodes (9): Meta, MontageJob, Presentation, Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →…, Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między…, VoiceTrack, Meta, presentation_list() (+1 more)

### Community 82 - "test_addressing.py"
Cohesion: 0.14
Nodes (16): expand_row(), parse_bay_numbers(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers() (+8 more)

### Community 83 - "LayoutError"
Cohesion: 0.16
Nodes (18): clean_columns(), clean_layout(), clean_underlay(), _dock_role(), _id(), _int(), LayoutError, _num() (+10 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.12
Nodes (23): active_master(), Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis…, Aktywny (najnowszy) import mastera lokalizacji albo None., Meta, WarehouseModelForm, _parse_location_code(), Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., B0-01-300A → (zone, rack, bay, level_letter, level_num). (+15 more)

### Community 95 - "shared.py"
Cohesion: 0.08
Nodes (48): build_scene_for_model(), model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), load_stock_inputs() (+40 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.07
Nodes (46): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+38 more)

### Community 118 - "test_design_variants.py"
Cohesion: 0.13
Nodes (12): compute_kpi(), equipment_capacity(), (punkt przed frontem boku/kanału, liczba miejsc paletowych) dla elementów…, Nominalna wydajność sprzętu wg katalogu, zsumowana per rodzaj elementu., storage_faces(), travel_stats(), _el(), KpiTests (+4 more)

### Community 120 - "test_model_geometry.py"
Cohesion: 0.16
Nodes (13): floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +…, Najmniejsza hala (szer., głęb.) mieszcząca wszystkie regały + margines. (+5 more)

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.22
Nodes (11): cartons_for(), Kartonów na paletę z kontenera: z rozkładu master daty [(kartonów, waga)] —…, CartonsTests, codes(), CompareTests, PlacementTests, TestCase, rack() (+3 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 128 - "test_design_compare.py"
Cohesion: 0.19
Nodes (11): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+3 more)

### Community 132 - "_save"
Cohesion: 0.31
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 133 - "SlotLocator"
Cohesion: 0.25
Nodes (6): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…, SlotLocatorTests

### Community 134 - "layout-preview.js"
Cohesion: 0.31
Nodes (10): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+2 more)

### Community 135 - "map_columns"
Cohesion: 0.26
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 136 - "parse_stamp"
Cohesion: 0.26
Nodes (6): _parse_dt(), parse_stamp(), _parse_time(), → (datetime naiwny, czy_ma_czas) albo None; ValueError przy nieczytelnym…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., ValueParsingTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.15
Nodes (25): column_list(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, hall_feature_kinds(), _analyze(), equipment_catalog(), _image_size(), _layout(), _parse() (+17 more)

### Community 139 - ".slot"
Cohesion: 0.20
Nodes (8): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 141 - "test_container_inbound.py"
Cohesion: 0.23
Nodes (7): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 150 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 151 - "design_calibration.py"
Cohesion: 0.18
Nodes (11): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją)., resolve_moves(), window_source(), _manh() (+3 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.19
Nodes (12): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, plan_for_model(), Rozwinięty plan modelu → (rzędy, miejsca, duplikaty)., DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of() (+4 more)

### Community 153 - "test_ewm_tasks_parser.py"
Cohesion: 0.25
Nodes (7): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase, Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…

### Community 154 - "test_model_edit.py"
Cohesion: 0.31
Nodes (6): apply_zone_edit(), Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, _copy(), ModelEditTests, SimpleTestCase, Edycja wariantu hali blokami (plan 2026-10-02, etap 4).

### Community 156 - "generate"
Cohesion: 0.12
Nodes (16): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+8 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.11
Nodes (23): PlacesTests, SimpleTestCase, bottleneck_focus(), layout_places(), peak_index(), any_role, Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu…, features: dicty `hall_feature_dict` (+ słupy), floor {width, depth} → miejsca… (+15 more)

### Community 159 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.12
Nodes (23): Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”). (+15 more)

### Community 164 - "build_pallets"
Cohesion: 0.20
Nodes (5): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "ewm_tasks.py"
Cohesion: 0.22
Nodes (10): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), Parser eksportu zadań magazynowych EWM (WT) z monitora magazynu (/SCWM/MON) →…, Wiersze pliku jako listy wartości — strumieniowo, bez ładowania całości do… (+2 more)

### Community 172 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 173 - "showcase.js"
Cohesion: 0.16
Nodes (13): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS, camAt(), docksCam(), moveItem(), navigate(), pickCards() (+5 more)

### Community 174 - "check_placement"
Cohesion: 0.29
Nodes (9): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+1 more)

### Community 176 - "masterdata/views.py"
Cohesion: 0.14
Nodes (17): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), abc_from_history(), {materiał: A/B/C} z ostatniej segmentacji (Prognozy i ML); {} gdy nie liczona., catalog(), _counts(), demo(), home() (+9 more)

### Community 177 - "scenario/services.py"
Cohesion: 0.10
Nodes (26): move_minutes(), Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą… (+18 more)

### Community 178 - "simulate_plan"
Cohesion: 0.15
Nodes (13): Docks, Pool, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan(), Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min., Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}., run_report() (+5 more)

### Community 179 - "demo_hall"
Cohesion: 0.22
Nodes (8): Command, demo_hall(), demo_zones(), atomic, BaseCommand, _r(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…

### Community 182 - "DockRoleTests"
Cohesion: 0.21
Nodes (3): DockRoleTests, TestCase, SimS3bTests

### Community 184 - "parse_row"
Cohesion: 0.29
Nodes (5): parse_number(), parse_row(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "layout.py"
Cohesion: 0.10
Nodes (33): skipUnless, bbox(), near_pairs(), overlap_depth(), rack_corners(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, analyze() (+25 more)

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "warehouse_variant_edit.py"
Cohesion: 0.23
Nodes (10): fit_floor(), {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Hala co najmniej tak duża, jak obrys regałów (+ margines), nie mniejsza niż…, zone_summary(), _num(), _md_role, require_POST, Kopia modelu (hala ze słupami i podkładem, regały, elementy hali) — „przyszły… (+2 more)

### Community 193 - "RackRuleAndOverrideTests"
Cohesion: 0.27
Nodes (4): BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests

### Community 197 - "test_dane.py"
Cohesion: 0.28
Nodes (5): ImportLog, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka…, S3b w aplikacji: rola doku (pole, migracja, generator, edytor, symulacja),…

### Community 198 - "WarehouseLocationMasterBatch"
Cohesion: 0.22
Nodes (6): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch, Ekrany „Wykryj z EWM” (podgląd → zapis) i „Zgodność z EWM” (+ XLSX), z rolami.

### Community 199 - "test_design_sim.py"
Cohesion: 0.22
Nodes (3): TestCase, Symulacja dnia projektowego na hali z generatora (plan 2026-10-02, etap 3a)., SimulationViewTests

### Community 201 - "site.test.mjs"
Cohesion: 0.33
Nodes (5): ENTER_S, TRAVEL_S, sitePlan(), siteToHall(), SITE

## Knowledge Gaps
- **109 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+104 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **52 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `test_dane.py`, `masterdata/services.py`, `test_design_calibration.py`, `views_showcase.py`, `test_ewm_service.py`, `masterdata/views.py`, `scenario/views.py`, `layout`, `studio/views.py`, `warehouse_model.py`, `blender_route.py`, `test_model_geometry.py`, `studio/models.py`, `test_model_edit.py`, `generate`, `views_sim.py`, `shared.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `WarehouseTaskBatch` connect `shared.py` to `warehouse_tasks.py`, `map_columns`, `test_design_sim.py`, `simulate`, `ml/views.py`, `WarehouseTask`, `DesignHubTests`, `ForecastTests`, `design_day.py`?**
  _High betweenness centrality (0.032) - this node is a cross-community bridge._
- **Why does `TasksEndpointAndImportTests` connect `TasksEndpointAndImportTests` to `twin/models.py`, `SlotLocator`?**
  _High betweenness centrality (0.022) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `LayoutError` (e.g. with `CheckLayoutTests` and `CleanLayoutTests`) actually correct?**
  _`LayoutError` has 12 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _109 weakly-connected nodes found - possible documentation gaps or missing edges._