# Graph Report - agent-a10077732524ddf48  (2026-10-05)

## Corpus Check
- 238 files · ~145,490 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2681 nodes · 5552 edges · 181 communities (146 shown, 35 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 200 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f04e7b88`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- warehouse_model.py
- scenario/models.py
- studio/api.py
- simulate_plan
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
- ml/views.py
- test_design_sim_scene.py
- twinema_design_kit.py
- importers.py
- roles.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- test_addressing.py
- ml/services.py
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
- ParseTests
- test_design_compare.py
- ewm_service.py
- warehouse_variants.py
- masterdata/views.py
- StudioViewTests
- designer
- scene-builder.js
- test_bay_template_views.py
- _inside
- middleware.py
- scenario/views.py
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
- test_dane.py
- sim/__init__.py
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- addressing.py
- EwmTasksPollingTests
- FloorGrid
- test_flow_player.py
- bay_templates.py
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- EwmViewsTests
- test_design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- LoadAndViewTests
- detect
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
- shared.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- map_columns
- test_ewm_tasks_parser.py
- SlotLocator
- parse_overrides
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- layout.py
- 0002_pole_odkladcze.py
- twinema_render.py
- .slot
- StudioConfig
- GeneratorTests
- studio/migrations/0001_initial.py
- ScenarioDay
- build_pallets
- warehouse_layout.py
- demo_stock
- CompareViewTests
- 0003_render_montaz.py
- WarehouseLocationMasterBatch
- demo_scenariusz.py
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- ewm_tasks.py
- generate
- VariantEditViewTests
- test_ewm_detect.py
- GeneratorViewTests
- test_model_edit.py
- 0002_wydania_obsada.py
- CalibrationViewTests
- _save
- scenario/services.py
- report.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- build_plan
- 0003_domyslne_nosniki_klasy.py
- test_sim.py
- 0002_opakowania_nosniki.py
- VariantViewTests
- test_layout_editor_js.py
- staffing
- params_for
- design_calibration.py
- _wt_window
- WarehouseTask
- fullscreen.test.mjs
- BlenderExportViewTests
- parse_row
- BuildSceneTests
- column_list
- BottleneckTests
- cartons_per_pallet_hint
- BlenderImportGuardTests

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 37 edges
2. `SlotLocator` - 33 edges
3. `simulate()` - 29 edges
4. `Scenario` - 24 edges
5. `build_scene()` - 24 edges
6. `WarehouseModelRack` - 24 edges
7. `generate()` - 23 edges
8. `Scan` - 23 edges
9. `clean_layout()` - 23 edges
10. `check_layout()` - 23 edges

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

## Communities (181 total, 35 thin omitted)

### Community 0 - "warehouse_model.py"
Cohesion: 0.09
Nodes (31): hall_feature_kinds(), model_columns(), _parse_location_code(), Słupy hali jako elementy „column” (format hall_feature_dict + `height`) dla…, Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, B0-01-300A → (zone, rack, bay, level_letter, level_num)., safe_json() (+23 more)

### Community 1 - "scenario/models.py"
Cohesion: 0.11
Nodes (22): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+14 more)

### Community 2 - "studio/api.py"
Cohesion: 0.07
Nodes (43): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+35 more)

### Community 3 - "simulate_plan"
Cohesion: 0.14
Nodes (12): Docks, Fleet, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, simulate_plan(), cutoff_risk() (+4 more)

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
Nodes (24): Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick() (+16 more)

### Community 8 - "twin/models.py"
Cohesion: 0.08
Nodes (22): demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Meta, WarehouseModelForm, Migration, Meta (+14 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.12
Nodes (20): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, import_file(), _level_of(), load_demo() (+12 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.13
Nodes (20): anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity(), rack_to_element(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i… (+12 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.09
Nodes (39): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), rack_axes(), rack_point(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _aisle_m() (+31 more)

### Community 12 - "Material"
Cohesion: 0.08
Nodes (17): PureTestCase, Carrier, ImportLog, Material, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna. (+9 more)

### Community 13 - "test_layout.py"
Cohesion: 0.15
Nodes (19): analyze(), check_layout(), _issue(), Lista problemów: error blokuje zapis, warning tylko ostrzega., (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a…, CheckLayoutTests, CleanLayoutTests, codes() (+11 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.17
Nodes (17): _geometry(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji). (+9 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.15
Nodes (12): LocationOverride, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master() (+4 more)

### Community 16 - "ml/views.py"
Cohesion: 0.11
Nodes (14): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, MlRunTests, TestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., detail(), home() (+6 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "importers.py"
Cohesion: 0.18
Nodes (22): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+14 more)

### Community 20 - "roles.py"
Cohesion: 0.11
Nodes (11): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, has_role(), True dla superusera albo członka którejś z grup., Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required() (+3 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.15
Nodes (18): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+10 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.14
Nodes (5): override_settings, TestCase, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "test_addressing.py"
Cohesion: 0.17
Nodes (12): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), codes(), ExpandModelTests, ExpandRowTests, ov() (+4 more)

### Community 26 - "ml/services.py"
Cohesion: 0.12
Nodes (23): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), abc_by_hits(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Dni z ruchem ≥ WORKDAY_SHARE mediany dni z jakimkolwiek ruchem (rosnąco)., working_days() (+15 more)

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
Nodes (21): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+13 more)

### Community 31 - "design_day.py"
Cohesion: 0.09
Nodes (24): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, _abc_xyz(), build_profile(), _groups(), load_groups(), _order_profile(), percentile() (+16 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.19
Nodes (27): snap(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected() (+19 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "test_design_compare.py"
Cohesion: 0.19
Nodes (11): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+3 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.21
Nodes (15): model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.13
Nodes (19): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), abc_from_history(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., {materiał: A/B/C} z ostatniej segmentacji (Prognozy i ML); {} gdy nie liczona., catalog(), _counts() (+11 more)

### Community 42 - "StudioViewTests"
Cohesion: 0.10
Nodes (19): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+11 more)

### Community 43 - "designer"
Cohesion: 0.38
Nodes (11): day_save(), _errors(), outbound_save(), designer, require_POST, _save_formset(), scenario_copy(), scenario_create() (+3 more)

### Community 44 - "scene-builder.js"
Cohesion: 0.10
Nodes (31): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+23 more)

### Community 45 - "test_bay_template_views.py"
Cohesion: 0.18
Nodes (5): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase, Ekran szablonów gniazd (CRUD, role) + kolumny szablon/numeracja/kierunek w…

### Community 46 - "_inside"
Cohesion: 0.14
Nodes (11): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., _vna_racks(), Palety w lokalizacjach (stan magazynu) w scenie Blendera —…, EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w… (+3 more)

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.12
Nodes (30): InboundStream, Meta, OutboundStream, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Auta wyjazdowe — jak przyjęcia. Koniec okna = cut-off (odjazd / odbiór kuriera)., Zmiana procesu: godziny, przerwa, zakładana obsada. Koniec ≤ początek = zmiana…, Scenario, Shift (+22 more)

### Community 49 - "test_ewm_tasks_flow.py"
Cohesion: 0.19
Nodes (10): Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją)., resolve_moves(), window_source(), SimpleTestCase, Zadania EWM (WT) w animacji przepływów: ruchy wózków z realnych zadań (agenci z…, ResolveMovesTests (+2 more)

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "layout-core.js"
Cohesion: 0.13
Nodes (18): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+10 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (32): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+24 more)

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
Cohesion: 0.15
Nodes (22): applyIssues(), CFG, check(), fit(), fullscreen, history, load(), payload() (+14 more)

### Community 59 - "test_dane.py"
Cohesion: 0.15
Nodes (9): Meta, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase (+1 more)

### Community 60 - "sim/__init__.py"
Cohesion: 0.21
Nodes (11): Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)., with_extra_docks() (+3 more)

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

### Community 67 - "layout-hall.js"
Cohesion: 0.25
Nodes (17): drawItem(), el(), render(), status(), viewCenter(), CFG, deleteSelectedColumn(), drawColumns() (+9 more)

### Community 68 - "addressing.py"
Cohesion: 0.16
Nodes (11): _bay_locations(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+3 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.16
Nodes (6): EwmTasksPollingTests, MetaRefreshGuardTests, SimpleTestCase, TestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.16
Nodes (9): FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), SimpleTestCase, _rack() (+1 more)

### Community 71 - "test_flow_player.py"
Cohesion: 0.15
Nodes (7): ClampTests, FlowPlayerPanelTests, FlowSceneEndpointTests, SimpleTestCase, TestCase, Animacja przepływów w widoku 3D modelu: endpoint sceny dla odtwarzacza three.js…, _clamped()

### Community 72 - "bay_templates.py"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

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
Cohesion: 0.20
Nodes (10): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund. (+2 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.08
Nodes (20): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne). (+12 more)

### Community 82 - "detect"
Cohesion: 0.21
Nodes (15): format_bay_numbers(), letter_rank(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., detect(), _distance(), _grid(), _new_template() (+7 more)

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
Cohesion: 0.11
Nodes (17): rack_corners(), _column_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma). (+9 more)

### Community 95 - "shared.py"
Cohesion: 0.11
Nodes (37): _activity_picks(), build_scene_for_model(), model_racks(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak). (+29 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - "SlotLocator"
Cohesion: 0.33
Nodes (3): Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, SlotLocatorTests

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.17
Nodes (11): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Scenariusz (niezależny od layoutu), Składowanie i kompletacja, TWINEMA — założenia master daty i scenariuszy (+3 more)

### Community 123 - "layout.py"
Cohesion: 0.20
Nodes (18): clean_columns(), clean_layout(), clean_underlay(), _fname(), height_kpi(), _id(), _int(), LayoutError (+10 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - ".slot"
Cohesion: 0.20
Nodes (8): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 128 - "GeneratorTests"
Cohesion: 0.15
Nodes (6): Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., vna_levels(), GeneratorTests, SimpleTestCase, Generator hali od parametrów (plan 2026-10-02, etap 1): pojemność, geometria,…, _rect()

### Community 132 - "ScenarioDay"
Cohesion: 0.16
Nodes (3): check_triples(), ScenarioDay, triple()

### Community 133 - "build_pallets"
Cohesion: 0.20
Nodes (5): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase

### Community 134 - "warehouse_layout.py"
Cohesion: 0.16
Nodes (22): feature_row(), rack_row(), _analyze(), _image_size(), _layout(), _parse(), _md_role, _planner (+14 more)

### Community 135 - "demo_stock"
Cohesion: 0.21
Nodes (8): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase

### Community 138 - "WarehouseLocationMasterBatch"
Cohesion: 0.29
Nodes (5): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch

### Community 139 - "demo_scenariusz.py"
Cohesion: 0.33
Nodes (5): Command, atomic, BaseCommand, _r(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…

### Community 141 - "test_container_inbound.py"
Cohesion: 0.23
Nodes (7): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.20
Nodes (5): png(), override_settings, TestCase, E2b — API edytora: zapis wysokości, słupów i sprzętu; podkład (upload,…, StructureApiTests

### Community 149 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 150 - "generate"
Cohesion: 0.42
Nodes (8): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za., _row_pairs()

### Community 151 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 154 - "test_model_edit.py"
Cohesion: 0.10
Nodes (26): bbox(), near_pairs(), overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, apply_zone_edit(), _box(), collisions() (+18 more)

### Community 156 - "CalibrationViewTests"
Cohesion: 0.22
Nodes (3): CalibrationViewTests, TestCase, _racks()

### Community 157 - "_save"
Cohesion: 0.31
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 158 - "scenario/services.py"
Cohesion: 0.20
Nodes (9): Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)., simulate(), dock_role(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, features: dicty jak `twin.shared.hall_feature_dict` (kind, label, width, depth,…, staging_side(), PlacesTests (+1 more)

### Community 159 - "report.py"
Cohesion: 0.24
Nodes (12): bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze…, Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min., Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}. (+4 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 164 - "test_sim.py"
Cohesion: 0.40
Nodes (5): EngineTests, plan(), Symulacja dnia (S3a) — czysty Python: plan, kolejki doków, pole odkładcze, cut-…, shifts(), truck()

### Community 167 - "test_layout_editor_js.py"
Cohesion: 0.27
Nodes (6): skipUnless, rack_geom(), Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, LayoutCoreJsTests, node_eval(), Czyste funkcje JS edytora layoutu (static/twin/js/layout-core.js): testy `node…

### Community 168 - "staffing"
Cohesion: 0.24
Nodes (5): process_hours(), → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, staffing(), StaffingTests, _results()

### Community 169 - "params_for"
Cohesion: 0.29
Nodes (5): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., CatalogTests

### Community 170 - "design_calibration.py"
Cohesion: 0.28
Nodes (6): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).

