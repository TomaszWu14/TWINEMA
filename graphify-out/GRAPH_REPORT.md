# Graph Report - agent-a33895230b4b2dd95  (2026-10-05)

## Corpus Check
- 293 files · ~189,954 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3310 nodes · 7066 edges · 210 communities (165 shown, 45 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 220 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2f0254fd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sim.py
- day_demand
- CatalogViewTests
- render/views.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- showcase.py
- site.py
- blender_scene.py
- test_master_data.py
- analyze
- twinema_design_kit.py
- test_ewm_service.py
- ml/services.py
- test_design_sim_scene.py
- scene-builder.js
- masterdata/importers.py
- scene-data.js
- test_voice.py
- equipment/importers.py
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
- staffing.py
- ewm_service.py
- warehouse_variants.py
- test_fleet_catalog.py
- draft_script
- designer
- day-timeline.js
- BayTemplateViewTests
- EquipmentAgentsTests
- middleware.py
- scenario/views.py
- resolve_moves
- warehouse_blender.py
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- layout-site.js
- DaneViewTests
- test_dane.py
- VoiceViewTests
- scenario/services.py
- pre-push
- test_ml.py
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-editor.js
- SlotLocator
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- blender_route.py
- calibrate
- Pochodzenie kodu
- ScenarioViewTests
- Presentation
- LoadAndViewTests
- addressing.py
- equipment/views.py
- simulate
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
- rack_axes
- test_ewm_tasks_parser.py
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
- design_calibration.py
- build_pallets
- layout-preview.js
- ComputeTests
- Scan
- 0003_render_montaz.py
- warehouse_layout.py
- masterdata/services.py
- ScenarioConfig
- segmentation.py
- scenario/migrations/0001_initial.py
- 0004_kadry.py
- StructureApiTests
- VariantViewTests
- EwmViewsTests
- layout-hall.js
- ewm_tasks.py
- parse_row
- warehouse_variant_edit.py
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- test_aisles.py
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- ewm_levels.py
- 0003_domyslne_nosniki_klasy.py
- GeometryUploadTests
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- equipment/models.py
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- params_for
- warehouse_racktype.py
- showcase.js
- 0006_prezentacja_3d.py
- test_role_matrix.py
- CalibrationViewTests
- warehouse_design_day.py
- views_showcase.py
- current_stock_log
- DockRoleTests
- masterdata/views.py
- LayoutEquipmentSaveTests
- 0006_sprzet_z_katalogu.py
- parse_stamp
- 0004_rola_doku_nosnosc.py
- bay_templates.py
- EquipmentConfig
- 0002_klasy_systemowe.py
- 0004_stawki_domyslne.py
- equipment/migrations/0001_initial.py
- 0003_koszty.py
- 0004_flota_z_katalogu.py
- views_compare.py
- test_container_inbound.py
- WarehouseTaskBatch
- parse_overrides
- PlayViewTests
- roles.py
- layout.py
- test_ewm_tasks_refresh.py
- ShowcaseViewTests
- ImportViewTests
- 0005_dni_szczytowe.py
- blender_stock.py
- demo_scenariusz.py
- 0006_klasy_rynkowe.py
- 0005_osprzet_producent.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 47 edges
2. `SlotLocator` - 33 edges
3. `Equipment` - 31 edges
4. `Scenario` - 30 edges
5. `generate()` - 30 edges
6. `simulate()` - 29 edges
7. `LayoutError` - 29 edges
8. `analyze()` - 29 edges
9. `rack_corners()` - 27 edges
10. `clean_layout()` - 27 edges

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

## Communities (210 total, 45 thin omitted)

### Community 0 - "test_sim.py"
Cohesion: 0.05
Nodes (53): Docks, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan(), Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny). (+45 more)

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (20): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+12 more)

### Community 2 - "CatalogViewTests"
Cohesion: 0.22
Nodes (3): CatalogViewTests, TestCase, SystemClassesTests

### Community 3 - "render/views.py"
Cohesion: 0.18
Nodes (12): create(), delete(), jobs(), Meta, any_role, designer, require_POST, Stan zleceń w toku — strona odpytuje i przeładowuje się, gdy coś się zmieni. (+4 more)

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
Nodes (25): _is_shelf(), Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, _Agent, _kpi(), Layout, _manh() (+17 more)

### Community 8 - "twin/models.py"
Cohesion: 0.07
Nodes (25): Meta, WarehouseModelForm, Migration, Meta, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant (+17 more)

