# Graph Report - agent-aaeba043c34f1e269  (2026-10-05)

## Corpus Check
- 291 files · ~188,962 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3284 nodes · 6999 edges · 219 communities (168 shown, 51 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 220 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9f0c2e88`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_sim.py
- day_demand
- Equipment
- RenderJob
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- test_showcase.py
- site.py
- blender_scene.py
- test_s3b_views.py
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
- blender_route.py
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
- resolve_moves
- warehouse_blender.py
- layout-core.js
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- build_deck
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- addressing.py
- DaneViewTests
- test_dane.py
- VoiceViewTests
- views_sim.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-editor.js
- simulate_plan
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- rack_corners
- design_calibration.py
- Pochodzenie kodu
- ScenarioViewTests
- Shot
- LoadAndViewTests
- test_addressing.py
- equipment/views.py
- SimViewTests
- icon
- shared.py
- studio/api.py
- CoreConfig
- health
- MasterdataConfig
- MlConfig
- RenderConfig
- fetch_vendor.sh
- TwinConfig
- warehouse_compare.py
- docker-entrypoint.sh
- masterdata/migrations/0001_initial.py
- ml/migrations/0001_initial.py
- render/migrations/0001_initial.py
- design_catalog.py
- design_kpi.py
- test_ewm_tasks_parser.py
- test_model_geometry.py
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- PlacementTests
- 0002_pole_odkladcze.py
- twinema_render.py
- CostRate
- StudioConfig
- required_fleet
- studio/migrations/0001_initial.py
- report.py
- SlotLocator
- layout-preview.js
- test_costs.py
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
- layout-site.js
- test_ewm_detect.py
- ewm_tasks.py
- views/__init__.py
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- build_plan
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- ewm_levels.py
- 0003_domyslne_nosniki_klasy.py
- site.test.mjs
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- equipment/models.py
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- params_for
- test_layout_editor_js.py
- showcase.js
- 0006_prezentacja_3d.py
- ViewerRoleMatrixTests
- scenario/services.py
- warehouse_design_day.py
- views_showcase.py
- EngineTests
- BlenderExportViewTests
- PackagingTests
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
- WarehouseModelRack
- test_container_inbound.py
- WarehouseTaskBatch
- parse_overrides
- CostViewsTests
- PlayViewTests
- DesignHubTests
- context_processors.py
- Command
- layout.py
- MetaRefreshGuardTests
- ShowcaseViewTests
- ImportViewTests
- 0005_dni_szczytowe.py
- compare.py
- ShowcaseForm
- compliance
- WarehouseLocationMasterBatch
- .handle
- 0006_klasy_rynkowe.py
- 0005_osprzet_producent.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 46 edges
2. `SlotLocator` - 33 edges
3. `Equipment` - 31 edges
4. `generate()` - 30 edges
5. `Scenario` - 29 edges
6. `simulate()` - 29 edges
7. `LayoutError` - 29 edges
8. `analyze()` - 29 edges
9. `rack_corners()` - 26 edges
10. `clean_layout()` - 26 edges

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

## Communities (219 total, 51 thin omitted)

### Community 0 - "test_sim.py"
Cohesion: 0.13
Nodes (21): Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), dock_role(), needed_roles() (+13 more)

### Community 1 - "day_demand"
Cohesion: 0.12
Nodes (20): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+12 more)

### Community 2 - "Equipment"
Cohesion: 0.09
Nodes (14): Equipment, (od, do) jako float; brak „do” = „od”; brak obu = None., Parametry robocze (z osprzętem) — jedno źródło dla layoutu i symulacji., assign_classes(), pick_class(), Dobór klasy sprzętu do regałów (generator hali, dane demo) — ta sama reguła co…, Dicty regałów generatora (pola modelu) → ustawia `equipment_model` po kategorii…, Najmniejsza klasa systemowa danej kategorii regału (reach/vna), która sięga… (+6 more)

### Community 3 - "RenderJob"
Cohesion: 0.13
Nodes (14): Meta, RenderJob, create(), delete(), jobs(), Meta, any_role, designer (+6 more)

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
Nodes (26): Najmniejsze k ∈ 1..limit, dla którego `ok(fix(k))`; None, gdy nie pomaga., _smallest(), Gniazdo regału: środek boku `bay_idx` (0..n-1) na poziomie `level` (1 =…, _slot(), _Agent, _kpi(), Layout, _manh() (+18 more)

### Community 8 - "twin/models.py"
Cohesion: 0.07
Nodes (29): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), Macierz ról: rola Podgląd nie zmienia danych i nie widzi danych źródłowych…, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między… (+21 more)

### Community 9 - "test_showcase.py"
Cohesion: 0.16
Nodes (20): _cam(), clean_slides(), _fmt(), _hhmm(), kpi_cards(), ValueError, Prezentacja 3D (P1) — czysty Python (bez Django): walidacja slajdów, karty KPI,…, Podsumowanie z liczb (bez AI). f: positions, need, fill_pct, day („typowym” /… (+12 more)

### Community 10 - "site.py"
Cohesion: 0.09
Nodes (34): overlap_depth(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, guess_dock_role(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…, _area_m2(), building_height(), building_rect(), check_site() (+26 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.07
Nodes (48): heading_deg(), rack_axes(), rack_point(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., Kierunek jazdy w układzie hali [°] (0 = +x, 90 = +y)., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _activity_picks() (+40 more)

### Community 12 - "test_s3b_views.py"
Cohesion: 0.12
Nodes (16): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów). (+8 more)

### Community 13 - "analyze"
Cohesion: 0.11
Nodes (24): analyze(), check_layout(), _issue(), Lista problemów: error blokuje zapis, warning tylko ostrzega., (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a…, CheckLayoutTests, CleanLayoutTests, codes() (+16 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.18
Nodes (22): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+14 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.14
Nodes (13): LocationOverride, Meta, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Master data for a single warehouse location., WarehouseLocationMaster, load_sample(), Syntetyczna próbka mastera lokalizacji (hala B0) dla testów „Wykryj z EWM” i…, [(kod, typ EWM)] — kod B0-<rząd>-<gniazdo><pozycja palety><litera poziomu>. (+5 more)

### Community 16 - "ml/services.py"
Cohesion: 0.14
Nodes (17): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+9 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

### Community 18 - "scene-builder.js"
Cohesion: 0.17
Nodes (22): asphaltTex(), cartonTex(), createViewer(), doorTex(), HATCH, hatchTex(), hex2rgb(), _lblCache (+14 more)

### Community 19 - "masterdata/importers.py"
Cohesion: 0.20
Nodes (19): _bool(), _cell(), _code(), _date(), missing_required(), _num(), parse_location(), parse_material() (+11 more)

### Community 20 - "scene-data.js"
Cohesion: 0.13
Nodes (23): DECOR_FILL, decorParts(), DEFAULT_CLEAR_H, EDGE_KINDS, effectiveQuality(), extents(), FAST_ABOVE, FLAT_KINDS (+15 more)

### Community 21 - "test_voice.py"
Cohesion: 0.08
Nodes (34): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+26 more)

### Community 22 - "equipment/importers.py"
Cohesion: 0.16
Nodes (16): _cols(), _curve(), import_rows(), _num(), parse_file(), parse_row(), Import własnych modeli sprzętu z xlsx/csv (K2) — czysty Python poza zapisem w…, → (wiersze poprawne, odrzucone [(nr wiersza, powód)]). (+8 more)

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

### Community 30 - "blender_route.py"
Cohesion: 0.10
Nodes (19): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+11 more)

### Community 31 - "design_day.py"
Cohesion: 0.11
Nodes (20): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+12 more)

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
Nodes (15): letter_rank(), parse_code(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.11
Nodes (29): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+21 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.15
Nodes (17): clean_elements(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, _comparison(), _get(), _md_role, _planner (+9 more)

### Community 41 - "test_fleet_catalog.py"
Cohesion: 0.17
Nodes (9): move_minutes(), Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, fleet_from_catalog(), Sprzęt floty z katalogu (K1) → czas ruchu palety na tym layoucie: średnia droga…, Fleet, FleetCatalogTests, FleetChargingTests, TestCase (+1 more)

### Community 42 - "draft_script"
Cohesion: 0.19
Nodes (16): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+8 more)

### Community 43 - "scenario/views.py"
Cohesion: 0.14
Nodes (26): has_role(), True dla superusera albo członka którejś z grup., cartons_per_pallet_hint(), Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, _arrival_rows(), day_save(), _errors(), _fc() (+18 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.10
Nodes (44): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+36 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.20
Nodes (7): EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w…, Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/models.py"
Cohesion: 0.08
Nodes (29): demo_zones(), Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…, check_triples(), InboundStream, Meta, OutboundStream, Scenariusz: założenia wolumenów niezależne od layoutu (ten sam scenariusz… (+21 more)

### Community 49 - "resolve_moves"
Cohesion: 0.14
Nodes (9): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), CalibrationViewTests, TestCase, SimpleTestCase, _racks(), ResolveMovesTests, _row() (+1 more)

### Community 50 - "warehouse_blender.py"
Cohesion: 0.12
Nodes (23): default_start(), load_window(), parse_start(), Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, ClampTests, SimpleTestCase (+15 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.20
Nodes (22): approve(), _draft_or_back(), model_kpi(), montage_create(), montage_input_key(), montage_ready(), presentation_create(), presentation_delete() (+14 more)

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
Cohesion: 0.19
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "addressing.py"
Cohesion: 0.14
Nodes (13): _bay_locations(), format_bay_numbers(), make_code(), parse_bay_numbers(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar… (+5 more)

### Community 59 - "DaneViewTests"
Cohesion: 0.18
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "test_dane.py"
Cohesion: 0.20
Nodes (9): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+1 more)

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

### Community 67 - "layout-editor.js"
Cohesion: 0.12
Nodes (33): svgTransform(), all(), applyIssues(), CFG, check(), drawHall(), drawItem(), el() (+25 more)

### Community 68 - "simulate_plan"
Cohesion: 0.15
Nodes (10): cartons_for(), Docks, Pool, Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, Kartonów na paletę z kontenera: z rozkładu master daty [(kartonów, waga)] —…, Ludzie procesu: jeden „slot” na osobę na zmianę, dostępny [początek, koniec).…, simulate_plan() (+2 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 70 - "FloorGrid"
Cohesion: 0.11
Nodes (12): FloorGrid, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, _simplify(), BuildSceneTests, SimpleTestCase (+4 more)

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

### Community 76 - "rack_corners"
Cohesion: 0.18
Nodes (13): bbox(), near_pairs(), rack_corners(), Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, _column_corners(), _box(), collisions(), fit_floor() (+5 more)

### Community 77 - "design_calibration.py"
Cohesion: 0.16
Nodes (13): calibrate(), ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda)., Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu). (+5 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "Shot"
Cohesion: 0.12
Nodes (10): Meta, MontageJob, Presentation, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)., Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →…, Shot (+2 more)

### Community 82 - "test_addressing.py"
Cohesion: 0.23
Nodes (9): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, codes(), ExpandModelTests, ExpandRowTests, ov(), SimpleTestCase, Generator adresów modelu magazynu: szablon gniazda + reguła rzędu + wyjątki… (+1 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.18
Nodes (16): _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list(), _curve(), import_file() (+8 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "shared.py"
Cohesion: 0.11
Nodes (26): letter_level(), Sam numer poziomu 1..5 (``default`` dla nieznanej litery)., hall_feature_kinds(), model_columns(), _parse_location_code(), Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, Słupy hali jako elementy „column” (format hall_feature_dict + `height`) dla…, Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids. (+18 more)

### Community 87 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 95 - "warehouse_compare.py"
Cohesion: 0.14
Nodes (28): model_floor(), model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., variant_row(), load_day_tasks() (+20 more)

### Community 117 - "design_catalog.py"
Cohesion: 0.19
Nodes (14): check_aisles(), element_summary(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji)., Rzut obrysu elementu na oś: (początek, koniec) [m]; along=True → szerokość., Kontrola szerokości alejek między równoległymi elementami składowania.… (+6 more)

### Community 118 - "design_kpi.py"
Cohesion: 0.15
Nodes (18): footprint(), (szerokość wzdłuż osi elementu, głębokość) [m]., anchor_count(), anchors(), _center(), compute_kpi(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i… (+10 more)

### Community 119 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (8): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests, Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…

### Community 120 - "test_model_geometry.py"
Cohesion: 0.13
Nodes (13): floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +…, Najmniejsza hala (szer., głęb.) mieszcząca wszystkie regały + margines. (+5 more)

### Community 121 - "TWINEMA — założenia master daty i scenariuszy"
Cohesion: 0.15
Nodes (12): Cel i odbiorcy, Dodatkowe (runda 3, 9 pytań), Ludzie i czas, Materiał i nośniki, Przyjęcia, Runda 4 — grafika, działka, katalog sprzętu, Scenariusz (niezależny od layoutu), Składowanie i kompletacja (+4 more)

### Community 123 - "PlacementTests"
Cohesion: 0.24
Nodes (9): positions(), Miejsca paletowe regału (jak w KPI wariantów: palet w gnieździe ≈ szerokość /…, codes(), CompareTests, PlacementTests, TestCase, rack(), stock() (+1 more)

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "CostRate"
Cohesion: 0.21
Nodes (9): CostRate, Meta, Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, _check_range(), EquipmentForm, Meta, RateForm, ImportFileError (+1 more)

### Community 128 - "required_fleet"
Cohesion: 0.18
Nodes (8): capacity(), comparison(), Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), CompareTests, SimpleTestCase

### Community 132 - "report.py"
Cohesion: 0.21
Nodes (12): bottlenecks(), hhmm(), p95(), Wyniki przebiegu: oś czasu co 15 min, KPI dnia, agregacja wielu przebiegów…, Reguły wąskich gardeł. rerun(kind, *args) → kpi przebiegu reprezentatywnego ze…, Liczba przedziałów [s, e) aktywnych w chwili t = i·15 min., Surowy przebieg (`engine.simulate_plan`) → {kpi, timeline}., run_report() (+4 more)

### Community 133 - "SlotLocator"
Cohesion: 0.09
Nodes (22): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., abc_by_hits(), build_pallets(), _deg(), _half(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.… (+14 more)

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
Cohesion: 0.12
Nodes (28): placement_for(), Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie…, column_list(), feature_row(), rack_row(), [{x, y, size, ref}] — środki słupów. `ref` = [i, j] dla siatki, ["e", k] dla…, _analyze(), equipment_catalog() (+20 more)

### Community 139 - "masterdata/services.py"
Cohesion: 0.11
Nodes (23): Command, BaseCommand, current_stock_log(), import_file(), _level_of(), load_demo(), Zapis importów do bazy + odczyt danych dla bliźniaka (stany do sceny, grupy do…, Nowy aktywny master lokalizacji (poprzednie nieaktywne) — ten sam, którego… (+15 more)

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 150 - "EwmViewsTests"
Cohesion: 0.15
Nodes (3): EwmViewsTests, TestCase, Kody lokalizacji z mastera EWM to dane źródłowe — Podgląd ich nie widzi…

### Community 151 - "layout-site.js"
Cohesion: 0.17
Nodes (24): snap(), setView(), status(), viewCenter(), CFG, deleteSelectedColumn(), drawColumns(), drawUnderlay() (+16 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 153 - "ewm_tasks.py"
Cohesion: 0.16
Nodes (14): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), parse_number(), parse_row() (+6 more)

### Community 154 - "views/__init__.py"
Cohesion: 0.13
Nodes (15): apply_zone_edit(), {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, zone_summary(), _copy(), ModelEditTests, SimpleTestCase, design_hub() (+7 more)

### Community 156 - "generate"
Cohesion: 0.07
Nodes (24): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+16 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.17
Nodes (15): staging_side(), PlacesTests, SimpleTestCase, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, bottleneck_focus(), layout_places(), peak_index(), any_role (+7 more)

### Community 159 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "ewm_levels.py"
Cohesion: 0.17
Nodes (16): NamedTuple, code_slot(), is_hall_a(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm(), Litera kodu lokalizacji EWM → fizyczne miejsce w stosie (JEDNO źródło prawdy).… (+8 more)

### Community 164 - "site.test.mjs"
Cohesion: 0.33
Nodes (5): ENTER_S, TRAVEL_S, sitePlan(), siteToHall(), SITE

### Community 167 - "equipment/models.py"
Cohesion: 0.18
Nodes (10): apply_attachments(), capacity_at(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Parametry sprzętu po osprzęcie: udźwig (i krzywa) pomniejszony o sumę redukcji,…, Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, AttachmentTests, ParseTests (+2 more)

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.19
Nodes (8): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., BlenderImportGuardTests, CatalogTests, SimpleTestCase, Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 172 - "test_layout_editor_js.py"
Cohesion: 0.22
Nodes (8): skipUnless, rack_geom(), Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, Punkt działki → punkt hali (odwrotność `hall_to_site`; osie ortonormalne)., site_to_hall(), LayoutCoreJsTests, node_eval(), Czyste funkcje JS edytora layoutu (static/twin/js/layout-core.js): testy `node…

### Community 173 - "showcase.js"
Cohesion: 0.16
Nodes (13): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS, camAt(), docksCam(), moveItem(), navigate(), pickCards() (+5 more)

### Community 175 - "ViewerRoleMatrixTests"
Cohesion: 0.22
Nodes (6): TestCase, Widoki odczytu przyjmują POST jak GET (renderują) — liczy się, że nic nie…, _routes(), _url(), ViewerRoleMatrixTests, ViewerSceneTests

### Community 176 - "scenario/services.py"
Cohesion: 0.18
Nodes (15): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, _center(), check_placement(), _inside(), _issue() (+7 more)

### Community 177 - "warehouse_design_day.py"
Cohesion: 0.12
Nodes (17): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), ewm_tasks_profile(), _planner (+9 more)