### Community 171 - "_wt_window"
Cohesion: 0.22
Nodes (9): default_start(), load_window(), parse_start(), Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, _clamped_float(), ?wt=<id>|latest — wózki z importu zadań EWM w oknie ?wt_from (czas lokalny,… (+1 more)

### Community 172 - "WarehouseTask"
Cohesion: 0.25
Nodes (4): Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 175 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 177 - "column_list"
Cohesion: 0.43
Nodes (4): column_list(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, ColumnTests, grid()

### Community 179 - "cartons_per_pallet_hint"
Cohesion: 0.50
Nodes (4): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_hint(), Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…

### Community 180 - "BlenderImportGuardTests"
Cohesion: 0.50
Nodes (3): BlenderImportGuardTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

## Knowledge Gaps
- **82 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+77 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **35 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `GeneratorTests`, `studio/api.py`, `masterdata/services.py`, `demo_scenariusz.py`, `blender_scene.py`, `test_ewm_service.py`, `roles.py`, `StructureApiTests`, `WorkerApiTests`, `test_model_edit.py`, `test_warehouse_model_view.py`, `BayTemplate`, `masterdata/views.py`, `test_bay_template_views.py`, `scenario/views.py`, `test_ewm_tasks_flow.py`, `studio/views.py`, `test_deck.py`, `test_dane.py`, `views_sim.py`, `test_flow_player.py`, `test_design_calibration.py`, `studio/models.py`, `rack_corners`, `shared.py`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.041) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _82 weakly-connected nodes found - possible documentation gaps or missing edges._