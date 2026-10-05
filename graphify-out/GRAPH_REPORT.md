# Graph Report - agent-a811e831b9d9f2857  (2026-10-05)

## Corpus Check
- 251 files · ~163,034 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 2879 nodes · 6055 edges · 185 communities (148 shown, 37 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 210 edges (avg confidence: 0.53)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7a5568b1`
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
- test_design_variants.py
- blender_scene.py
- Material
- check_layout
- twinema_design_kit.py
- make_model_and_master
- ml/services.py
- test_design_sim_scene.py
- scene-builder.js
- importers.py
- scene-data.js
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- RenderJob
- test_design_forecast.py
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
- ewm_service.py
- warehouse_variants.py
- scenario/services.py
- StudioViewTests
- designer
- day-timeline.js
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
- DaneViewTests
- sim/__init__.py
- VoiceViewTests
- test_s3b_views.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-hall.js
- export.py
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- warehouse_model.py
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- BlenderExportViewTests
- calibrate
- Pochodzenie kodu
- ScenarioViewTests
- studio/models.py
- LoadAndViewTests
- addressing.py
- segmentation.py
- SimViewTests
- icon
- rack_corners
- test_design_hub.py
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
- params_for
- design_kpi.py
- .slot
- model_racks
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- test_blender_export.py
- StudioConfig
- generate
- studio/migrations/0001_initial.py
- _save
- blender_stock.py
- layout-preview.js
- CalibrationViewTests
- SlotLocator
- 0003_render_montaz.py
- warehouse_layout.py
- SimulationViewTests
- ScenarioConfig
- test_container_inbound.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- VariantViewTests
- bottlenecks
- EwmViewsTests
- .as_dict
- EngineTests
- test_layout.py
- 0002_wydania_obsada.py
- GeometryUploadTests
- VariantEditViewTests
- views_play.py
- report.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- test_dane.py
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- PlayViewTests
- .handle
- context_processors.py
- Command
- blender_route.py
- WarehouseTask
- fullscreen.test.mjs
- layout.py
- check_triples
- masterdata/views.py
- simulate
- simulate_plan
- MetaRefreshGuardTests
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

## Communities (185 total, 37 thin omitted)

### Community 0 - "shared.py"
Cohesion: 0.16
Nodes (20): load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, hall_feature_dict(), Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, Element hali → dict do renderu (kolor rozwiązany, etykieta z rodzaju)., design_hub() (+12 more)

### Community 1 - "scenario/models.py"
Cohesion: 0.11
Nodes (21): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+13 more)

### Community 2 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 3 - "views_compare.py"
Cohesion: 0.19
Nodes (9): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, compare(), _label(), any_role, Tabela porównania layout × scenariusz (E7) i eksport xlsx (E8)., run_xlsx() (+1 more)

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.12
Nodes (29): never_cache, purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie., Zapis uploadu na dysk kawałkami → token (nazwa pliku) do podglądu i importu., Ścieżka pliku po tokenie z formularza — tylko nasz format nazwy (bez path…, Import całego pliku do partii. Błąd w trakcie → partia „error”, zapisane…, run_import() (+21 more)

### Community 7 - "simulate"
Cohesion: 0.11
Nodes (19): _Agent, Layout, _manh(), _pick(), Mnożnik wzrostu: > 1 dokłada losowe kopie zadań (czas ±15 min), < 1 losowo…, Linie kompletacji → objazdy: per dokument (bez dokumentu — pojedynczo), max 20…, tasks: [(sekunda od DAY_START, rodzaj, materiał, dokument)]; fleet: {"agv": n,…, Agent, który najwcześniej stanie w `start` (nie wcześniej niż `release`). (+11 more)

### Community 8 - "twin/models.py"
Cohesion: 0.06
Nodes (36): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Ekrany studia: role, szkic z szablonu, edycja tylko w szkicu, akceptacja, szkic…, active_master_qs() (+28 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.08
Nodes (30): missing_required(), parse_rows(), → (poprawne dicty, odrzucone [{row, reason}] — próbka), liczba odrzuconych.…, Command, BaseCommand, cartons_per_pallet_distribution(), current_stock_log(), import_file() (+22 more)

### Community 10 - "test_design_variants.py"
Cohesion: 0.15
Nodes (13): anchor_count(), clean_elements(), compute_kpi(), equipment_capacity(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, Liczba rzeczywistych punktów obsługi (0 → droga liczona od przodu hali)., (punkt przed frontem boku/kanału, liczba miejsc paletowych) dla elementów…, Nominalna wydajność sprzętu wg katalogu, zsumowana per rodzaj elementu. (+5 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.10
Nodes (38): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), build_scene(), _container_flow(), _demo_picks(), _feature_center() (+30 more)

### Community 12 - "Material"
Cohesion: 0.08
Nodes (18): PureTestCase, Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów… (+10 more)

### Community 13 - "check_layout"
Cohesion: 0.13
Nodes (20): check_layout(), column_list(), _fname(), _issue(), _name(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, Lista problemów: error blokuje zapis, warning tylko ostrzega., CheckLayoutTests (+12 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.18
Nodes (22): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+14 more)

### Community 15 - "make_model_and_master"
Cohesion: 0.24
Nodes (6): load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., make_model_and_master(), TestCase, ServiceTests

### Community 16 - "ml/services.py"
Cohesion: 0.13
Nodes (19): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+11 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.11
Nodes (12): build_sim_scene(), CorridorRouter, _pick_time(), Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs(), _busiest_hour() (+4 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.15
Nodes (24): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+16 more)

### Community 19 - "importers.py"
Cohesion: 0.18
Nodes (22): _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm(), _num() (+14 more)

### Community 20 - "scene-data.js"
Cohesion: 0.15
Nodes (21): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, editorScene(), effectiveQuality(), extents(), FAST_ABOVE, hallWalls() (+13 more)

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

### Community 25 - "RenderJob"
Cohesion: 0.13
Nodes (14): Meta, RenderJob, create(), delete(), jobs(), Meta, any_role, designer (+6 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.18
Nodes (15): backtest(), fit(), forecast(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i…, series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu… (+7 more)

### Community 27 - "flow-player.js"
Cohesion: 0.11
Nodes (10): createFlowPlayer(), _e, FLOW_LABELS, FLOW_Y, _p, _s, SIM_KEYS, SKU_PALETTE (+2 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "ViewFloatLocalizationTests"
Cohesion: 0.10
Nodes (10): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, G1: prawdziwy stan HU z odtwarzacza przepływów chowa palety poglądowe (bez…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "Agent"
Cohesion: 0.17
Nodes (7): Agent, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów.

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (20): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+12 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.20
Nodes (26): addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected(), rotateSelected() (+18 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (16): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+8 more)

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

### Community 39 - "ewm_service.py"
Cohesion: 0.08
Nodes (35): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows() (+27 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.18
Nodes (15): Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "scenario/services.py"
Cohesion: 0.33
Nodes (7): Palety na stanie per materiał z wagą i flagami stref specjalnych (dla reguł…, stock_profile(), placement_for(), Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)., Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie…, feature_row(), rack_row()

### Community 42 - "StudioViewTests"
Cohesion: 0.10
Nodes (19): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+11 more)

### Community 43 - "designer"
Cohesion: 0.38
Nodes (11): day_save(), _errors(), outbound_save(), designer, require_POST, _save_formset(), scenario_copy(), scenario_create() (+3 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.11
Nodes (43): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+35 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.19
Nodes (8): _vna_racks(), EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.09
Nodes (38): has_role(), True dla superusera albo członka którejś z grup., cartons_per_pallet_hint(), Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, demo_zones(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, InboundStream (+30 more)

### Community 49 - "resolve_moves"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "Scan"
Cohesion: 0.06
Nodes (37): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), map_columns(), map_kind(), missing_required() (+29 more)

### Community 51 - "layout-core.js"
Cohesion: 0.13
Nodes (19): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+11 more)

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (34): Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta., template_script(), approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create() (+26 more)

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
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "layout-editor.js"
Cohesion: 0.13
Nodes (25): svgTransform(), applyIssues(), CFG, check(), drawItem(), el(), fit(), fullscreen (+17 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.17
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "sim/__init__.py"
Cohesion: 0.21
Nodes (11): Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)., with_extra_docks() (+3 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "test_s3b_views.py"
Cohesion: 0.12
Nodes (14): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, S3b w aplikacji: rola doku (pole, migracja, generator, edytor, symulacja),…, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,…, _cell(), any_role, designer, require_POST (+6 more)

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

### Community 68 - "export.py"
Cohesion: 0.15
Nodes (17): _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook(), _sheet(), cutoff_risk() (+9 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.21
Nodes (7): FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), _Ctx

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "warehouse_model.py"
Cohesion: 0.14
Nodes (21): Meta, WarehouseModelForm, _parse_location_code(), Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., B0-01-300A → (zone, rack, bay, level_letter, level_num)., save_hall_features(), model_scene_data(), _parse_pasted_codes() (+13 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - "packaging.py"
Cohesion: 0.17
Nodes (18): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+10 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 77 - "calibrate"
Cohesion: 0.21
Nodes (9): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie. (+1 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.09
Nodes (18): Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno). (+10 more)

### Community 82 - "addressing.py"
Cohesion: 0.06
Nodes (47): _bay_locations(), expand_model(), expand_row(), format_bay_numbers(), letter_rank(), make_code(), parse_bay_numbers(), parse_code() (+39 more)

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
Nodes (15): rack_corners(), _column_corners(), floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma). (+7 more)

### Community 87 - "test_design_hub.py"
Cohesion: 0.22
Nodes (5): DemoFileTests, DesignHubTests, SimpleTestCase, TestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…

### Community 95 - "warehouse_blender.py"
Cohesion: 0.12
Nodes (24): model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą… (+16 more)

### Community 117 - "params_for"
Cohesion: 0.15
Nodes (10): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., AisleCheckTests, BlenderImportGuardTests, CatalogTests, SimpleTestCase (+2 more)

### Community 118 - "design_kpi.py"
Cohesion: 0.18
Nodes (17): check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji)., Rzut obrysu elementu na oś: (początek, koniec) [m]; along=True → szerokość. (+9 more)

### Community 119 - ".slot"
Cohesion: 0.20
Nodes (8): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 120 - "model_racks"
Cohesion: 0.13
Nodes (17): build_scene_for_model(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją)., window_source() (+9 more)

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "test_placement.py"
Cohesion: 0.15
Nodes (20): _center(), check_placement(), _inside(), _issue(), _poly(), positions(), Pojemność layoutu vs potrzeba i reguły rozmieszczenia (S3b) — czysty Python,…, Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /… (+12 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "test_blender_export.py"
Cohesion: 0.13
Nodes (11): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., _aisle_m(), Najwęższy korytarz przy regale: po każdej stronie najbliższy równoległy regał…, _span(), BuildSceneTests, SimpleTestCase, _rack() (+3 more)

### Community 128 - "generate"
Cohesion: 0.13
Nodes (14): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+6 more)

### Community 132 - "_save"
Cohesion: 0.16
Nodes (7): CompareViewTests, TestCase, HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 133 - "blender_stock.py"
Cohesion: 0.17
Nodes (9): abc_by_hits(), build_pallets(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase (+1 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.33
Nodes (9): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+1 more)

### Community 135 - "CalibrationViewTests"
Cohesion: 0.22
Nodes (3): CalibrationViewTests, TestCase, _racks()

### Community 136 - "SlotLocator"
Cohesion: 0.28
Nodes (5): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, SlotLocatorTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.17
Nodes (21): hall_feature_kinds(), _analyze(), _image_size(), _layout(), _parse(), _md_role, _planner, require_POST (+13 more)

### Community 139 - "SimulationViewTests"
Cohesion: 0.17
Nodes (4): TestCase, TestCase, SimSceneViewTests, SimulationViewTests

### Community 141 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "VariantViewTests"
Cohesion: 0.24
Nodes (3): _el(), TestCase, VariantViewTests

### Community 150 - "bottlenecks"
Cohesion: 0.31
Nodes (6): bottlenecks(), Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze…, _smallest(), BottleneckTests, _rep()

### Community 153 - "EngineTests"
Cohesion: 0.47
Nodes (4): EngineTests, plan(), shifts(), truck()

### Community 154 - "test_layout.py"
Cohesion: 0.10
Nodes (28): bbox(), near_pairs(), overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, apply_zone_edit(), _box(), collisions() (+20 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.17
Nodes (15): PlacesTests, SimpleTestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places(), peak_index(), any_role, Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu… (+7 more)

### Community 159 - "report.py"
Cohesion: 0.27
Nodes (10): aggregate(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, [kpi przebiegu] → {klucz: {mean, worst}}; najgorszy = P95 (gdy złe „dużo”) albo…, Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min., Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}., run_report() (+2 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.24
Nodes (9): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests (+1 more)

### Community 164 - "test_dane.py"
Cohesion: 0.25
Nodes (7): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, Moduł Dane z bazą: zapis importów, demo, widoki i podpięcie do bliźniaka…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, ewm_tasks_profile(), _planner

### Community 168 - ".handle"
Cohesion: 0.40
Nodes (4): Command, atomic, BaseCommand, _r()

### Community 171 - "blender_route.py"
Cohesion: 0.14
Nodes (17): Item, Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, _dedupe() (+9 more)

### Community 172 - "WarehouseTask"
Cohesion: 0.14
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 174 - "layout.py"
Cohesion: 0.28
Nodes (15): clean_columns(), clean_layout(), clean_underlay(), _dock_role(), _id(), _int(), LayoutError, _num() (+7 more)

### Community 176 - "masterdata/views.py"
Cohesion: 0.16
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), catalog(), _counts(), demo(), home(), log_detail(), materials() (+7 more)

### Community 177 - "simulate"
Cohesion: 0.15
Nodes (13): placement_bottlenecks(), Problemy pojemności/rozmieszczenia w formacie wąskich gardeł symulacji (na…, simulate(), dock_role(), needed_roles(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`). (+5 more)

