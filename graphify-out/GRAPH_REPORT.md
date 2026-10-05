# Graph Report - TWINEMA  (2026-10-05)

## Corpus Check
- 279 files · ~178,543 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 3144 nodes · 6673 edges · 212 communities (160 shown, 52 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 205 edges (avg confidence: 0.54)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e5e6b7d1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- places.py
- day_demand
- equipment/models.py
- export.py
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- masterdata/services.py
- site.py
- blender_scene.py
- test_master_data.py
- analyze
- twinema_design_kit.py
- EwmViewsTests
- ml/views.py
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
- detect
- ewm_service.py
- warehouse_variants.py
- Fleet
- StudioViewTests
- designer
- day-timeline.js
- BayTemplateViewTests
- _inside
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
- VoiceViewTests
- DaneViewTests
- test_dane.py
- synthesize
- test_s3b_views.py
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- LayoutApiTests
- layout-editor.js
- OutboundTests
- EwmTasksPollingTests
- FloorGrid
- FlowSceneEndpointTests
- SiteApiTests
- ewm_demo_tasks.py
- packaging.py
- RackTypeWeightsTests
- addressing.py
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
- design_kpi.py
- test_design_variants.py
- compliance
- test_model_geometry.py
- TWINEMA — założenia master daty i scenariuszy
- 0002_lektor.py
- test_placement.py
- 0002_pole_odkladcze.py
- twinema_render.py
- Equipment
- StudioConfig
- scenario/services.py
- studio/migrations/0001_initial.py
- WarehouseTask
- SlotLocator
- layout-preview.js
- ComputeTests
- Scan
- 0003_render_montaz.py
- warehouse_layout.py
- .slot
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
- rack_corners
- 0002_wydania_obsada.py
- generate
- VariantEditViewTests
- views_play.py
- CalibrationViewTests
- 0003_konstrukcja_hali.py
- 0003_symulacja_dnia.py
- test_sim.py
- 0003_domyslne_nosniki_klasy.py
- compare.py
- 0002_opakowania_nosniki.py
- GeneratorViewTests
- simulate_plan
- MasterDataViewTests
- scene-site.js
- 0005_dzialka.py
- params_for
- test_layout_editor_js.py
- fullscreen.test.mjs
- WarehouseLocationMasterBatch
- map_columns
- masterdata/views.py
- layout.py
- GeometryUploadTests
- demo_hall
- CatalogViewTests
- context_processors.py
- DockRoleTests
- Command
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
- build_plan
- ContainerInboundTests
- ml/services.py
- parse_overrides
- parse_row
- PlayViewTests
- BottleneckTests
- PackagingTests
- Pool
- DesignHubTests
- warehouse_model_copy
- MetaRefreshGuardTests
- ClampTests
- 0005_dni_szczytowe.py

## God Nodes (most connected - your core abstractions)
1. `WarehouseModel` - 43 edges
2. `SlotLocator` - 33 edges
3. `generate()` - 30 edges
4. `simulate()` - 29 edges
5. `LayoutError` - 29 edges
6. `analyze()` - 29 edges
7. `Scenario` - 28 edges
8. `rack_corners()` - 26 edges
9. `clean_layout()` - 26 edges
10. `Equipment` - 25 edges

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

## Communities (212 total, 52 thin omitted)

### Community 0 - "places.py"
Cohesion: 0.20
Nodes (11): dock_role(), needed_roles(), places_from_features(), Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych…, Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`)., features: dicty jak `twin.shared.hall_feature_dict` (kind, label, dock_role,…, Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)., staging_side() (+3 more)

### Community 1 - "day_demand"
Cohesion: 0.15
Nodes (18): arrivals_count(), day_demand(), _hhmm(), peak_concurrency(), _pick(), Plan przyjęć → zapotrzebowanie dnia (czysty Python — bez Django, testowalny bez…, Liczba przyjazdów po wzroście — zaokrąglenie w górę (auto albo jest, albo go…, n przyjazdów równomiernie w oknie [od, do): środki n równych odcinków. (+10 more)

### Community 2 - "equipment/models.py"
Cohesion: 0.14
Nodes (14): capacity_at(), move_minutes(), Katalog sprzętu (K1) — czysty Python, bez Django. • `KINDS` — typy sprzętu;…, Udźwig [kg] na wysokości: nominalny do pierwszego punktu krzywej, potem…, Ruch palety: dojazd pusty + jazda z ładunkiem (po `dist_m` w jedną stronę),…, Katalog sprzętu (K1): klasy systemowe (anonimowe, z migracji) i własne modele…, assign_classes(), pick_class() (+6 more)

### Community 3 - "export.py"
Cohesion: 0.15
Nodes (18): _bytes(), compare_workbook(), Eksport wyników symulacji do xlsx (E8): założenia, KPI, wąskie gardła, obsada,…, run: ScenarioRun; day: ScenarioDay tego wyniku (do obsady z założeń)., columns: [nagłówek kolumny]; rows: `compare.compare_columns`., run_workbook(), _sheet(), cutoff_risk() (+10 more)

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
Nodes (25): _is_shelf(), _Agent, _kpi(), Layout, load_day_tasks(), _manh(), _p95(), _pick() (+17 more)

### Community 8 - "twin/models.py"
Cohesion: 0.05
Nodes (42): Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required(), ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., C1: koszty CAPEX/OPEX — czysta kalkulacja (ręczne przykłady), koszty wyniku…, Flota scenariusza z katalogu sprzętu (K1): czas ruchu palety z parametrów,…, Animacja dnia (S4): miejsca z layoutu, wąskie gardła → miejsca i okna czasu,…, Symulacja dnia w aplikacji (S3a): uruchomienie, wynik na ekranie scenariusza,… (+34 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.10
Nodes (24): missing_required(), Command, BaseCommand, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, current_stock_log(), import_file(), _level_of() (+16 more)

### Community 10 - "site.py"
Cohesion: 0.08
Nodes (38): guess_dock_role(), Rola doku z etykiety (dla doków bez jawnej roli): „kontener” → kontenery,…, _area_m2(), building_height(), building_rect(), check_site(), clean_site(), default_site() (+30 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.07
Nodes (46): Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), rack_axes(), rack_point(), Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access() (+38 more)

### Community 12 - "test_master_data.py"
Cohesion: 0.14
Nodes (13): Carrier, ImportLog, Material, Meta, PalletClass, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik…, Jeden import pliku: rodzaj, wynik i próbka odrzuconych wierszy. Import stanów…, Nośnik (paleta): EUR 120×80 domyślnie, reszta edytowalna. (+5 more)

### Community 13 - "analyze"
Cohesion: 0.15
Nodes (19): analyze(), check_equipment(), check_layout(), _issue(), _name(), Lista problemów: error blokuje zapis, warning tylko ostrzega., Wysokość podnoszenia (błąd) i udźwig na wysokości vs nośność miejsca…, (kpi, issues) — KPI tym samym wzorem co warianty (`design_kpi.compute_kpi`), a… (+11 more)

### Community 14 - "twinema_design_kit.py"
Cohesion: 0.18
Nodes (22): add(), add_block(), _clear(), _coll(), elements(), export_variant(), _geometry(), load_variant() (+14 more)

### Community 16 - "ml/views.py"
Cohesion: 0.17
Nodes (11): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, detail(), home(), _int(), any_role, designer (+3 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.08
Nodes (17): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+9 more)

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
Cohesion: 0.12
Nodes (22): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+14 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "twinema_montage.py"
Cohesion: 0.06
Nodes (32): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, Montaż filmu: pobierz ujęcia i nagrania, wykonaj komendy z…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), run_montage() (+24 more)

### Community 25 - "RenderJob"
Cohesion: 0.12
Nodes (15): Meta, Zlecenia renderu: aplikacja kolejkuje, worker z Blenderem (poza serwerem)…, RenderJob, create(), delete(), jobs(), Meta, any_role (+7 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.20
Nodes (12): backtest(), fit(), forecast(), series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily(), ForecastTests (+4 more)

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
Cohesion: 0.10
Nodes (21): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+13 more)

### Community 31 - "design_day.py"
Cohesion: 0.10
Nodes (22): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, abc_by_hits(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, _abc_xyz(), build_profile(), _groups(), _order_profile() (+14 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "layout-panels.js"
Cohesion: 0.18
Nodes (28): addItems(), change(), deleteSelected(), duplicateSelected(), keyOf(), keysAt(), moveSelected(), rotateSelected() (+20 more)

### Community 34 - "kpi_facts"
Cohesion: 0.11
Nodes (18): clean_draft(), estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy). (+10 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.08
Nodes (23): Następny krok: F6 — szlif (wg burzy mózgów, `docs/PLAN.md` §2.2 i §6), Po stronie właściciela (zanim pierwszy prawdziwy film), Przekazanie — stan projektu i następny krok (F6), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`), 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów) (+15 more)