### Community 178 - "views_showcase.py"
Cohesion: 0.24
Nodes (15): _context(), any_role, designer, require_POST, Prezentacje 3D (P1): lista, tworzenie (ze szablonem startowym), odtwarzacz +…, Dane odtwarzacza: scena (layout + działka), miejsca, wyniki (karty KPI, wąskie…, Wszystko, czego potrzebuje odtwarzacz i szablon startowy (jedno źródło)., showcase_create() (+7 more)

### Community 179 - "EngineTests"
Cohesion: 0.47
Nodes (4): EngineTests, plan(), shifts(), truck()

### Community 182 - "DockRoleTests"
Cohesion: 0.21
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
Cohesion: 0.10
Nodes (28): compare_columns(), results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook() (+20 more)

### Community 198 - "WarehouseModelRack"
Cohesion: 0.18
Nodes (8): demo_hall(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, WarehouseModelRack, Ekran szablonów gniazd (CRUD, role) + kolumny szablon/numeracja/kierunek w…, „Wklej adresy" w Modelu magazynu: wklejona lista adresów jednej alejki/regału →…, _create_from_geometry(), Plik geometrii (np. z rysunku hali): regały od razu z pozycją, kątem i…, warehouse_model_upload()

### Community 199 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 200 - "WarehouseTaskBatch"
Cohesion: 0.12
Nodes (8): MlRunTests, TestCase, Meta, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTask, WarehouseTaskBatch, ForecastViewTests, TestCase

### Community 201 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 207 - "layout.py"
Cohesion: 0.11
Nodes (29): rack_to_element(), Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,…, attach_equipment(), check_equipment(), clean_columns(), clean_layout(), clean_underlay(), _dock_role() (+21 more)

### Community 210 - "ImportViewTests"
Cohesion: 0.31
Nodes (3): ImportViewTests, TestCase, _xlsx()

### Community 213 - "ShowcaseForm"
Cohesion: 0.33
Nodes (4): Prezentacja 3D dla zarządu (P1): model hali (+ działka) i opcjonalnie wynik…, Showcase, Meta, ShowcaseForm

### Community 214 - "compliance"
Cohesion: 0.29
Nodes (5): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, CompliancePureTests, SimpleTestCase

### Community 215 - "WarehouseLocationMasterBatch"
Cohesion: 0.29
Nodes (5): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch

### Community 216 - ".handle"
Cohesion: 0.40
Nodes (4): Command, atomic, BaseCommand, _r()

## Knowledge Gaps
- **113 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+108 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **51 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `RenderJob`, `test_costs.py`, `test_showcase.py`, `masterdata/services.py`, `test_s3b_views.py`, `analyze`, `test_ewm_service.py`, `generate`, `test_warehouse_model_view.py`, `views_play.py`, `BayTemplate`, `test_fleet_catalog.py`, `scenario/views.py`, `scenario/models.py`, `views_showcase.py`, `studio/views.py`, `masterdata/views.py`, `test_dane.py`, `views_sim.py`, `WarehouseModelRack`, `FloorGrid`, `rack_corners`, `shared.py`, `test_model_geometry.py`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Why does `WarehouseTaskBatch` connect `WarehouseTaskBatch` to `warehouse_tasks.py`, `simulate`, `views/__init__.py`, `DesignHubTests`, `ml/services.py`, `test_design_sim_scene.py`, `warehouse_blender.py`, `warehouse_design_day.py`, `test_ewm_tasks_parser.py`, `test_design_forecast.py`, `warehouse_compare.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `StructureApiTests` connect `StructureApiTests` to `twin/models.py`?**
  _High betweenness centrality (0.020) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 15 inferred relationships involving `Equipment` (e.g. with `CatalogMathTests` and `CatalogViewTests`) actually correct?**
  _`Equipment` has 15 INFERRED edges - model-reasoned connections that need verification._
- **Are the 9 inferred relationships involving `Scenario` (e.g. with `DayProfileForm` and `HourField`) actually correct?**
  _`Scenario` has 9 INFERRED edges - model-reasoned connections that need verification._