# Graph Report - agent-a8f2388dc31ef0f10  (2026-10-05)

## Corpus Check
- 214 files · ~125,132 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2368 nodes · 4805 edges · 157 communities (126 shown, 31 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 161 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `99f00ba7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- WarehouseTaskBatch
- scenario/models.py
- studio/api.py
- test_outbound.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- design_kpi.py
- blender_scene.py
- GeneratorTests
- test_layout.py
- design_catalog.py
- shared.py
- blender_stock.py
- test_design_sim_scene.py
- twinema_design_kit.py
- importers.py
- roles.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- addressing.py
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- WarehouseModelViewTests
- blender_route.py
- design_day.py
- forecast.py
- layout-editor.js
- kpi_facts
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- test_design_compare.py
- warehouse_model_ewm.py
- warehouse_variants.py
- masterdata/views.py
- draft_script
- scenario/views.py
- model_edit.py
- BayTemplateViewTests
- EquipmentAgentsTests
- middleware.py
- Scenario
- resolve_moves
- Scan
- SimulationViewTests
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- render/views.py
- Material
- StudioViewTests
- VoiceViewTests
- layout.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- VariantViewTests
- test_container_inbound.py
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- rack_corners
- RackTypeWeightsTests
- EwmViewsTests
- calibrate
- Pochodzenie kodu
- ScenarioViewTests
- Shot
- LoadAndViewTests
- ScenarioDay
- segmentation.py
- ewm_tasks.py
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
- SlotLocator
- parse_overrides
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- parse_row
- 0002_pole_odkladcze.py
- twinema_render.py
- .slot
- StudioConfig
- generate
- studio/migrations/0001_initial.py
- params_for
- build_pallets
- warehouse_layout.py
- demo_stock
- MlRunTests
- 0003_render_montaz.py
- design_calibration.py
- demo_scenariusz.py
- ScenarioConfig
- test_ewm_tasks_refresh.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- Command
- warehouse_design_sim.py
- GeneratorViewTests
- test_design_sim.py
- GeometryUploadTests
- warehouse_generator.py
- near_pairs
- 0002_wydania_obsada.py
- WarehouseTask

## God Nodes (most connected - your core abstractions)
1. `SlotLocator` - 33 edges
2. `WarehouseModel` - 32 edges
3. `simulate()` - 29 edges
4. `build_scene()` - 24 edges
5. `Scan` - 23 edges
6. `Agent` - 22 edges
7. `WarehouseModelRack` - 22 edges
8. `WarehouseTaskBatch` - 22 edges
9. `rack_corners()` - 21 edges
10. `model_racks()` - 21 edges

## Surprising Connections (you probably didn't know these)
- `start()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `load_variant()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add()` --calls--> `params_for()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py
- `add_block()` --calls--> `rack_axes()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/blender_route.py
- `add_block()` --calls--> `block_rows()`  [EXTRACTED]
  tools/blender/twinema_design_kit.py → web/twin/design_catalog.py

## Import Cycles
- None detected.

## Communities (157 total, 31 thin omitted)

### Community 0 - "WarehouseTaskBatch"
Cohesion: 0.10
Nodes (21): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json() (+13 more)

### Community 1 - "scenario/models.py"
Cohesion: 0.11
Nodes (21): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+13 more)