### Community 36 - "BayTemplate"
Cohesion: 0.09
Nodes (18): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, Named location type template — dimensions apply to all locations with matching…, WarehouseRackType, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests (+10 more)

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "detect"
Cohesion: 0.21
Nodes (15): letter_rank(), parse_code(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), atomic, Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.21
Nodes (15): rack_to_element(), Regał modelu magazynu (dict jak w scenie: width/depth/level_h/n_bays/n_levels,…, _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "Fleet"
Cohesion: 0.24
Nodes (4): Fleet, FleetCatalogTests, FleetChargingTests, TestCase

### Community 42 - "StudioViewTests"
Cohesion: 0.10
Nodes (19): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+11 more)

### Community 43 - "designer"
Cohesion: 0.38
Nodes (11): day_save(), _errors(), outbound_save(), designer, require_POST, _save_formset(), scenario_copy(), scenario_create() (+3 more)

### Community 44 - "day-timeline.js"
Cohesion: 0.09
Nodes (49): createDayPlayer(), fleet(), NO_SHADOW, PARTS, along(), buildTracks(), countersAt(), crewAt() (+41 more)

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "_inside"
Cohesion: 0.19
Nodes (8): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., EquipmentAgentsTests, SimpleTestCase, _rack(), Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "scenario/views.py"
Cohesion: 0.07
Nodes (39): has_role(), True dla superusera albo członka którejś z grup., cartons_per_pallet_hint(), Podpowiedź do normy scenariusza „kartonów na paletę”: średnia ważona liczbą…, Scenariusz referencyjny (syntetyczny, anonimowy): centrum dystrybucyjne z…, check_triples(), InboundStream, Meta (+31 more)

