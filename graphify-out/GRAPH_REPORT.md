# Graph Report - agent-ab76a461212393a56  (2026-10-05)

## Corpus Check
- 182 files · ~103,853 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1980 nodes · 3908 edges · 138 communities (110 shown, 28 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 117 edges (avg confidence: 0.57)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `11a7afaa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- shared.py
- warehouse_model.py
- studio/api.py
- FloorGrid
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- simulate
- twin/models.py
- test_dane.py
- design_kpi.py
- blender_scene.py
- generate
- test_model_edit.py
- params_for
- test_ewm_service.py
- blender_stock.py
- test_design_sim_scene.py
- twinema_design_kit.py
- ValueError
- roles.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- twinema_montage.py
- test_addressing.py
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- test_warehouse_model_view.py
- Agent
- design_day.py
- forecast.py
- masterdata/services.py
- script.py
- TWINEMA — zakres i plan
- BayTemplate
- ParseTests
- warehouse_compare.py
- ewm_service.py
- warehouse_variants.py
- masterdata/views.py
- StudioViewTests
- load_groups
- _feature_center
- BayTemplateViewTests
- _inside
- middleware.py
- SlotLocator
- design_calibration.py
- Scan
- WarehouseTask
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- Przekazanie — stan projektu i następny krok (F5)
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- RenderMontageTests
- resolve_moves
- DaneViewTests
- _save
- VoiceViewTests
- blender_route.py
- pre-push
- test_ml.py
- WarehouseHallFeatureTests
- detect
- VariantViewTests
- addressing.py
- EwmTasksPollingTests
- EwmViewsTests
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- .slot
- RackTypeWeightsTests
- test_ewm_detect.py
- check_aisles
- PROVENANCE.md
- CalibrationViewTests
- studio/models.py
- LoadAndViewTests
- GeneratorViewTests
- segmentation.py
- ewm_tasks.py
- icon
- safe_json
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
- build_pallets
- parse_overrides
- SimulationViewTests
- 0002_lektor.py
- GeneratorTests
- LocationOverride
- twinema_render.py
- any_role
- StudioConfig
- ClampTests
- studio/migrations/0001_initial.py
- parse_row
- VariantEditViewTests
- ProfileTests
- CompareViewTests
- warehouse_model_copy
- 0003_render_montaz.py

## God Nodes (most connected - your core abstractions)
1. `SlotLocator` - 33 edges
2. `WarehouseModel` - 30 edges
3. `simulate()` - 29 edges
4. `build_scene()` - 24 edges
5. `Scan` - 23 edges
6. `Agent` - 22 edges
7. `WarehouseTaskBatch` - 22 edges
8. `model_racks()` - 21 edges
9. `FloorGrid` - 20 edges
10. `params_for()` - 20 edges

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

## Communities (138 total, 28 thin omitted)

### Community 0 - "shared.py"
Cohesion: 0.14
Nodes (22): load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch, hall_feature_dict(), hall_feature_kinds(), Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, Element hali → dict do renderu (kolor rozwiązany, etykieta z rodzaju). (+14 more)

### Community 1 - "warehouse_model.py"
Cohesion: 0.05
Nodes (47): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, rack_corners(), floor_size(), is_geometry_csv(), _num() (+39 more)

### Community 2 - "studio/api.py"
Cohesion: 0.07
Nodes (41): claim(), _claimed_job(), fail(), _forbidden(), require_GET, require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+33 more)

### Community 3 - "FloorGrid"
Cohesion: 0.08
Nodes (14): _dedupe(), FloorGrid, Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., _simplify(), BlenderExportViewTests (+6 more)

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
Cohesion: 0.12
Nodes (15): Meta, WarehouseModelForm, Migration, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, WarehouseHallFeature, WarehouseModel, WarehouseModelRack (+7 more)

### Community 9 - "test_dane.py"
Cohesion: 0.15
Nodes (13): demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, ImportLog, Material, Meta, Dane podstawowe bliźniaka: materiały, stany w lokalizacjach i dziennik… (+5 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.12
Nodes (22): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity() (+14 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.10
Nodes (35): rack_point(), Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), _aisle_m(), build_scene(), _carry(), _container_flow(), _Ctx (+27 more)

### Community 12 - "generate"
Cohesion: 0.28
Nodes (11): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+3 more)

### Community 13 - "test_model_edit.py"
Cohesion: 0.18
Nodes (16): apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.…, {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Pary regałów nachodzących na siebie (obrysy osiowe, tolerancja `tol` m) —… (+8 more)

### Community 14 - "params_for"
Cohesion: 0.15
Nodes (18): _geometry(), block_rows(), element_summary(), footprint(), height(), pallet_positions(), params_for(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+10 more)

### Community 15 - "test_ewm_service.py"
Cohesion: 0.12
Nodes (15): active_master_qs(), Kody lokalizacji magazynu — wspólna konwencja mapy 3D / eksportu SAP. Litera na…, Lokalizacje z aktywnej partii master-daty (pusty queryset, gdy brak partii).…, One import of location master data (height, volume, weight, type)., Master data for a single warehouse location., WarehouseLocationMaster, WarehouseLocationMasterBatch, load_sample() (+7 more)

### Community 16 - "blender_stock.py"
Cohesion: 0.12
Nodes (20): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+12 more)

### Community 17 - "test_design_sim_scene.py"
Cohesion: 0.12
Nodes (13): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+5 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "ValueError"
Cohesion: 0.16
Nodes (23): ValueError, _bool(), _cell(), _code(), _date(), ImportFileError, map_columns(), norm() (+15 more)

### Community 20 - "roles.py"
Cohesion: 0.09
Nodes (13): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, has_role(), True dla superusera albo członka którejś z grup., Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required() (+5 more)

### Community 21 - "test_voice.py"
Cohesion: 0.12
Nodes (22): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+14 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.15
Nodes (18): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+10 more)

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
Nodes (11): _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s, SIM_KEYS (+3 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "test_warehouse_model_view.py"
Cohesion: 0.12
Nodes (10): InstancingGuardTests, TestCase, Regression: warehouse model 3D view used a non-existent `get_item` filter → 500., UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests (+2 more)

### Community 30 - "Agent"
Cohesion: 0.19
Nodes (7): Agent, _r(), Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Agent z osią czasu ruchu: rodzaj z `SPEED` (wózek, pracownik, kombi, AGV, EPT)., Jazda/przejście trasą A* do `target`; trasa trafia też do mapy przepływów.

### Community 31 - "design_day.py"
Cohesion: 0.14
Nodes (19): _abc_xyz(), build_profile(), _groups(), _order_profile(), percentile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:…, Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista… (+11 more)

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "masterdata/services.py"
Cohesion: 0.12
Nodes (20): demo_materials(), Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami., missing_required(), Command, BaseCommand, Pozycja stanu: materiał w lokalizacji (z jednego importu stanów)., StockItem, import_file() (+12 more)

### Community 34 - "script.py"
Cohesion: 0.13
Nodes (15): estimate_seconds(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy)., Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta. (+7 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.11
Nodes (16): 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów), 2.3 Poza zakresem, 2. Zakres, 3. Architektura, 4. Uczenie maszynowe, 5. Studio prezentacji (+8 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "ParseTests"
Cohesion: 0.12
Nodes (7): MapColumnsTests, ParseTests, SimpleTestCase, Parser plików modułu Dane — czysty Python (bez bazy)., Wzór pliku z ekranu Dane musi się importować bez ręcznych poprawek., ReadTableTests, _xlsx()

### Community 38 - "warehouse_compare.py"
Cohesion: 0.19
Nodes (14): _is_shelf(), capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet() (+6 more)

### Community 39 - "ewm_service.py"
Cohesion: 0.10
Nodes (30): atomic, active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), Warstwa ORM nad czystymi modułami adresowania: master EWM, plan modelu, zapis… (+22 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.21
Nodes (15): model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., _comparison(), _get(), _md_role, _planner, require_POST, Wariant jako twinema.design-variant — do dalszej edycji w Blenderze… (+7 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.15
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), demo(), home() (+7 more)

### Community 42 - "StudioViewTests"
Cohesion: 0.09
Nodes (22): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+14 more)

### Community 43 - "load_groups"
Cohesion: 0.40
Nodes (4): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "_inside"
Cohesion: 0.19
Nodes (8): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., EquipmentAgentsTests, SimpleTestCase, _rack(), Paleta przechodzi AGV → kombi w jednym miejscu: między klatkami nie skacze…, Czas klatek palety rośnie: kombi czeka (wait_until), zamiast „cofać" paletę w…, _scene()

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "SlotLocator"
Cohesion: 0.33
Nodes (3): Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, SlotLocatorTests

### Community 49 - "design_calibration.py"
Cohesion: 0.16
Nodes (13): calibrate(), ideal_cycle(), _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda)., Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu). (+5 more)

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "WarehouseTask"
Cohesion: 0.13
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, ForecastViewTests, TestCase

### Community 52 - "studio/views.py"
Cohesion: 0.20
Nodes (22): approve(), _draft_or_back(), model_kpi(), montage_create(), montage_input_key(), montage_ready(), presentation_create(), presentation_delete() (+14 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "Przekazanie — stan projektu i następny krok (F5)"
Cohesion: 0.33
Nodes (5): Następny krok: F5 — Studio prezentacji, Otwarte przy wdrożeniu (po stronie właściciela), Przekazanie — stan projektu i następny krok (F5), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "RenderMontageTests"
Cohesion: 0.20
Nodes (3): override_settings, TestCase, RenderMontageTests

### Community 58 - "resolve_moves"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 59 - "DaneViewTests"
Cohesion: 0.18
Nodes (5): _csv(), DaneViewTests, DemoAndSceneTests, ImportServiceTests, TestCase

### Community 60 - "_save"
Cohesion: 0.43
Nodes (5): HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 61 - "VoiceViewTests"
Cohesion: 0.10
Nodes (18): FakeResp, opener_err(), opener_ok(), override_settings, SimpleTestCase, Klient ElevenLabs — zawsze z podstawionym `opener` (bez sieci)., SynthesizeTests, fake_tts() (+10 more)

### Community 62 - "blender_route.py"
Cohesion: 0.17
Nodes (13): Item, Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze., _at(), container_inbound(), Przyjęcie kontenera z kartonami luzem (plan 2026-10-02, etap 2b) — czysty…, docks: [(środek doku kontenerowego)], stations: [(środek stanowiska…, heading_deg() (+5 more)

### Community 64 - "test_ml.py"
Cohesion: 0.15
Nodes (4): ForecastTests, SimpleTestCase, ML1 prognoza + ML2 segmentacja: czyste moduły, zapis przebiegów, ekrany., SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 66 - "detect"
Cohesion: 0.21
Nodes (15): format_bay_numbers(), letter_rank(), Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu., [10, …, 47, 50] → „10-47,50” (odwrotność parse_bay_numbers)., detect(), _distance(), _grid(), _new_template() (+7 more)

### Community 68 - "addressing.py"
Cohesion: 0.16
Nodes (11): _bay_locations(), make_code(), parse_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Kod EWM → (strefa, przejście, gniazdo, pozycja, litera, połówka) albo None., Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+3 more)

### Community 69 - "EwmTasksPollingTests"
Cohesion: 0.25
Nodes (3): EwmTasksPollingTests, TestCase, Import „w tle” ponad STALE_AFTER = proces padł — polling ma się zatrzymać.

### Community 71 - "FlowSceneEndpointTests"
Cohesion: 0.24
Nodes (3): FlowPlayerPanelTests, FlowSceneEndpointTests, TestCase

### Community 72 - "bay_templates.py"
Cohesion: 0.25
Nodes (10): bay_template_delete(), bay_template_form(), bay_template_list(), _int(), _levels_from_post(), _md_role, _planner, require_POST (+2 more)

### Community 73 - "ewm_demo_tasks.py"
Cohesion: 0.31
Nodes (9): bin_code(), day_tasks(), main(), Demonstracyjny eksport zadań magazynowych EWM (/SCWM/MON) do importu w TWINEMA.…, Zadania jednego dnia: [(rodzaj, materiał, dokument)] w kolejności do rozdania…, `n` chwil potwierdzeń jednego zasobu w zmianie: start + odstępy ~ mean_gap,…, row(), rows_for_day() (+1 more)

### Community 74 - ".slot"
Cohesion: 0.20
Nodes (8): _deg(), _half(), 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code(), Kod → (zone, rack_id, bay, col_idx, level) albo None.

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "test_ewm_detect.py"
Cohesion: 0.23
Nodes (10): expand_model(), [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, DetectHeightsTests, DetectIrregularBayTests, expand_proposal(), master_of(), SimpleTestCase, „Wykryj z EWM”: propozycja szablonów, numeracji i wyjątków z kodów; round-trip… (+2 more)

### Community 77 - "check_aisles"
Cohesion: 0.24
Nodes (7): check_aisles(), Kontrola szerokości alejek między równoległymi elementami składowania.…, AisleCheckTests, BlenderImportGuardTests, SimpleTestCase, _rack(), Blender importuje te moduły bez Django — żadnego importu Django na poziomie…

### Community 79 - "CalibrationViewTests"
Cohesion: 0.22
Nodes (3): CalibrationViewTests, TestCase, _racks()

### Community 80 - "studio/models.py"
Cohesion: 0.10
Nodes (16): Meta, MontageJob, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Długość klipu: nagranie + zapas 0,5 s, w granicach kolejki renderów (2–60 s)., Render pasuje do obecnego presetu i długości kwestii (stan zlecenia osobno)., Montaż filmu (ffmpeg w workerze na PC). Cache: ten sam `input_key` i gotowe →… (+8 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "safe_json"
Cohesion: 0.22
Nodes (10): JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), ewm_tasks_profile(), _planner, _md_role, _planner, require_POST, warehouse_rack_type_delete() (+2 more)

### Community 95 - "warehouse_blender.py"
Cohesion: 0.09
Nodes (34): _activity_picks(), build_scene_for_model(), model_racks(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_stock_inputs(), Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy… (+26 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "test_ewm_tasks_parser.py"
Cohesion: 0.22
Nodes (6): parse_number(), parse_stamp(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., Parser eksportu zadań magazynowych EWM (WT): aliasy nagłówków, liczby, daty,…, ValueParsingTests

### Community 119 - "build_pallets"
Cohesion: 0.19
Nodes (6): build_pallets(), Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests, ParseCodeTests, SimpleTestCase, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…

### Community 120 - "parse_overrides"
Cohesion: 0.28
Nodes (6): map_kind(), parse_overrides(), „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, KindMappingTests, SimpleTestCase

### Community 121 - "SimulationViewTests"
Cohesion: 0.17
Nodes (4): TestCase, TestCase, SimSceneViewTests, SimulationViewTests

### Community 123 - "GeneratorTests"
Cohesion: 0.18
Nodes (3): GeneratorTests, SimpleTestCase, _rect()

### Community 124 - "LocationOverride"
Cohesion: 0.20
Nodes (7): LocationOverride, Meta, Named location type template — dimensions apply to all locations with matching…, Wyjątek adresu: nadpisuje wynik szablonu dla jednego miejsca albo całego…, Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, WarehouseRackType

### Community 125 - "twinema_render.py"
Cohesion: 0.33
Nodes (8): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings()

### Community 126 - "any_role"
Cohesion: 0.25
Nodes (8): film_file(), presentation_list(), any_role, Napisy całej narracji (ujęcia jedno po drugim). Montaż w F5c przesunie je o…, Stan renderów i montażu — strona odpytuje i przeładowuje się, gdy coś się…, status_json(), subtitles(), voice_file()

### Community 132 - "parse_row"
Cohesion: 0.46
Nodes (3): parse_row(), Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;…, RowTests

### Community 136 - "warehouse_model_copy"
Cohesion: 0.50
Nodes (4): _md_role, require_POST, Kopia modelu (regały + elementy hali) — wariant do przeróbek bez ruszania…, warehouse_model_copy()

## Knowledge Gaps
- **46 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+41 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **28 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `shared.py`, `masterdata/services.py`, `studio/api.py`, `warehouse_model.py`, `BayTemplate`, `test_dane.py`, `masterdata/views.py`, `generate`, `test_model_edit.py`, `test_ewm_service.py`, `studio/models.py`, `roles.py`, `studio/views.py`, `LocationOverride`, `test_warehouse_model_view.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Why does `synthesize()` connect `VoiceViewTests` to `twinema_montage.py`, `studio/views.py`?**
  _High betweenness centrality (0.059) - this node is a cross-community bridge._
- **Why does `Api` connect `twinema_montage.py` to `VoiceViewTests`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Scan` (e.g. with `HeaderAliasTests` and `KindMappingTests`) actually correct?**
  _`Scan` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _46 weakly-connected nodes found - possible documentation gaps or missing edges._