### Community 2 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 3 - "test_outbound.py"
Cohesion: 0.21
Nodes (11): cutoff_risk(), process_hours(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy…, span(), staffing() (+3 more)

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
Cohesion: 0.11
Nodes (21): _Agent, _kpi(), Layout, _manh(), _p95(), _pick(), Symulacja dnia projektowego na wariancie hali (plan 2026-10-02, etap 3a) —…, Mnożnik wzrostu: > 1 dokłada losowe kopie zadań (czas ±15 min), < 1 losowo… (+13 more)

### Community 8 - "twin/models.py"
Cohesion: 0.10
Nodes (18): Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka…, Meta, WarehouseModelForm, Migration, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, WarehouseHallFeature, WarehouseModel (+10 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.17
Nodes (16): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, import_file(), _level_of(), load_demo(), Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…, Materiały demo (upsert) + import stanów demo dla modelu hali → (liczba… (+8 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.15
Nodes (18): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), compute_kpi(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i… (+10 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.10
Nodes (37): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), _aisle_m(), build_scene(), _carry(), _container_flow() (+29 more)

### Community 12 - "GeneratorTests"
Cohesion: 0.18
Nodes (3): GeneratorTests, SimpleTestCase, _rect()

### Community 13 - "test_layout.py"
Cohesion: 0.17
Nodes (17): clean_layout(), feature_row(), _id(), _int(), LayoutError, _num(), ValueError, Nieprawidłowe dane z edytora — komunikat do pokazania użytkownikowi. (+9 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.15
Nodes (19): _geometry(), block_rows(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+11 more)

### Community 15 - "shared.py"
Cohesion: 0.08
Nodes (23): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, LocationOverride, Meta, Named location type template — dimensions apply to all locations with matching…, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,… (+15 more)

### Community 16 - "blender_stock.py"
Cohesion: 0.10
Nodes (24): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation() (+16 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.09
Nodes (15): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+7 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "importers.py"
Cohesion: 0.18
Nodes (21): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+13 more)

### Community 20 - "roles.py"
Cohesion: 0.08
Nodes (16): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Meta (+8 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.15
Nodes (18): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+10 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "addressing.py"
Cohesion: 0.06
Nodes (45): expand_model(), expand_row(), format_bay_numbers(), letter_rank(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,… (+37 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.18
Nodes (15): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+7 more)

### Community 27 - "flow-player.js"
Cohesion: 0.10
Nodes (12): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s (+4 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "WarehouseModelViewTests"
Cohesion: 0.11
Nodes (9): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests, ViewFloatLocalizationTests (+1 more)

### Community 30 - "blender_route.py"
Cohesion: 0.10
Nodes (20): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+12 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (20): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+12 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-editor.js"
Cohesion: 0.07
Nodes (70): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+62 more)

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

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.10
Nodes (27): apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, [(kod, typ EWM, wysokość mm, udźwig kg)] z mastera — tylko kody stref modelu., Propozycja „Wykryj z EWM” dla rzędów modelu (nic nie zapisuje). (+19 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.19
Nodes (15): clean_elements(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.17
Nodes (13): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., demo(), home(), log_detail(), materials() (+5 more)

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.15
Nodes (21): has_role(), True dla superusera albo członka którejś z grup., _arrival_rows(), day_save(), _errors(), _fc(), _hours_rows(), _num() (+13 more)

### Community 44 - "model_edit.py"
Cohesion: 0.13
Nodes (22): bbox(), overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.… (+14 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "EquipmentAgentsTests"
Cohesion: 0.22
Nodes (6): EquipmentAgentsTests, SimpleTestCase, _rack(), Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "Scenario"
Cohesion: 0.13
Nodes (21): InboundStream, Meta, OutboundStream, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Auta wyjazdowe — jak przyjęcia. Koniec okna = cut-off (odjazd / odbiór kuriera)., Zmiana procesu: godziny, przerwa, zakładana obsada. Koniec ≤ początek = zmiana…, Scenario, Shift (+13 more)

### Community 49 - "resolve_moves"
Cohesion: 0.23
Nodes (7): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, _racks(), ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "SimulationViewTests"
Cohesion: 0.17
Nodes (4): CompareViewTests, TestCase, TestCase, SimulationViewTests

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (34): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+26 more)

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

### Community 58 - "render/views.py"
Cohesion: 0.18
Nodes (12): create(), delete(), jobs(), Meta, any_role, designer, require_POST, Stan zleceń w toku — strona odpytuje i przeładowuje się, gdy coś się zmieni. (+4 more)

### Community 59 - "Material"
Cohesion: 0.12
Nodes (13): ImportLog, Material, Meta, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Materiał (SKU): opakowanie zbiorcze i paletyzacja — wejście do rozmieszczenia i…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem (+5 more)

### Community 60 - "StudioViewTests"
Cohesion: 0.23
Nodes (3): override_settings, TestCase, StudioViewTests

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "layout.py"
Cohesion: 0.19
Nodes (13): skipUnless, analyze(), check_layout(), _issue(), _name(), rack_geom(), Layout hali dla edytora planu (czysty Python — bez Django, testowalny bez…, Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i… (+5 more)

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.18
Nodes (4): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…

### Community 68 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.08
Nodes (14): _dedupe(), FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), BlenderExportViewTests (+6 more)

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "bay_templates.py"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "rack_corners"
Cohesion: 0.17
Nodes (14): rack_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +… (+6 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "calibrate"
Cohesion: 0.19
Nodes (9): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie. (+1 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "Shot"
Cohesion: 0.11
Nodes (12): Meta, MontageJob, Presentation, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)., Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →…, Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między… (+4 more)

### Community 82 - "ScenarioDay"
Cohesion: 0.16
Nodes (3): check_triples(), ScenarioDay, triple()

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.11
Nodes (26): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., active_master(), Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis…, Aktywny (najnowszy) import mastera lokalizacji albo None., Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), _parse_location_code() (+18 more)

### Community 95 - "warehouse_blender.py"
Cohesion: 0.11
Nodes (24): build_scene_for_model(), Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą… (+16 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - "SlotLocator"
Cohesion: 0.25
Nodes (6): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…, SlotLocatorTests

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.17
Nodes (11): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Scenariusz (niezależny od layoutu), Składowanie i kompletacja, TWINEMA — założenia master daty i scenariuszy (+3 more)

### Community 123 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - ".slot"
Cohesion: 0.20
Nodes (8): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 128 - "generate"
Cohesion: 0.28
Nodes (11): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+3 more)

### Community 132 - "params_for"
Cohesion: 0.24
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 133 - "build_pallets"
Cohesion: 0.20
Nodes (5): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase

### Community 134 - "warehouse_layout.py"
Cohesion: 0.25
Nodes (14): rack_row(), hall_feature_kinds(), _layout(), _parse(), _md_role, _planner, require_POST, → (layout, None) albo (None, odpowiedź błędu). (+6 more)

### Community 135 - "demo_stock"
Cohesion: 0.19
Nodes (11): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami., Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+3 more)

### Community 138 - "design_calibration.py"
Cohesion: 0.28
Nodes (6): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).

### Community 139 - "demo_scenariusz.py"
Cohesion: 0.33
Nodes (5): Command, atomic, BaseCommand, _r(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…

### Community 141 - "test_ewm_tasks_refresh.py"
Cohesion: 0.40
Nodes (3): MetaRefreshGuardTests, SimpleTestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…

### Community 149 - "warehouse_design_sim.py"
Cohesion: 0.16
Nodes (25): model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H. (+17 more)

### Community 151 - "test_design_sim.py"
Cohesion: 0.15
Nodes (5): Symulacja dnia projektowego na hali z generatora (plan 2026-10-02, etap 3a)., TestCase, Edycja wariantu hali blokami (plan 2026-10-02, etap 4)., VariantEditViewTests, _save()

### Community 153 - "warehouse_generator.py"
Cohesion: 0.47
Nodes (4): HallGeneratorForm, _initial(), _md_role, warehouse_model_generator()

### Community 154 - "near_pairs"
Cohesion: 0.29
Nodes (4): near_pairs(), Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, GeometryTests, TestCase

### Community 156 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): Meta, WarehouseTask, CalibrationViewTests, TestCase, ForecastViewTests, TestCase

## Knowledge Gaps
- **70 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+65 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **31 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `generate`, `BayTemplate`, `masterdata/views.py`, `rack_corners`, `shared.py`, `roles.py`, `studio/views.py`, `test_design_sim.py`, `render/views.py`?**
  _High betweenness centrality (0.051) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.034) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Scan` (e.g. with `HeaderAliasTests` and `KindMappingTests`) actually correct?**
  _`Scan` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _70 weakly-connected nodes found - possible documentation gaps or missing edges._