### Community 49 - "resolve_moves"
Cohesion: 0.26
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 50 - "warehouse_blender.py"
Cohesion: 0.12
Nodes (24): default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją). (+16 more)

### Community 51 - "layout-core.js"
Cohesion: 0.14
Nodes (17): axes(), BACK_GAP_M, bbox(), center(), corners(), History, makeBlock(), mode() (+9 more)

### Community 52 - "studio/views.py"
Cohesion: 0.13
Nodes (32): approve(), deck_pdf(), _draft_or_back(), film_file(), model_kpi(), montage_create(), montage_input_key(), montage_ready() (+24 more)

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

### Community 58 - "VoiceViewTests"
Cohesion: 0.24
Nodes (4): fake_tts(), override_settings, TestCase, VoiceViewTests

### Community 59 - "DaneViewTests"
Cohesion: 0.17
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "test_dane.py"
Cohesion: 0.20
Nodes (9): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami:…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, DemoStockTests, SimpleTestCase (+1 more)

### Community 61 - "synthesize"
Cohesion: 0.16
Nodes (14): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, enabled() (+6 more)

### Community 62 - "test_s3b_views.py"
Cohesion: 0.13
Nodes (13): Wynik symulacji dnia scenariusza na modelu hali (S3a): KPI średnia/najgorszy,…, ScenarioRun, S3b w aplikacji: rola doku (pole, migracja, generator, edytor, symulacja),…, _cell(), any_role, designer, require_POST, Symulacja dnia scenariusza na modelu hali (S3a): uruchomienie, karta KPI,… (+5 more)

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
Cohesion: 0.11
Nodes (40): all(), applyIssues(), CFG, check(), drawHall(), drawItem(), el(), fit() (+32 more)

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
Cohesion: 0.18
Nodes (18): cartons_per_pallet(), classify(), pallet_height_cm(), pallet_weight_kg(), Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).…, Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana., Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika., Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad… (+10 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "addressing.py"
Cohesion: 0.16
Nodes (11): _bay_locations(), format_bay_numbers(), make_code(), parse_bay_numbers(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i… (+3 more)

### Community 77 - "test_design_calibration.py"
Cohesion: 0.13
Nodes (15): calibrate(), ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda)., Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu). (+7 more)

### Community 79 - "ScenarioViewTests"
Cohesion: 0.19
Nodes (3): hhmm(), TestCase, ScenarioViewTests