### Community 178 - "simulate_plan"
Cohesion: 0.17
Nodes (7): Docks, Fleet, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan()

### Community 182 - "StockItem"
Cohesion: 0.17
Nodes (5): Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, DockRoleTests, TestCase, SimS3bTests

### Community 183 - "demo_stock"
Cohesion: 0.21
Nodes (8): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase

### Community 184 - "safe_json"
Cohesion: 0.28
Nodes (8): JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), _md_role, _planner, require_POST, warehouse_rack_type_delete(), warehouse_rack_type_form(), warehouse_rack_type_list()

### Community 186 - "analyze"
Cohesion: 0.14
Nodes (13): skipUnless, rack_to_element(), Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,…, analyze(), height_kpi(), rack_geom(), Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, Wysokość w świetle → maks. poziomów per strefa (przy wysokości poziomu jej… (+5 more)

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

## Knowledge Gaps
- **92 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+87 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **37 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `shared.py`, `generate`, `test_dane.py`, `test_layout.py`, `warehouse_model.py`, `masterdata/views.py`, `scenario/views.py`, `studio/models.py`, `studio/views.py`, `rack_corners`, `test_s3b_views.py`, `RenderJob`, `test_blender_export.py`, `views_play.py`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `WarehouseTaskBatch` connect `shared.py` to `warehouse_tasks.py`, `simulate`, `SimulationViewTests`, `WarehouseTask`, `ml/services.py`, `test_design_hub.py`, `test_design_forecast.py`, `warehouse_blender.py`?**
  _High betweenness centrality (0.030) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _92 weakly-connected nodes found - possible documentation gaps or missing edges._