### Community 9 - "showcase.py"
Cohesion: 0.15
Nodes (19): _cam(), clean_slides(), _fmt(), _hhmm(), kpi_cards(), ValueError, Prezentacja 3D (P1) — czysty Python (bez Django): walidacja slajdów, karty KPI,…, Podsumowanie z liczb (bez AI). f: positions, need, fill_pct, day („typowym” /… (+11 more)

### Community 10 - "site.py"
Cohesion: 0.10
Nodes (32): guess_dock_role(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…, _area_m2(), building_height(), building_rect(), check_site(), _dock_issues(), entry_point() (+24 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.11
Nodes (32): heading_deg(), rack_point(), Kierunek jazdy w układzie hali [°] (0 = +x, 90 = +y)., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks(), build_scene(), _carry() (+24 more)

### Community 12 - "test_master_data.py"
Cohesion: 0.14
Nodes (12): Carrier, ImportLog, Material, Meta, PalletClass, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna., Klasa wysokości albo wagi palety z towarem (np. do 1,4 m / do 600 kg) — do… (+4 more)

### Community 13 - "analyze"
Cohesion: 0.11
Nodes (23): analyze(), check_layout(), _issue(), Lista problemów: error blokuje zapis, warning tylko ostrzega., (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a…, CheckLayoutTests, CleanLayoutTests, codes() (+15 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.18
Nodes (22): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+14 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.12
Nodes (14): LocationOverride, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>., CompliancePureTests (+6 more)

### Community 16 - "ml/services.py"
Cohesion: 0.14
Nodes (17): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+9 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.09
Nodes (15): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+7 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.17
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "masterdata/importers.py"
Cohesion: 0.20
Nodes (19): _bool(), _cell(), _code(), _date(), missing_required(), _num(), parse_location(), parse_material() (+11 more)

### Community 20 - "scene-data.js"
Cohesion: 0.13
Nodes (24): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, EDGE_KINDS, editorScene(), effectiveQuality(), extents(), FAST_ABOVE (+16 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "equipment/importers.py"
Cohesion: 0.15
Nodes (18): _cols(), _curve(), import_rows(), _num(), parse_file(), parse_row(), Import własnych modeli sprzętu z xlsx/csv (K2) — czysty Python poza zapisem w…, → (wiersze poprawne, odrzucone [(nr wiersza, powód)]). (+10 more)

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
Cohesion: 0.11
Nodes (17): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+9 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (20): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+12 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.16
Nodes (31): makeBlock(), mode(), nextRackIds(), addItems(), change(), deleteSelected(), duplicateSelected(), keyOf() (+23 more)

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

### Community 38 - "staffing.py"
Cohesion: 0.21
Nodes (11): cutoff_risk(), process_hours(), productive_h(), Obsada: potrzebna vs zakładana per proces i zmiana + ryzyko cut-off kurierów…, → [{process, label, hours, shifts:[{…, needed, gap}], needed, assumed, short}]…, Czy pakowanie (wszystkie paczki) zdąży do ostatniego odbioru kuriera przy…, span(), staffing() (+3 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (32): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows() (+24 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.21
Nodes (15): model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "test_fleet_catalog.py"
Cohesion: 0.17
Nodes (9): move_minutes(), Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, fleet_from_catalog(), Sprzęt floty z katalogu (K1) → czas ruchu palety na tym layoucie: średnia droga…, Fleet, FleetCatalogTests, FleetChargingTests, TestCase (+1 more)

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "designer"
Cohesion: 0.38
Nodes (11): day_save(), _errors(), outbound_save(), designer, require_POST, _save_formset(), scenario_copy(), scenario_create() (+3 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.09
Nodes (49): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+41 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "EquipmentAgentsTests"
Cohesion: 0.15
Nodes (11): _aisle_m(), Najwęższy korytarz przy regale: po każdej stronie najbliższy równoległy regał…, VNA: z pola `equipment`; bez pola — wysoki regał przy wąskiej alejce…, _span(), _vna_racks(), EquipmentAgentsTests, SimpleTestCase, _rack() (+3 more)

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.08
Nodes (33): check_triples(), InboundStream, Meta, OutboundStream, Dzień typowy i szczytowy; nowe dostają domyślne strumienie i profil (szczyt:…, Auta wyjazdowe — jak przyjęcia. Koniec okna = cut-off (odjazd / odbiór kuriera)., Zmiana procesu: godziny, przerwa, zakładana obsada. Koniec ≤ początek = zmiana…, Scenario (+25 more)

### Community 49 - "resolve_moves"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "warehouse_blender.py"
Cohesion: 0.12
Nodes (24): default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją). (+16 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (16): axes(), BACK_GAP_M, bbox(), center(), corners(), History, rad(), rotateAround() (+8 more)

### Community 52 - "studio/views.py"
Cohesion: 0.12
Nodes (34): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+26 more)

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

### Community 58 - "layout-site.js"
Cohesion: 0.21
Nodes (16): svgTransform(), all(), h(), num(), AREA_COLORS, AREA_SIZE, CFG, drawSite() (+8 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.18
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "test_dane.py"
Cohesion: 0.11
Nodes (14): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+6 more)

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "scenario/services.py"
Cohesion: 0.07
Nodes (24): Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz…, Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, Prezentacja 3D dla zarządu (P1): model hali (+ działka) i opcjonalnie wynik…, ScenarioRun, Showcase, Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)., C1: koszty CAPEX/OPEX — czysta kalkulacja (ręczne przykłady), koszty wyniku…, FleetHoursAndQueriesTests (+16 more)

### Community 64 - "test_ml.py"
Cohesion: 0.11
Nodes (6): ForecastTests, MlRunTests, SimpleTestCase, TestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "LayoutApiTests"
Cohesion: 0.15
Nodes (5): LayoutApiTests, LayoutEditorPageTests, TestCase, Ekran edytora (E2): tylko Projektant/Administratorzy, konfiguracja dla modułu…, E3: podgląd 3D obok planu — three.js z vendora (importmap, bez CDN),…

### Community 67 - "layout-editor.js"
Cohesion: 0.15
Nodes (23): applyIssues(), CFG, check(), fit(), fullscreen, history, load(), payload() (+15 more)

### Community 68 - "SlotLocator"
Cohesion: 0.28
Nodes (5): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, SlotLocatorTests

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

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
Cohesion: 0.21
Nodes (16): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+8 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "blender_route.py"
Cohesion: 0.11
Nodes (22): skipUnless, bbox(), near_pairs(), overlap_depth(), rack_corners(), Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —… (+14 more)

### Community 77 - "calibrate"
Cohesion: 0.19
Nodes (8): calibrate(), rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund., Ten sam ruch co 2 min vs co 4 min → współczynnik rośnie dwukrotnie., _rows(), _racks()

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "Presentation"
Cohesion: 0.18
Nodes (8): Meta, MontageJob, Presentation, Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →…, Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między…, VoiceTrack, Meta, PresentationForm

### Community 82 - "addressing.py"
Cohesion: 0.06
Nodes (46): _bay_locations(), expand_model(), expand_row(), format_bay_numbers(), letter_rank(), parse_bay_numbers(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +… (+38 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.18
Nodes (16): _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list(), _curve(), import_file() (+8 more)

### Community 84 - "simulate"
Cohesion: 0.10
Nodes (16): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), cartons_per_pallet_hint(), [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, placement_bottlenecks(), Problemy pojemności/rozmieszczenia w formacie wąskich gardeł symulacji (na… (+8 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.12
Nodes (24): rack_class(), Jeden predykat rodzaju regału dla KPI, rozmieszczenia, symulacji, animacji i…, model_columns(), _parse_location_code(), Słupy hali jako elementy „column” (format hall_feature_dict + `height`) dla…, Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., B0-01-300A → (zone, rack, bay, level_letter, level_num)., save_hall_features() (+16 more)

### Community 87 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 95 - "shared.py"
Cohesion: 0.12
Nodes (31): has_role(), True dla superusera albo członka którejś z grup., build_scene_for_model(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak). (+23 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.13
Nodes (22): block_rows(), check_aisles(), element_summary(), footprint(), _front_to(), height(), pallet_positions(), _parallel() (+14 more)

### Community 118 - "rack_axes"
Cohesion: 0.13
Nodes (20): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity() (+12 more)

### Community 119 - "test_ewm_tasks_parser.py"
Cohesion: 0.30
Nodes (5): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, HeaderAliasTests, Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…

### Community 120 - "test_model_geometry.py"
Cohesion: 0.16
Nodes (14): floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +…, Najmniejsza hala (szer., głęb.) mieszcząca wszystkie regały + margines. (+6 more)

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
Cohesion: 0.14
Nodes (10): CostRate, Equipment, Meta, (od, do) jako float; brak „do” = „od”; brak obu = None., Parametry robocze (z osprzętem) — jedno źródło dla layoutu i symulacji., Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, _check_range(), EquipmentForm (+2 more)

### Community 128 - "SimulationViewTests"
Cohesion: 0.09
Nodes (12): capacity(), comparison(), Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), CompareTests, CompareViewTests (+4 more)

### Community 132 - "design_calibration.py"
Cohesion: 0.21
Nodes (8): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda)., Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…

### Community 133 - "build_pallets"
Cohesion: 0.18
Nodes (8): abc_by_hits(), build_pallets(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…

### Community 134 - "layout-preview.js"
Cohesion: 0.33
Nodes (9): S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode(), stage (+1 more)

### Community 135 - "ComputeTests"
Cohesion: 0.18
Nodes (9): compute(), _item(), mix_days(), Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy…, Dni w roku: [(typ dnia, liczba dni)]. Brak symulacji jednego typu → cały rok z…, rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf:…, _total(), ComputeTests (+1 more)

### Community 136 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.12
Nodes (29): placement_for(), Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie…, column_list(), feature_row(), rack_row(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, hall_feature_kinds(), _analyze() (+21 more)

### Community 139 - "masterdata/services.py"
Cohesion: 0.11
Nodes (21): Command, BaseCommand, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, import_file(), _level_of(), load_demo() (+13 more)

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 150 - "EwmViewsTests"
Cohesion: 0.15
Nodes (3): EwmViewsTests, TestCase, Kody lokalizacji z mastera EWM to dane źródłowe — Podgląd ich nie widzi…

### Community 151 - "layout-hall.js"
Cohesion: 0.26
Nodes (16): drawHall(), drawItem(), el(), render(), status(), viewCenter(), CFG, deleteSelectedColumn() (+8 more)

### Community 152 - "ewm_tasks.py"
Cohesion: 0.23
Nodes (10): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), Parser eksportu zadań magazynowych EWM (WT) z monitora magazynu (/SCWM/MON) →…, Wiersze pliku jako listy wartości — strumieniowo, bez ładowania całości do… (+2 more)

### Community 153 - "parse_row"
Cohesion: 0.29
Nodes (5): parse_number(), parse_row(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 154 - "warehouse_variant_edit.py"
Cohesion: 0.15
Nodes (15): apply_zone_edit(), fit_floor(), {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Hala co najmniej tak duża, jak obrys regałów (+ margines), nie mniejsza niż…, zone_summary(), _copy(), ModelEditTests (+7 more)

### Community 156 - "generate"
Cohesion: 0.09
Nodes (22): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+14 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.16
Nodes (16): PlacesTests, SimpleTestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places(), peak_index(), any_role, Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu… (+8 more)

### Community 159 - "test_aisles.py"
Cohesion: 0.29
Nodes (6): AisleTests, block(), TestCase, rack(), R2: alejki dla par 0°/180° (blok „Dodaj blok” — plecami / frontami), najbliższy…, Jak makeBlock w layout-core.js: 0° | 180° (narożnik w x+w, y+d) | alejka | 0°.

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "ewm_levels.py"
Cohesion: 0.17
Nodes (16): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), Litera kodu lokalizacji EWM → fizyczne miejsce w stosie (JEDNO źródło prawdy).… (+8 more)

### Community 167 - "equipment/models.py"
Cohesion: 0.13
Nodes (13): apply_attachments(), capacity_at(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Parametry sprzętu po osprzęcie: udźwig (i krzywa) pomniejszony o sumę redukcji,…, Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, CatalogMathTests, PlainTestCase (+5 more)

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.24
Nodes (6): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 172 - "warehouse_racktype.py"
Cohesion: 0.33
Nodes (6): _md_role, _planner, require_POST, warehouse_rack_type_delete(), warehouse_rack_type_form(), warehouse_rack_type_list()

### Community 173 - "showcase.js"
Cohesion: 0.16
Nodes (13): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS, camAt(), docksCam(), moveItem(), navigate(), pickCards() (+5 more)

### Community 175 - "test_role_matrix.py"
Cohesion: 0.22
Nodes (7): TestCase, Macierz ról: rola Podgląd nie zmienia danych i nie widzi danych źródłowych…, Widoki odczytu przyjmują POST jak GET (renderują) — liczy się, że nic nie…, _routes(), _url(), ViewerRoleMatrixTests, ViewerSceneTests

### Community 177 - "warehouse_design_day.py"
Cohesion: 0.20
Nodes (9): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, ewm_tasks_profile(), _planner, _int(), ewm_tasks_forecast() (+1 more)

### Community 178 - "views_showcase.py"
Cohesion: 0.24
Nodes (15): _context(), any_role, designer, require_POST, Prezentacje 3D (P1): lista, tworzenie (ze szablonem startowym), odtwarzacz +…, Dane odtwarzacza: scena (layout + działka), miejsca, wyniki (karty KPI, wąskie…, Wszystko, czego potrzebuje odtwarzacz i szablon startowy (jedno źródło)., showcase_create() (+7 more)

### Community 179 - "current_stock_log"
Cohesion: 0.50
Nodes (4): current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., {materiał: palet na aktualnym stanie} — pozycja stanu = jedna paleta (jak w…, _stock_pallets()

### Community 182 - "DockRoleTests"
Cohesion: 0.17
Nodes (3): DockRoleTests, TestCase, SimS3bTests

### Community 183 - "masterdata/views.py"
Cohesion: 0.16
Nodes (15): abc_from_history(), {materiał: A/B/C} z ostatniej segmentacji (Prognozy i ML); {} gdy nie liczona., catalog(), _counts(), demo(), home(), log_detail(), materials() (+7 more)

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "parse_stamp"
Cohesion: 0.26
Nodes (6): _parse_dt(), parse_stamp(), _parse_time(), → (datetime naiwny, czy_ma_czas) albo None; ValueError przy nieczytelnym…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., ValueParsingTests

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "bay_templates.py"
Cohesion: 0.19
Nodes (12): Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role (+4 more)

### Community 197 - "views_compare.py"
Cohesion: 0.08
Nodes (21): compare_columns(), Tabela porównania layout × scenariusz (E7) — czysty Python na zapisanych…, results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`. (+13 more)

### Community 199 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 200 - "WarehouseTaskBatch"
Cohesion: 0.10
Nodes (13): Meta, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTask, WarehouseTaskBatch, ForecastViewTests, TestCase, DemoFileTests, DesignHubTests (+5 more)

### Community 201 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 205 - "roles.py"
Cohesion: 0.07
Nodes (19): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)… (+11 more)

### Community 207 - "layout.py"
Cohesion: 0.12
Nodes (27): attach_equipment(), check_equipment(), clean_columns(), clean_layout(), clean_underlay(), _dock_role(), _fname(), height_kpi() (+19 more)

### Community 208 - "test_ewm_tasks_refresh.py"
Cohesion: 0.40
Nodes (3): MetaRefreshGuardTests, SimpleTestCase, Audyt UX-004 (WCAG 2.2.1): szczegóły importu zadań EWM nie przeładowują się co…

### Community 210 - "ImportViewTests"
Cohesion: 0.31
Nodes (3): ImportViewTests, TestCase, _xlsx()

### Community 215 - "blender_stock.py"
Cohesion: 0.14
Nodes (14): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), _deg(), _half(), load_stock_inputs(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy… (+6 more)

### Community 216 - "demo_scenariusz.py"
Cohesion: 0.17
Nodes (14): assign_classes(), pick_class(), Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co…, Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii…, Najmniejsza klasa systemowa danej kategorii regału (reach/vna), która sięga…, Command, demo_hall(), demo_zones() (+6 more)

## Knowledge Gaps
- **112 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+107 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **45 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `render/views.py`, `masterdata/services.py`, `analyze`, `test_ewm_service.py`, `generate`, `test_warehouse_model_view.py`, `views_play.py`, `BayTemplate`, `test_fleet_catalog.py`, `test_role_matrix.py`, `scenario/views.py`, `views_showcase.py`, `studio/views.py`, `masterdata/views.py`, `test_dane.py`, `scenario/services.py`, `roles.py`, `simulate`, `demo_scenariusz.py`, `shared.py`, `test_model_geometry.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Why does `Scan` connect `Scan` to `warehouse_tasks.py`, `parse_overrides`, `test_ewm_tasks_parser.py`, `ewm_tasks.py`, `parse_row`, `parse_stamp`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `model_racks()` connect `shared.py` to `views_compare.py`, `warehouse_tasks.py`, `warehouse_variants.py`, `test_fleet_catalog.py`, `masterdata/services.py`, `blender_scene.py`, `warehouse_blender.py`, `studio/views.py`, `warehouse_model.py`, `warehouse_variant_edit.py`, `scenario/services.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `Equipment` (e.g. with `CatalogMathTests` and `CatalogViewTests`) actually correct?**
  _`Equipment` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._