### Community 80 - "studio/models.py"
Cohesion: 0.10
Nodes (16): Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)., Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →… (+8 more)

### Community 82 - "test_addressing.py"
Cohesion: 0.19
Nodes (11): expand_row(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, Numery gniazd rzędu w kolejności fizycznej; pusta reguła = 1..n_bays; nadmiar…, row_bay_numbers(), codes(), ExpandModelTests, ExpandRowTests, ov() (+3 more)

### Community 83 - "equipment/views.py"
Cohesion: 0.18
Nodes (14): _can_edit(), catalog_copy(), catalog_delete(), catalog_detail(), catalog_form(), catalog_list(), _curve(), any_role (+6 more)

### Community 84 - "SimViewTests"
Cohesion: 0.23
Nodes (3): DemoSimTests, TestCase, SimViewTests

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "warehouse_model.py"
Cohesion: 0.15
Nodes (19): Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., save_hall_features(), _f(), _features_data(), model_scene_data(), _parse_pasted_codes(), _md_role, _planner (+11 more)

### Community 87 - "studio/api.py"
Cohesion: 0.16
Nodes (24): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+16 more)

### Community 95 - "shared.py"
Cohesion: 0.09
Nodes (33): load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., load_groups(), load_inputs(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch (+25 more)

### Community 117 - "design_kpi.py"
Cohesion: 0.18
Nodes (17): check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.…, Liczba miejsc paletowych elementu (0 dla transportu/kompletacji)., Rzut obrysu elementu na oś: (początek, koniec) [m]; along=True → szerokość. (+9 more)

### Community 118 - "test_design_variants.py"
Cohesion: 0.15
Nodes (13): anchor_count(), clean_elements(), compute_kpi(), equipment_capacity(), Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.…, Liczba rzeczywistych punktów obsługi (0 → droga liczona od przodu hali)., (punkt przed frontem boku/kanału, liczba miejsc paletowych) dla elementów…, Nominalna wydajność sprzętu wg katalogu, zsumowana per rodzaj elementu. (+5 more)

### Community 119 - "compliance"
Cohesion: 0.29
Nodes (5): compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,…, rows: [{"zone", "rack_id", "has_template"}]; locations/duplicates: wynik…, CompliancePureTests, SimpleTestCase

### Community 120 - "test_model_geometry.py"
Cohesion: 0.14
Nodes (16): Meta, WarehouseModelForm, floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma). (+8 more)

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
Cohesion: 0.16
Nodes (9): CostRate, Equipment, Meta, (od, do) jako float; brak „do” = „od”; brak obu = None., Stawka kosztowa (C1) jako widełki min–max — wartości domyślne syntetyczne,…, _check_range(), EquipmentForm, Meta (+1 more)

