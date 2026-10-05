# Graph Report - agent-a61b257e81c7e3b37  (2026-10-05)

## Corpus Check
- 245 files · ~150,737 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2774 nodes · 5781 edges · 179 communities (139 shown, 40 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 209 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a87fa542`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- shared.py
- day_demand
- studio/api.py
- sim/__init__.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- design_kpi.py
- blender_scene.py
- Material
- test_layout.py
- design_catalog.py
- test_ewm_service.py
- blender_stock.py
- SimSceneTests
- twinema_design_kit.py
- importers.py
- Scenario
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- test_addressing.py
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- test_warehouse_model_view.py
- blender_route.py
- design_day.py
- forecast.py
- layout-panels.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- test_placement.py
- warehouse_compare.py
- warehouse_model_ewm.py
- warehouse_variants.py
- masterdata/views.py
- draft_script
- views_compare.py
- scene-builder.js
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- scenario/views.py
- resolve_moves
- Scan
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-editor.js
- test_dane.py
- StockItem
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- CompliancePureTests
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- EwmViewsTests
- design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- roles.py
- LoadAndViewTests
- ewm_service.py
- segmentation.py
- SimViewTests
- icon
- rack_corners
- DesignHubTests
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- warehouse_design_sim.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- map_columns
- test_ewm_tasks_parser.py
- render/views.py
- parse_overrides
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- clean_layout
- 0002_pole_odkladcze.py
- twinema_render.py
- SlotLocator
- StudioConfig
- generate
- studio/migrations/0001_initial.py
- scenario/models.py
- StudioViewTests
- warehouse_layout.py
- demo_stock
- layout-preview.js
- 0003_render_montaz.py
- test_ml.py
- ScenarioDay
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- ewm_tasks.py
- ProfileTests
- test_model_edit.py
- test_ewm_detect.py
- GeometryUploadTests
- model_edit.py
- 0002_wydania_obsada.py
- PackagingTests
- HourField
- test_sim.py
- report.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- build_plan
- 0003_domyslne_nosniki_klasy.py
- simulate_plan
- 0002_opakowania_nosniki.py
- VariantViewTests
- layout.py
- 0004_rola_doku_nosnosc.py
- params_for
- test_ewm_tasks_refresh.py
- warehouse_blender.py
- SimulationViewTests
- fullscreen.test.mjs
- BlenderExportViewTests
- parse_row
- BuildSceneTests
- context_processors.py
- Command

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 38 edges
2. `SlotLocator` - 33 edges
3. `simulate()` - 29 edges
4. `Scenario` - 25 edges
5. `generate()` - 25 edges
6. `Material` - 24 edges
7. `rack_corners()` - 24 edges
8. `build_scene()` - 24 edges
9. `clean_layout()` - 24 edges
10. `WarehouseModelRack` - 24 edges

## Surprising Connections (you probably didn't know these)
- `bottlenecks()` --calls--> `add()`  [INFERRED]
  web/scenario/sim/report.py → tools/blender/twinema_design_kit.py
- `_geometry()` --calls--> `footprint()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `_geometry()` --calls--> `height()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `start()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `load_variant()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py

## Import Cycles
- None detected.

## Communities (179 total, 40 thin omitted)

### Community 0 - "shared.py"
Cohesion: 0.08
Nodes (38): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., letter_level(), Sam numer poziomu 1..5 (``default`` dla nieznanej litery)., Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), model_columns(), _parse_location_code() (+30 more)

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (21): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+13 more)

### Community 2 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 3 - "sim/__init__.py"
Cohesion: 0.11
Nodes (19): Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many() (+11 more)

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
Cohesion: 0.10
Nodes (26): Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick() (+18 more)

### Community 8 - "twin/models.py"
Cohesion: 0.08
Nodes (22): demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Meta, WarehouseModelForm, Migration, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, WarehouseHallFeature (+14 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.09
Nodes (30): Command, BaseCommand, [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), current_stock_log(), load_demo() (+22 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.14
Nodes (20): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), compute_kpi(), equipment_capacity(), rack_to_element() (+12 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.13
Nodes (29): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), build_scene(), _carry(), _container_flow(), _Ctx (+21 more)

### Community 12 - "Material"
Cohesion: 0.10
Nodes (16): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna. (+8 more)

### Community 13 - "test_layout.py"
Cohesion: 0.25
Nodes (10): check_layout(), Lista problemów: error blokuje zapis, warning tylko ostrzega., CheckLayoutTests, CleanLayoutTests, codes(), feat(), layout(), TestCase (+2 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.17
Nodes (18): block_rows(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji). (+10 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.11
Nodes (18): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, LocationOverride, Meta, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, One import of location master data (height, volume, weight, type)., Master data for a single warehouse location. (+10 more)

### Community 16 - "blender_stock.py"
Cohesion: 0.11
Nodes (20): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+12 more)

### Community 17 - "SimSceneTests"
Cohesion: 0.11
Nodes (11): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+3 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.18
Nodes (22): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+14 more)

### Community 19 - "importers.py"
Cohesion: 0.06
Nodes (40): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), missing_required(), norm() (+32 more)

### Community 20 - "Scenario"
Cohesion: 0.13
Nodes (7): Meta, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, Scenario, ScenarioRun, S3b w aplikacji: rola doku (pole, migracja, generator, edytor, symulacja),…, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,…

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.14
Nodes (19): NamedTuple, _level_of(), code_slot(), is_hall_a(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+11 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "test_addressing.py"
Cohesion: 0.17
Nodes (12): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), codes(), ExpandModelTests, ExpandRowTests, ov() (+4 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.18
Nodes (15): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+7 more)

### Community 27 - "flow-player.js"
Cohesion: 0.10
Nodes (12): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s (+4 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "test_warehouse_model_view.py"
Cohesion: 0.12
Nodes (10): InstancingGuardTests, TestCase, Regression: warehouse model 3D view used a non-existent `get_item` filter → 500., UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "blender_route.py"
Cohesion: 0.10
Nodes (20): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+12 more)

### Community 31 - "design_day.py"
Cohesion: 0.14
Nodes (19): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+11 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.20
Nodes (26): addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected(), rotateSelected() (+18 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "test_placement.py"
Cohesion: 0.16
Nodes (18): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+10 more)

### Community 38 - "warehouse_compare.py"
Cohesion: 0.19
Nodes (14): _is_shelf(), capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet() (+6 more)

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.13
Nodes (21): active_master(), apply_proposal(), atomic, Aktywny (najnowszy) import mastera lokalizacji albo None., Zapis propozycji: nowe szablony, szablon domyślny + numeracja rzędów, wyjątki…, _compliance_xlsx(), _md_role, _planner (+13 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.15
Nodes (16): clean_elements(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, _comparison(), _get(), _md_role, _planner (+8 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.19
Nodes (13): catalog(), _counts(), demo(), home(), log_detail(), materials(), any_role, designer (+5 more)

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "views_compare.py"
Cohesion: 0.14
Nodes (16): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`. (+8 more)

### Community 44 - "scene-builder.js"
Cohesion: 0.13
Nodes (23): zoneColors(), concreteTex(), createViewer(), hex2rgb(), _lblCache, mkTex(), noise(), signTex() (+15 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.15
Nodes (11): _aisle_m(), Najwęższy korytarz przy regale: po każdej stronie najbliższy równoległy regał…, _span(), _vna_racks(), EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w… (+3 more)

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.15
Nodes (26): has_role(), True dla superusera albo członka którejś z grup., _arrival_rows(), day_save(), DayProfileForm, _errors(), _fc(), _hours_rows() (+18 more)

### Community 49 - "resolve_moves"
Cohesion: 0.14
Nodes (9): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), CalibrationViewTests, TestCase, SimpleTestCase, _racks(), ResolveMovesTests, _row() (+1 more)

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (18): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+10 more)

### Community 52 - "studio/views.py"
Cohesion: 0.11
Nodes (36): Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między…, VoiceTrack, approve(), deck_pdf(), _draft_or_back(), film_file(), Meta, model_kpi() (+28 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "build_deck"
Cohesion: 0.11
Nodes (14): FPDF, PlainTestCase, build_deck(), _Deck, Deck PDF prezentacji (czysty Python — fpdf2, bez Django i bez bazy). Strony…, „Etykieta: wartość.” → (etykieta, wartość) do kafla; zdanie bez dwukropka →…, slides: [{"label": "Przelot nad halą", "text": kwestia, "image": bytes PNG albo…, split_fact() (+6 more)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.18
Nodes (4): override_settings, TestCase, RenderMontageTests, _voice()

### Community 58 - "layout-editor.js"
Cohesion: 0.15
Nodes (22): applyIssues(), CFG, check(), fit(), fullscreen, history, load(), payload() (+14 more)

### Community 59 - "test_dane.py"
Cohesion: 0.13
Nodes (10): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase, Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka… (+2 more)

### Community 60 - "StockItem"
Cohesion: 0.17
Nodes (5): Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, DockRoleTests, TestCase, SimS3bTests

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "views_sim.py"
Cohesion: 0.16
Nodes (12): InForm, _cell(), any_role, designer, require_POST, Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI,…, Wynik zapisany w ScenarioRun → grupy karty KPI (#21), wykres osi czasu i wąskie…, Zdarzenia przebiegu reprezentatywnego dla odtwarzacza 3D (format:… (+4 more)

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
Cohesion: 0.23
Nodes (18): round(), drawItem(), el(), render(), status(), viewCenter(), CFG, deleteSelectedColumn() (+10 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.15
Nodes (10): _dedupe(), FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), SimpleTestCase (+2 more)

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "packaging.py"
Cohesion: 0.20
Nodes (16): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+8 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "design_calibration.py"
Cohesion: 0.13
Nodes (15): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., calibrate(), ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda). (+7 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "roles.py"
Cohesion: 0.07
Nodes (19): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., Meta, MontageJob (+11 more)

### Community 82 - "ewm_service.py"
Cohesion: 0.09
Nodes (32): expand_model(), format_bay_numbers(), letter_rank(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None. (+24 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "rack_corners"
Cohesion: 0.16
Nodes (12): rack_corners(), _column_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma). (+4 more)

### Community 95 - "warehouse_design_sim.py"
Cohesion: 0.14
Nodes (22): load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., load_inputs(), Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, design_hub(), _planner (+14 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - "render/views.py"
Cohesion: 0.18
Nodes (12): create(), delete(), jobs(), Meta, any_role, designer, require_POST, Stan zleceń w toku — strona odpytuje i przeładowuje się, gdy coś się zmieni. (+4 more)

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.17
Nodes (11): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Scenariusz (niezależny od layoutu), Składowanie i kompletacja, TWINEMA — założenia master daty i scenariuszy (+3 more)

### Community 123 - "clean_layout"
Cohesion: 0.13
Nodes (24): clean_columns(), clean_layout(), clean_underlay(), column_list(), _dock_role(), _id(), _int(), LayoutError (+16 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "SlotLocator"
Cohesion: 0.09
Nodes (19): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., build_pallets(), _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).… (+11 more)

### Community 128 - "generate"
Cohesion: 0.07
Nodes (22): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+14 more)

### Community 132 - "scenario/models.py"
Cohesion: 0.11
Nodes (20): Command, demo_zones(), atomic, BaseCommand, _r(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, check_triples() (+12 more)

### Community 133 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 134 - "warehouse_layout.py"
Cohesion: 0.17
Nodes (21): hall_feature_kinds(), _analyze(), _image_size(), _layout(), _parse(), _md_role, _planner, require_POST (+13 more)

### Community 135 - "demo_stock"
Cohesion: 0.17
Nodes (11): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+3 more)

### Community 136 - "layout-preview.js"
Cohesion: 0.33
Nodes (9): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+1 more)

### Community 138 - "test_ml.py"
Cohesion: 0.25
Nodes (3): MlRunTests, TestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany.

### Community 141 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 151 - "test_model_edit.py"
Cohesion: 0.17
Nodes (5): TestCase, Edycja wariantu hali blokami (plan 2026-10-02, etap 4)., Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests, _save()

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.27
Nodes (8): DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip…, Propozycja → obiekty jak z bazy → rozwinięte kody per przejście., rows_of()

### Community 154 - "model_edit.py"
Cohesion: 0.10
Nodes (25): bbox(), near_pairs(), overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, apply_zone_edit(), _box(), collisions() (+17 more)

### Community 158 - "test_sim.py"
Cohesion: 0.14
Nodes (15): dock_role(), needed_roles(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`)., features: dicty jak `twin.shared.hall_feature_dict` (kind, label, dock_role,…, Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)., staging_side() (+7 more)

### Community 159 - "report.py"
Cohesion: 0.15
Nodes (16): aggregate(), bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, [kpi przebiegu] → {klucz: {mean, worst}}; najgorszy = P95 (gdy złe „dużo”) albo…, Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze… (+8 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 164 - "simulate_plan"
Cohesion: 0.19
Nodes (10): cartons_for(), Docks, Fleet, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Kartonów na paletę z kontenera: z rozkładu master daty [(kartonów, waga)] —…, simulate_plan(), EngineTests, plan() (+2 more)

### Community 167 - "layout.py"
Cohesion: 0.15
Nodes (14): skipUnless, analyze(), _fname(), height_kpi(), _issue(), _name(), rack_geom(), Layout hali dla edytora planu (czysty Python — bez Django, testowalny bez… (+6 more)

### Community 168 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 169 - "params_for"
Cohesion: 0.21
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 170 - "test_ewm_tasks_refresh.py"
Cohesion: 0.40
Nodes (3): MetaRefreshGuardTests, SimpleTestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…

### Community 171 - "warehouse_blender.py"
Cohesion: 0.10
Nodes (33): build_scene_for_model(), model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, default_start(), load_window() (+25 more)

### Community 172 - "SimulationViewTests"
Cohesion: 0.09
Nodes (10): load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H., Meta, WarehouseTask, ForecastViewTests, TestCase, TestCase, TestCase (+2 more)

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 175 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

## Knowledge Gaps
- **83 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+78 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **40 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `shared.py`, `generate`, `scenario/models.py`, `BayTemplate`, `masterdata/views.py`, `test_ewm_service.py`, `roles.py`, `scenario/views.py`, `Scenario`, `studio/views.py`, `render/views.py`, `test_model_edit.py`, `test_dane.py`, `test_warehouse_model_view.py`, `views_sim.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.038) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _83 weakly-connected nodes found - possible documentation gaps or missing edges._