### Community 128 - "scenario/services.py"
Cohesion: 0.08
Nodes (35): [(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None,…, weighted_cartons_per_pallet(), cartons_per_pallet_distribution(), [(kartonów/paletę, waga)] z master daty: waga = palet na stanie (albo 1 na…, fleet_from_catalog(), placement_bottlenecks(), Klej Django ↔ symulacja dnia (`scenario.sim` jest czystym Pythonem)., Sprzęt floty z katalogu (K1) → czas ruchu palety na tym layoucie: średnia droga… (+27 more)

### Community 132 - "WarehouseTask"
Cohesion: 0.13
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 133 - "SlotLocator"
Cohesion: 0.14
Nodes (9): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, BuildPalletsTests, ParseCodeTests, SimpleTestCase, Palety w lokalizacjach (stan magazynu) w scenie Blendera —… (+1 more)

### Community 134 - "layout-preview.js"
Cohesion: 0.27
Nodes (11): zoneColors(), S, CFG, createViewer(), initPreview(), MODES, preview3d(), setMode() (+3 more)

### Community 135 - "ComputeTests"
Cohesion: 0.18
Nodes (9): compute(), _item(), mix_days(), Koszty wariantu (C1) — czysty Python: CAPEX layoutu i floty, OPEX roczny pracy…, Dni w roku: [(typ dnia, liczba dni)]. Brak symulacji jednego typu → cały rok z…, rates: {klucz: (od, do)} — `CostRate`; layout: {positions: {reach|vna|shelf:…, _total(), ComputeTests (+1 more)

### Community 136 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 138 - "warehouse_layout.py"
Cohesion: 0.13
Nodes (27): placement_for(), Pojemność vs potrzeba i reguły rozmieszczenia na aktualnym layoucie i stanie…, feature_row(), rack_row(), hall_feature_kinds(), _analyze(), equipment_catalog(), _image_size() (+19 more)

### Community 139 - ".slot"
Cohesion: 0.24
Nodes (6): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 141 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 148 - "StructureApiTests"
Cohesion: 0.23
Nodes (4): png(), override_settings, TestCase, StructureApiTests

### Community 149 - "VariantViewTests"
Cohesion: 0.24
Nodes (3): _el(), TestCase, VariantViewTests

### Community 151 - "layout-site.js"
Cohesion: 0.20
Nodes (17): snap(), svgTransform(), setView(), viewCenter(), h(), num(), AREA_COLORS, AREA_SIZE (+9 more)

### Community 152 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 153 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 154 - "rack_corners"
Cohesion: 0.12
Nodes (23): bbox(), near_pairs(), overlap_depth(), rack_corners(), Głębokość nachodzenia dwóch obróconych prostokątów (narożniki w kolejności…, Pary (i, j), i < j, których obrysy osiowe poszerzone o `pad` się stykają —…, apply_zone_edit(), _box() (+15 more)

### Community 156 - "generate"
Cohesion: 0.13
Nodes (14): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+6 more)

### Community 157 - "VariantEditViewTests"
Cohesion: 0.22
Nodes (3): TestCase, Kopia „przyszłego layoutu” niesie konstrukcję hali z E2b: wysokość, słupy,…, VariantEditViewTests

### Community 158 - "views_play.py"
Cohesion: 0.17
Nodes (14): PlacesTests, SimpleTestCase, bottleneck_focus(), layout_places(), peak_index(), any_role, Animacja dnia scenariusza (S4): scena 3D hali + zdarzenia przebiegu…, features: dicty `hall_feature_dict` (+ słupy), floor {width, depth} → miejsca… (+6 more)

### Community 160 - "0003_konstrukcja_hali.py"
Cohesion: 0.50
Nodes (3): Migration, Istniejące regały półkowe (poziom < 1 m, jak blender_scene.SHELF_LEVEL_M) →…, shelves()

### Community 162 - "test_sim.py"
Cohesion: 0.14
Nodes (23): Silnik zdarzeniowy dnia scenariusza (czysty Python, czas w godzinach od 0:00).…, Symulacja dnia scenariusza na layoucie hali (S3a) — czysty Python, bez Django.…, Zwroty przychodzą w godzinach zmian obsługi zwrotów (bez ostatniej godziny)., returns_window(), run_day(), run_many(), _trouble(), aggregate() (+15 more)

### Community 167 - "simulate_plan"
Cohesion: 0.30
Nodes (7): Docks, plan: `plan.build_plan`; params: normy + flota; shifts: [{process, start_h,…, simulate_plan(), EngineTests, plan(), shifts(), truck()

### Community 168 - "MasterDataViewTests"
Cohesion: 0.17
Nodes (3): MasterDataViewTests, TestCase, SeedAndImportTests

### Community 169 - "scene-site.js"
Cohesion: 0.60
Nodes (4): buildSite(), flat(), GROUND, posts()

### Community 171 - "params_for"
Cohesion: 0.15
Nodes (10): block_rows(), params_for(), Rzędy bloku regałów: lista przesunięć „w głąb" [m] kolejnych rzędów.…, Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., AisleCheckTests, BlenderImportGuardTests, CatalogTests, SimpleTestCase (+2 more)

### Community 172 - "test_layout_editor_js.py"
Cohesion: 0.22
Nodes (8): skipUnless, rack_geom(), Regał edytora → dict sceny (jak `blender_scene.model_racks`) dla geometrii i…, Punkt działki → punkt hali (odwrotność `hall_to_site`; osie ortonormalne)., site_to_hall(), LayoutCoreJsTests, node_eval(), Czyste funkcje JS edytora layoutu (static/twin/js/layout-core.js): testy `node…

### Community 173 - "fullscreen.test.mjs"
Cohesion: 0.33
Nodes (3): bindFullscreenButton(), fullscreenController(), PSEUDO_CLASS

### Community 174 - "WarehouseLocationMasterBatch"
Cohesion: 0.29
Nodes (5): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., WarehouseLocationMasterBatch

### Community 175 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 176 - "masterdata/views.py"
Cohesion: 0.16
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), catalog(), _counts(), demo(), home(), log_detail(), materials() (+7 more)

### Community 177 - "layout.py"
Cohesion: 0.10
Nodes (31): attach_equipment(), clean_columns(), clean_layout(), clean_underlay(), _column_corners(), column_list(), _dock_role(), _fname() (+23 more)

### Community 179 - "demo_hall"
Cohesion: 0.22
Nodes (8): Command, demo_hall(), demo_zones(), atomic, BaseCommand, _r(), Hala z generatora z 3 dokami paletowymi IN (preset ma 1 — przy 16+ autach…, Strefy specjalne demo nad dwiema parami rzędów VNA: ADR (rzędy 1–2) i…

### Community 180 - "CatalogViewTests"
Cohesion: 0.22
Nodes (3): CatalogViewTests, TestCase, SystemClassesTests

### Community 182 - "DockRoleTests"
Cohesion: 0.17
Nodes (3): DockRoleTests, TestCase, SimS3bTests

### Community 185 - "0006_sprzet_z_katalogu.py"
Cohesion: 0.50
Nodes (3): assign(), Migration, Dotychczasowa kategoria regału (reach/vna) → najmniejsza klasa systemowa, która…

### Community 186 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 187 - "0004_rola_doku_nosnosc.py"
Cohesion: 0.50
Nodes (4): fill_roles(), _guess(), Migration, Kopia heurystyki z etykiety (z S3a) z chwili migracji — migracje mają być…

### Community 188 - "_save"
Cohesion: 0.18
Nodes (7): CompareViewTests, TestCase, HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 197 - "views_compare.py"
Cohesion: 0.24
Nodes (11): compare_columns(), results: [ScenarioRun.result] w kolejności kolumn (pierwsza = punkt…, Koszty wyniku symulacji (C1) — liczone przy wyświetleniu, więc zmiana stawek…, run_costs(), _shift_hours(), compare(), _label(), any_role (+3 more)

### Community 198 - "build_plan"
Cohesion: 0.26
Nodes (8): build_plan(), count(), Plan dnia z założeń scenariusza (czysty Python): losowanie min/śr/max i rozkład…, n chwil w oknie [od, do): środki n odcinków ± rozrzut; posortowane., day: {inbound:[stream], outbound:[stream],…, times_in_window(), tri(), PlanTests

### Community 199 - "ContainerInboundTests"
Cohesion: 0.32
Nodes (4): ContainerInboundTests, _items(), SimpleTestCase, _scene()

### Community 200 - "ml/services.py"
Cohesion: 0.31
Nodes (9): Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), Dni z ruchem ≥ WORKDAY_SHARE mediany dni z jakimkolwiek ruchem (rosnąco)., working_days(), Prognoza wzrostu wolumenów z historii zadań EWM (plan 2026-10-02, etap 5) —…, [(poniedziałek tygodnia, suma)] — tylko pełne tygodnie (bez pierwszego i… (+1 more)

### Community 201 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 202 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 208 - "warehouse_model_copy"
Cohesion: 0.50
Nodes (4): _md_role, require_POST, Kopia modelu (hala ze słupami i podkładem, regały, elementy hali) — „przyszły…, warehouse_model_copy()

## Knowledge Gaps
- **108 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Migration`, `Migration` (+103 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **52 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `masterdata/services.py`, `blender_scene.py`, `test_design_calibration.py`, `analyze`, `masterdata/views.py`, `scenario/views.py`, `studio/models.py`, `generate`, `studio/views.py`, `test_model_geometry.py`, `RenderJob`, `rack_corners`, `test_dane.py`, `test_s3b_views.py`, `shared.py`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Why does `Scan` connect `Scan` to `warehouse_tasks.py`, `parse_overrides`, `parse_row`, `map_columns`, `ewm_tasks.py`, `test_ewm_tasks_parser.py`?**
  _High betweenness centrality (0.024) - this node is a cross-community bridge._
- **Why does `Agent` connect `Agent` to `test_design_sim_scene.py`, `blender_scene.py`?**
  _High betweenness centrality (0.021) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 12 inferred relationships involving `LayoutError` (e.g. with `CheckLayoutTests` and `CleanLayoutTests`) actually correct?**
  _`LayoutError` has 12 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _108 weakly-connected nodes found - possible documentation gaps or missing edges._