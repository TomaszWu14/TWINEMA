# Graph Report - TWINEMA  (2026-10-05)

## Corpus Check
- 177 files · ~100,461 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 1890 nodes · 3734 edges · 128 communities (101 shown, 27 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 115 edges (avg confidence: 0.58)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9e2536d7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- warehouse_design_sim.py
- test_model_geometry.py
- api.py
- FloorGrid
- twinema_warehouse_anim.py
- test_foundation.py
- warehouse_tasks.py
- design_sim.py
- twin/models.py
- masterdata/services.py
- design_kpi.py
- blender_scene.py
- generate
- test_model_edit.py
- design_catalog.py
- ewm_service.py
- ml/services.py
- SimSceneTests
- twinema_design_kit.py
- ValueError
- roles.py
- test_voice.py
- ewm_levels.py
- WorkerApiTests
- simulate
- test_addressing.py
- test_design_forecast.py
- flow-player.js
- TasksEndpointAndImportTests
- WarehouseModelViewTests
- Agent
- test_design_day.py
- forecast.py
- warehouse_model.py
- script.py
- TWINEMA — zakres i plan
- BayTemplate
- test_container_inbound.py
- test_design_compare.py
- warehouse_model_ewm.py
- warehouse_variants.py
- masterdata/views.py
- StudioViewTests
- design_day.py
- design_calibration.py
- BayTemplateViewTests
- test_equipment_agents.py
- middleware.py
- SlotLocator
- test_design_calibration.py
- Scan
- SimulationViewTests
- studio/views.py
- CLAUDE.md — TWINEMA
- WarehouseModelPasteTests
- Przekazanie — stan projektu i następny krok (F5)
- ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie
- test_blender_export.py
- resolve_moves
- DaneViewTests
- _save
- VoiceViewTests
- build_scene_for_model
- pre-push
- ForecastTests
- WarehouseHallFeatureTests
- BlenderExportViewTests
- VariantViewTests
- hall_feature_dict
- EwmTasksPollingTests
- EwmViewsTests
- FlowSceneEndpointTests
- bay_templates.py
- ewm_demo_tasks.py
- blender_stock.py
- RackTypeWeightsTests
- params_for
- ForecastViewTests
- PROVENANCE.md
- CalibrationViewTests
- studio/models.py
- LoadAndViewTests
- GeneratorViewTests
- segmentation.py
- ewm_tasks.py
- icon
- shared.py
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
- parse_stamp
- build_pallets
- parse_row
- SimSceneViewTests
- 0002_lektor.py
- StudioConfig
- ClampTests
- studio/migrations/0001_initial.py

## God Nodes (most connected - your core abstractions)
1. `SlotLocator` - 33 edges
2. `simulate()` - 29 edges
3. `WarehouseModel` - 29 edges
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

## Communities (128 total, 27 thin omitted)

### Community 0 - "warehouse_design_sim.py"
Cohesion: 0.14
Nodes (24): model_racks(), Regały WarehouseModel jako dicty w formacie sceny (x, y, width, depth,…, load_inputs(), Agregaty zadań potwierdzonych partii (czas lokalny) — liczone w bazie, nie w…, load_day_tasks(), Zadania potwierdzone w dniu `day` (czas lokalny) jako sekundy od DAY_START_H., Zadania magazynowe EWM (WT) — import z monitora magazynu (/SCWM/MON) do…, WarehouseTaskBatch (+16 more)

### Community 1 - "test_model_geometry.py"
Cohesion: 0.13
Nodes (13): floor_size(), is_geometry_csv(), _num(), parse_geometry_csv(), Geometria regałów z pliku CSV (np. odczytana z rysunku hali) → regały modelu…, Plik geometrii poznajemy po nagłówku (plik kodów lokalizacji go nie ma)., Tekst CSV → (racks, errors). Wiersz z błędem trafia do `errors` (nr linii +…, Najmniejsza hala (szer., głęb.) mieszcząca wszystkie regały + margines. (+5 more)

### Community 2 - "api.py"
Cohesion: 0.09
Nodes (27): require_GET, claim(), _claimed_job(), fail(), _forbidden(), require_POST, API workera renderów. Uwierzytelnienie: nagłówek X-Worker-Token…, Zlecenia „w toku” dłużej niż RENDER_STALE_MIN (worker padł) wracają do kolejki. (+19 more)

### Community 3 - "FloorGrid"
Cohesion: 0.19
Nodes (8): _dedupe(), FloorGrid, Trasa A* (8-sąsiedztwo, bez ścinania narożników regałów) z punktu a do b.…, Usuwa węzły leżące na prostej (zostają tylko zakręty)., Siatka zajętości posadzki: komórka zablokowana, jeśli leży w obrysie regału.…, Najbliższa wolna komórka (BFS od komórki punktu) albo None, gdy hala zapchana., _simplify(), _Ctx

### Community 4 - "twinema_warehouse_anim.py"
Cohesion: 0.14
Nodes (37): _animate_agent(), _animate_item(), _bl(), _box_mesh(), build(), _build_feature(), _build_floor(), _build_pallets() (+29 more)

### Community 5 - "test_foundation.py"
Cohesion: 0.07
Nodes (17): BaseSettings, login_required, model_validator, AccessTests, ConfigTests, GroupContractTests, HealthTests, SimpleTestCase (+9 more)

### Community 6 - "warehouse_tasks.py"
Cohesion: 0.11
Nodes (33): never_cache, load_master_levels(), {kod: poziom} z aktywnego mastera lokalizacji (pusty dict, gdy brak)., location_report(), purge_stale(), Import zadań magazynowych EWM do bazy: `ewm_tasks.Scan` (strumień) →…, Lokalizacje z zadań partii vs regały modelu: ile trafia w gniazda, ile jest…, Porzucone podglądy (nikt nie kliknął „Importuj”) — kasowane po dobie. (+25 more)

### Community 7 - "design_sim.py"
Cohesion: 0.12
Nodes (15): _is_shelf(), _Agent, _kpi(), Layout, _manh(), _p95(), _pick(), Symulacja dnia projektowego na wariancie hali (plan 2026-10-02, etap 3a) —… (+7 more)

### Community 8 - "twin/models.py"
Cohesion: 0.09
Nodes (17): Kolejka renderów: API workera (token, przejęcie, scena, wynik) i ekran zleceń., Meta, WarehouseModelForm, Migration, Modele cyfrowego bliźniaka magazynu: typy regałów, master lokalizacji, szablony…, Element hali, którego siatka regałów nie odwzoruje: dok, brama, korytarz,…, WarehouseHallFeature, WarehouseModel (+9 more)

### Community 9 - "masterdata/services.py"
Cohesion: 0.09
Nodes (30): demo_materials(), demo_stock(), material_codes(), Dane demonstracyjne (syntetyczne): materiały zgodne z `tools/ewm_demo_tasks.py`…, Wiersze materiałów (dicty pól Material) z losowymi, ale wiarygodnymi wymiarami., Pozycje stanu dla regałów modelu: ~`fill` miejsc zajętych, materiały wg rotacji…, Command, BaseCommand (+22 more)

### Community 10 - "design_kpi.py"
Cohesion: 0.14
Nodes (18): anchor_count(), anchors(), _center(), clean_elements(), compute_kpi(), equipment_capacity(), Wskaźniki wariantu projektu magazynu (czysty Python — testowalny bez bazy i…, Walidacja elementów z pliku: znany rodzaj, liczby, parametry przez params_for.… (+10 more)

### Community 11 - "blender_scene.py"
Cohesion: 0.12
Nodes (32): heading_deg(), rack_corners(), rack_point(), Geometria i trasowanie dla eksportu animacji przepływów do Blendera. Czysty…, Kierunek jazdy w układzie hali [°] (0 = +x, 90 = +y)., Punkt hali: `along` [m] wzdłuż szerokości, `across` [m] wzdłuż głębokości…, _access(), build_scene() (+24 more)

### Community 12 - "generate"
Cohesion: 0.13
Nodes (14): _docks(), _feature(), generate(), _pair_pitch(), _rack(), Generator hali od parametrów — nowy magazyn „od zera” (plan 2026-10-02, etap…, Poziomy składowania z podłogą: góra najwyższej palety ≤ wysokość − tryskacze., [korytarz][A|B][korytarz]… — y każdego rzędu; A patrzy na korytarz przed, B za. (+6 more)

### Community 13 - "test_model_edit.py"
Cohesion: 0.10
Nodes (22): apply_zone_edit(), _box(), collisions(), fit_floor(), Edycja wariantu hali blokami (plan 2026-10-02, etap 4) — czysty Python.…, {strefa: liczba rzędów, gniazd w rzędzie (maks.), poziomy (maks.)} dla…, Zmienia regały strefy w miejscu (dicty jak `model_racks`) i zwraca listę…, Pary regałów nachodzących na siebie (obrysy osiowe, tolerancja `tol` m) —… (+14 more)

### Community 14 - "design_catalog.py"
Cohesion: 0.12
Nodes (22): _geometry(), block_rows(), check_aisles(), element_summary(), footprint(), height(), pallet_positions(), Katalog elementów do projektowania wariantów magazynu — JEDNO źródło prawdy.… (+14 more)

### Community 15 - "ewm_service.py"
Cohesion: 0.06
Nodes (32): Nowy aktywny master lokalizacji (poprzednie nieaktywne) — ten sam, którego…, _save_locations(), _bay_locations(), make_code(), Adresy miejsc paletowych modelu magazynu: szablon gniazda + reguła rzędu +…, Miejsca jednego gniazda (numer `bay`, fizyczny indeks `slot`) wg szablonu i…, compliance(), Raport zgodności modelu z EWM: kody z planu (expand_model) vs kody z mastera,… (+24 more)

### Community 16 - "ml/services.py"
Cohesion: 0.14
Nodes (17): Meta, ModelRun, Przebiegi modeli ML: wersja algorytmu, dane wejściowe, parametry, miary i wynik…, Przebiegi ML na imporcie zadań: dane z bliźniaka → czyste moduły…, run_forecast(), run_segmentation(), _user(), detail() (+9 more)

### Community 17 - "SimSceneTests"
Cohesion: 0.12
Nodes (10): build_sim_scene(), CorridorRouter, _pick_time(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b) — czysty Python.…, Trasa „jak w magazynie”: wzdłuż korytarza do przejazdu poprzecznego, nim do…, Chwila przejęcia ładunku: kombi rusza wcześniej niż AGV, ale paletę bierze po…, Przebiegi rozpoczęte w godzinie `hour` (zegar 5–21). Zwraca (przebiegi, ile…, window_legs() (+2 more)

### Community 18 - "twinema_design_kit.py"
Cohesion: 0.19
Nodes (21): add(), add_block(), _clear(), _coll(), elements(), export_variant(), load_variant(), _make() (+13 more)

### Community 19 - "ValueError"
Cohesion: 0.06
Nodes (41): apply_preset(), _key(), main(), TWINEMA → Blender: render ujęcia (preset kamery) ze sceny „twinema.scene”.…, FFmpeg H.264 w MP4 — Blender 5 przeniósł format wideo do `media_type`., Ustawia „Kamerę TWINEMA” i jej cel wg presetu na klatkach 1…frames., render(), _video_settings() (+33 more)

### Community 20 - "roles.py"
Cohesion: 0.13
Nodes (9): Flagi ról do szablonów — jedno zapytanie zamiast wielu has_role()., user_roles(), Command, BaseCommand, has_role(), True dla superusera albo członka którejś z grup., Dekorator: wymaga zalogowania + członkostwa w grupie (superuser zawsze…, role_required() (+1 more)

### Community 21 - "test_voice.py"
Cohesion: 0.11
Nodes (24): align(), AlignmentTests, CueTests, TestCase, Czysta logika lektora: hash cache, długość, słowa, plansze napisów, SRT., Sztuczne wyrównanie: każdy znak trwa per_char sekund., SrtTests, VoiceKeyTests (+16 more)

### Community 22 - "ewm_levels.py"
Cohesion: 0.15
Nodes (18): NamedTuple, code_slot(), is_hall_a(), letter_level(), letter_slot(), LetterSlot, level_height_keys(), level_height_mm() (+10 more)

### Community 23 - "WorkerApiTests"
Cohesion: 0.16
Nodes (4): override_settings, TestCase, RenderScreenTests, WorkerApiTests

### Community 24 - "simulate"
Cohesion: 0.18
Nodes (11): Mnożnik wzrostu: > 1 dokłada losowe kopie zadań (czas ±15 min), < 1 losowo…, tasks: [(sekunda od DAY_START, rodzaj, materiał, dokument)]; fleet: {"agv": n,…, scale_tasks(), simulate(), SimpleTestCase, Symulacja dnia projektowego na hali z generatora (plan 2026-10-02, etap 3a)., _busiest_hour(), Animacja godziny z symulacji dnia (plan 2026-10-02, etap 3b). (+3 more)

### Community 25 - "test_addressing.py"
Cohesion: 0.07
Nodes (39): expand_model(), expand_row(), format_bay_numbers(), letter_rank(), parse_code(), Rząd + szablon domyślny + wyjątki → lista miejsc (dict). Klucze: code, bay,…, [(rząd, szablon, wyjątki), …] → (miejsca z kluczami zone/aisle, {kod: [„B0-07”,…, Klucz sortowania liter poziomów: znane litery wg LETTER_ORDER, obce na końcu. (+31 more)

### Community 26 - "test_design_forecast.py"
Cohesion: 0.20
Nodes (12): backtest(), fit(), forecast(), series: [(dzień porządkowy, wartość)] → (nachylenie log/tydzień, wyraz wolny,…, MAPE [%] prognozy ostatnich `weeks` tygodni z modelu uczonego bez nich (None —…, Wzrost per strumień: roczne tempo P50/P90, mnożnik na `years` lat, MAPE testu…, _daily(), ForecastTests (+4 more)

### Community 27 - "flow-player.js"
Cohesion: 0.10
Nodes (11): _e, FLOW_LABELS, FLOW_Y, _m, _p, _q, _s, SIM_KEYS (+3 more)

### Community 28 - "TasksEndpointAndImportTests"
Cohesion: 0.15
Nodes (4): override_settings, TestCase, Duży plik → import w wątku w tle (bez blokowania żądania), partia kończy się…, TasksEndpointAndImportTests

### Community 29 - "WarehouseModelViewTests"
Cohesion: 0.11
Nodes (9): InstancingGuardTests, TestCase, UX #5: widok 3D nie może cicho paść czarnym ekranem — spinner + guard WebGL +…, Regresja bezpieczeństwa: wolny tekst pól regału/elementu (zone/rack_id/label)…, Regresja: FLOOR_W/FLOOR_D w JS muszą mieć KROPKĘ dziesiętną, nie polski…, R1: stal regałów renderowana przez InstancedMesh (3 draw calle), nie per-mesh.…, StoredXSSGuardTests, ViewFloatLocalizationTests (+1 more)

### Community 30 - "Agent"
Cohesion: 0.11
Nodes (17): Agent, Item, _r(), Osie czasu agentów (wózki widłowe, ludzie) i ładunków (palety, kartony) dla…, Postój do chwili `t` (realny znacznik zadania); zajęty agent nie cofa się w…, Przejęcie ładunku: klatka „na miejscu" → po `handling` s ładunek jest na…, Odłożenie ładunku w `pos` na wysokości `z` (np. gniazdo regału albo dok)., Ładunek: paleta albo karton. `appear`/`vanish` sterują widocznością w Blenderze. (+9 more)

### Community 31 - "test_design_day.py"
Cohesion: 0.16
Nodes (8): percentile(), Percentyl z interpolacją liniową (jak numpy/Excel PERCENTILE.INC); pusta lista…, _daily(), PercentileTests, ProfileTests, SimpleTestCase, Profil ruchów i dzień projektowy (krok 3): percentyle, dni robocze, dzień…, WorkingDaysTests

### Community 32 - "forecast.py"
Cohesion: 0.16
Nodes (13): candidates(), _demo(), evaluate(), fit(), _grid(), mape(), ML1 — prognoza tygodniowych wolumenów: kilka modeli wygładzania wykładniczego…, Najlepsze parametry modelu na serii `y` → (params, fitted, prognoza h→v, sd… (+5 more)

### Community 33 - "warehouse_model.py"
Cohesion: 0.13
Nodes (21): parse_bay_numbers(), „10-47,50” → [10, …, 47, 50]. Pusty tekst → []. Błędny zapis → ValueError., Numeracja gniazd rzędu: zakresy „10-47,50”., validate_bay_numbers(), WarehouseModelRack, _parse_location_code(), Zapis edytowalnej tabeli elementów hali z równoległych list POST + deleted_ids., B0-01-300A → (zone, rack, bay, level_letter, level_num). (+13 more)

### Community 34 - "script.py"
Cohesion: 0.13
Nodes (16): clean_draft(), _get(), kpi_facts(), _num(), Scenariusz prezentacji (czysty Python — bez Django i bez sieci). • `kpi_facts`…, Liczba po polsku: spacja tysięcy, przecinek dziesiętny., Zdania z liczbami wariantu. Brak wartości → zdanie pominięte (nie zgadujemy)., Szkic bez AI — działa zawsze, także bez klucza API. Do edycji przez projektanta. (+8 more)

### Community 35 - "TWINEMA — zakres i plan"
Cohesion: 0.11
Nodes (16): 1. Decyzje, 2.1 MVP, 2.2 Po MVP (wsad do burzy mózgów), 2.3 Poza zakresem, 2. Zakres, 3. Architektura, 4. Uczenie maszynowe, 5. Studio prezentacji (+8 more)

### Community 36 - "BayTemplate"
Cohesion: 0.16
Nodes (7): BayTemplate, Szablon gniazda (słupa regału): belka, palety na belce, poziomy od podłogi w…, BayTemplateTests, levels(), TestCase, RackRuleAndOverrideTests, Modele części 1: szablon gniazda (walidacja), reguła rzędu, wyjątki…

### Community 37 - "test_container_inbound.py"
Cohesion: 0.22
Nodes (8): outward(), Kierunek „na zewnątrz hali” od elementu przy ścianie: normalna najbliższej…, ContainerInboundTests, _f(), _items(), SimpleTestCase, Przyjęcie kontenera w animacji (plan 2026-10-02, etap 2b): kontener przy doku →…, _scene()

### Community 38 - "test_design_compare.py"
Cohesion: 0.19
Nodes (11): capacity(), comparison(), Porównanie wariantów hali na tym samym dniu projektowym (plan 2026-10-02, etap…, Miejsca paletowe (regały nie-półkowe), lokalizacje kartonowe (półki K1), bramy,…, Symulacja z flotą sugerowaną przez poprzedni przebieg, aż flota się ustali (≤…, [{wiersz KPI z wartościami per wariant + najlepszy}] dla tabeli., required_fleet(), variant_row() (+3 more)

### Community 39 - "warehouse_model_ewm.py"
Cohesion: 0.10
Nodes (29): atomic, active_master(), apply_proposal(), compliance_for_model(), detect_for_model(), master_rows(), plan_for_model(), Aktywny (najnowszy) import mastera lokalizacji albo None. (+21 more)

### Community 40 - "warehouse_variants.py"
Cohesion: 0.16
Nodes (17): model_floor(), Hala co najmniej tak duża, jak obrys regałów (dane bywają „poza halą")., Wariant projektu magazynu: elementy z katalogu `twin.design_catalog` (regały,…, WarehouseDesignVariant, _comparison(), _get(), _md_role, _planner (+9 more)

### Community 41 - "masterdata/views.py"
Cohesion: 0.15
Nodes (15): Wzór pliku: nagłówki (pierwszy alias = polska nazwa) — do pobrania z ekranu…, template_csv(), current_stock_log(), Najnowszy import stanów = aktualny stan magazynu (None, gdy brak)., Pozycje stanu jako dicty `build_pallets`: location, hu, sku, name, lot, expiry,…, stock_for_scene(), demo(), home() (+7 more)

### Community 42 - "StudioViewTests"
Cohesion: 0.10
Nodes (20): BaseModel, draft_script(), enabled(), Exception, Szkic scenariusza z Claude API. Do modelu trafiają WYŁĄCZNIE zdania z…, Błąd do pokazania użytkownikowi (bez szczegółów technicznych)., facts: lista zdań z liczbami → (shots, ostrzeżenia). Rzuca ScriptAIError., ScriptAIError (+12 more)

### Community 43 - "design_day.py"
Cohesion: 0.18
Nodes (15): groups_for(), {materiał: grupa towarowa} albo None, gdy materiałów jeszcze nie zaimportowano.…, _abc_xyz(), build_profile(), _groups(), _order_profile(), Profil ruchów i dzień projektowy z zadań EWM (spec projektowania magazynu, krok…, daily: {data: {rodzaj: n, "orders": n}}; hourly: {(data, godzina): {rodzaj:… (+7 more)

### Community 44 - "design_calibration.py"
Cohesion: 0.32
Nodes (6): _feature_center(), Środek elementu hali (narożnik + obrót jak w three.js)., _manh(), _point(), Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6) — czysty Python.…, Koniec ruchu z `resolve_moves` → (punkt na posadzce, wysokość gniazda).

### Community 45 - "BayTemplateViewTests"
Cohesion: 0.20
Nodes (4): BayTemplateViewTests, CoordsRuleColumnsTests, level_post(), TestCase

### Community 46 - "test_equipment_agents.py"
Cohesion: 0.15
Nodes (11): _aisle_m(), Najwęższy korytarz przy regale: po każdej stronie najbliższy równoległy regał…, _span(), _vna_racks(), EquipmentAgentsTests, SimpleTestCase, _rack(), Sprzęt nowego magazynu w animacji (plan 2026-10-02, etap 2): AGV + kombi w… (+3 more)

### Community 47 - "middleware.py"
Cohesion: 0.13
Nodes (9): client_ip(), Middleware przekrojowe: identyfikator żądania (korelacja logów) + nagłówki…, Dopisuje `record.request_id` z bieżącego żądania ("-" poza żądaniem)., Bierze X-Request-ID od proxy albo nadaje nowy; odsyła go w odpowiedzi., Permissions-Policy + Content-Security-Policy (domyślnie report-only)., IP klienta dla django-axes za jednym zaufanym proxy (Traefik/Coolify): ostatni…, RequestIDLogFilter, RequestIDMiddleware (+1 more)

### Community 48 - "SlotLocator"
Cohesion: 0.17
Nodes (8): _inside(), Czy punkt leży w obrysie regału poszerzonym o `margin` [m]., Kod lokalizacji → gniazdo w regale modelu (środek palety, wysokość, obrót).…, SlotLocator, ParseCodeTests, SimpleTestCase, Palety w lokalizacjach (stan magazynu) w scenie Blendera —…, SlotLocatorTests

### Community 49 - "test_design_calibration.py"
Cohesion: 0.16
Nodes (11): calibrate(), ideal_cycle(), Czas cyklu wg fizyki symulacji: dojazd prev → src, chwyt, przewóz src → dst,…, rows: krotki `blender_tasks.ROW_FIELDS` jednego dnia (rosnąco po potwierdzeniu)., CalibrationTests, SimpleTestCase, Kalibracja symulacji na obecnej hali (plan 2026-10-02, etap 6)., Wózek przewozi palety między dwoma gniazdami co `gap_s` sekund. (+3 more)

### Community 50 - "Scan"
Cohesion: 0.23
Nodes (5): Przebieg po pliku: nagłówek → mapowanie kolumn → wiersze sparsowane albo błędy,…, Poprawne, nieanulowane zadania (dicty pól modelu)., [(etykieta pola, nagłówek z pliku)] w kolejności pól., Scan, ScanFileTests

### Community 51 - "SimulationViewTests"
Cohesion: 0.13
Nodes (6): MlRunTests, TestCase, Meta, WarehouseTask, TestCase, SimulationViewTests

### Community 52 - "studio/views.py"
Cohesion: 0.19
Nodes (21): approve(), _draft_or_back(), model_kpi(), presentation_create(), presentation_delete(), presentation_detail(), presentation_list(), any_role (+13 more)

### Community 53 - "CLAUDE.md — TWINEMA"
Cohesion: 0.33
Nodes (5): CLAUDE.md — TWINEMA, Git, Graphify query-first, Testy (przed każdym PR), Zasady

### Community 55 - "Przekazanie — stan projektu i następny krok (F5)"
Cohesion: 0.33
Nodes (5): Następny krok: F5 — Studio prezentacji, Otwarte przy wdrożeniu (po stronie właściciela), Przekazanie — stan projektu i następny krok (F5), Stan, Zasady repo (skrót — pełne w `CLAUDE.md`)

### Community 56 - "ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie"
Cohesion: 0.40
Nodes (4): ADR-0001: Kopia kodu modelowania magazynu, nie przeniesienie, Decyzja, Kontekst, Skutki

### Community 57 - "test_blender_export.py"
Cohesion: 0.18
Nodes (8): rack_axes(), (u_w, u_d) — jednostkowe osie szerokości i głębokości regału w układzie hali., BuildSceneTests, SimpleTestCase, _rack(), Eksport modelu magazynu do animacji przepływów w Blenderze (tools/blender/)., RouteGeometryTests, _scene()

### Community 58 - "resolve_moves"
Cohesion: 0.29
Nodes (6): Wiersze WT (krotki ROW_FIELDS, rosnąco po potwierdzeniu) → (ruchy, pominięte).…, resolve_moves(), SimpleTestCase, ResolveMovesTests, _row(), SceneFromTasksTests

### Community 59 - "DaneViewTests"
Cohesion: 0.21
Nodes (3): _csv(), DaneViewTests, ImportServiceTests

### Community 60 - "_save"
Cohesion: 0.18
Nodes (7): CompareViewTests, TestCase, HallGeneratorForm, _initial(), _md_role, _save(), warehouse_model_generator()

### Community 61 - "VoiceViewTests"
Cohesion: 0.07
Nodes (25): Api, find_blender(), main(), Worker renderów TWINEMA — uruchamiany na komputerze z Blenderem (np. z GPU).…, BLENDER_BIN / --blender → PATH → typowe katalogi instalacji (najnowsza wersja)., run_job(), FakeResp, opener_err() (+17 more)

### Community 62 - "build_scene_for_model"
Cohesion: 0.22
Nodes (8): _activity_picks(), build_scene_for_model(), Aktywność pickerów (picker, kod, materiał; kolejność = confirmed_at) → trasy.…, Scena dla `WarehouseModel`. `batch` = PickerActivityBatch (None → demo…, load_stock_inputs(), Dane do `build_pallets`: (wiersze migawki, stany, aktywność). Stany = najnowszy…, Opis źródła wózków do `scene.source` (odtwarzacz pokazuje go pod animacją)., window_source()

### Community 64 - "ForecastTests"
Cohesion: 0.17
Nodes (3): ForecastTests, SimpleTestCase, SegmentationTests

### Community 65 - "WarehouseHallFeatureTests"
Cohesion: 0.23
Nodes (3): TestCase, rows: lista dictów pól równoległych → payload z listami., WarehouseHallFeatureTests

### Community 68 - "hall_feature_dict"
Cohesion: 0.29
Nodes (8): hall_feature_dict(), hall_feature_kinds(), Element hali → dict do renderu (kolor rozwiązany, etykieta z rodzaju)., _features_data(), _planner, Elementy hali → lista dictów do renderu (współdzielony hall_feature_dict)., warehouse_model_list(), warehouse_model_view()

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

### Community 74 - "blender_stock.py"
Cohesion: 0.20
Nodes (9): _deg(), _half(), Rzeczywiste palety w lokalizacjach → scena Blendera („cyfrowe zdjęcie"…, 1/2 dla połówki miejsca (kod z końcówką -1/-2, np. B0-07-300C-1), inaczej 0.…, dict gniazda: x, y, z (dół palety), heading, rozmiar [w, d] (+ half 1/2) albo…, Na ile części (w pionie) dzielony jest otwór poziomu danej półki; całe miejsce…, shelves_in_opening(), parse_code() (+1 more)

### Community 75 - "RackTypeWeightsTests"
Cohesion: 0.20
Nodes (3): TestCase, RackTypeWeightsTests, Typy regałów A/B/C/D: nośność per poziom (level_weights) — zapis w edytorze,…

### Community 76 - "params_for"
Cohesion: 0.43
Nodes (3): params_for(), Parametry elementu: domyślne z katalogu + nadpisania (tylko znane klucze)., CatalogTests

### Community 80 - "studio/models.py"
Cohesion: 0.13
Nodes (11): Meta, Presentation, Studio prezentacji: film o modelu hali składany z ujęć (preset kamery + kwestia…, Nagranie pasuje do obecnego tekstu i głosu (po poprawce kwestii — nieaktualne)., Nagranie lektora — cache po hashu (tekst + głos + model), współdzielony między…, Shot, VoiceTrack, estimate_seconds() (+3 more)

### Community 83 - "segmentation.py"
Cohesion: 0.23
Nodes (12): _demo(), _dist2(), features(), kmeans(), _name(), ML2 — segmentacja materiałów pod rozmieszczenie (slotting): k-means na profilu…, {materiał: {hits, cv, active, volume?}} — tylko materiały z ruchem., k-means++ → (przypisania, centroidy, inercja). Deterministyczne dla danego… (+4 more)

### Community 84 - "ewm_tasks.py"
Cohesion: 0.18
Nodes (13): _delimiter(), _encoding(), is_cancelled(), iter_table(), kind_from_word(), norm_header(), _parse_dt(), _parse_time() (+5 more)

### Community 85 - "icon"
Cohesion: 0.40
Nodes (4): simple_tag, icon(), Tagi szablonów modułu: ikony Lucide ze sprite'a static/twin/icons/lucide.svg., {% icon "package" %} → dekoracyjna (aria-hidden); z label → role=img + aria-…

### Community 86 - "shared.py"
Cohesion: 0.14
Nodes (15): load_groups(), {materiał z zadań: grupa towarowa} z modułu Dane; None, gdy materiałów jeszcze…, Wspólne importy i pomocnicze widoków bliźniaka — odpowiednik jądra widoków ze…, JSON bezpieczny do osadzenia w <script> przez |safe (escapuje <, >, & i…, safe_json(), design_hub(), _planner, ewm_tasks_profile() (+7 more)

### Community 95 - "warehouse_blender.py"
Cohesion: 0.15
Nodes (20): default_start(), load_window(), parse_start(), Wózki w animacji z realnych zadań magazynowych EWM (WT) zamiast symulacji demo.…, Początek pierwszej pełnej godziny z zadaniami partii (czas lokalny)., „2026-03-02T06:00” (input datetime-local, czas lokalny) → datetime ze strefą…, Zadania partii potwierdzone w oknie [start, start + hours) — najwyżej `limit`…, _clamped() (+12 more)

### Community 117 - "map_columns"
Cohesion: 0.24
Nodes (7): map_columns(), missing_required(), {pole: indeks kolumny}. Najpierw dokładne aliasy, potem nagłówek zaczynający…, DemoFileTests, SimpleTestCase, Zakładka „Projektowanie magazynu” w Magazyn 3D + plik demonstracyjny WT…, HeaderAliasTests

### Community 118 - "parse_stamp"
Cohesion: 0.36
Nodes (3): parse_stamp(), Data (+ osobny czas, jak w eksporcie SAP) → datetime ze strefą `tz` albo None., ValueParsingTests

### Community 119 - "build_pallets"
Cohesion: 0.32
Nodes (5): abc_by_hits(), build_pallets(), Klasa ABC wg udziału w pobraniach (ta sama reguła progów co…, Czysta funkcja: dane wejściowe jako proste krotki/dicty → (pallets, stats,…, BuildPalletsTests

### Community 120 - "parse_row"
Cohesion: 0.15
Nodes (12): map_kind(), parse_number(), parse_overrides(), parse_row(), „1.234,5” / „1,234.5” / „1 234,5” / „5-” (minus SAP na końcu) / liczba → float;…, „2010 = wydanie” (linia na proces) → ({proces: rodzaj}, [błędy])., Rodzaj procesu mag. → rodzaj ruchu. Kolejność: nadpisania → słownik wyjątków →…, Wiersz → dict pól `WarehouseTask` (+ `cancelled`); None = pusty wiersz;… (+4 more)

## Knowledge Gaps
- **45 isolated node(s):** `docker-entrypoint.sh script`, `Migration`, `Migration`, `Meta`, `Migration` (+40 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **27 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `WarehouseModel` connect `twin/models.py` to `test_model_geometry.py`, `api.py`, `BayTemplate`, `masterdata/services.py`, `StudioViewTests`, `masterdata/views.py`, `generate`, `test_model_edit.py`, `ewm_service.py`, `test_design_calibration.py`, `studio/views.py`, `shared.py`, `test_blender_export.py`, `VoiceViewTests`?**
  _High betweenness centrality (0.073) - this node is a cross-community bridge._
- **Why does `SlotLocator` connect `SlotLocator` to `warehouse_design_sim.py`, `warehouse_tasks.py`, `twin/models.py`, `blender_stock.py`, `CalibrationViewTests`, `test_design_calibration.py`, `build_pallets`, `resolve_moves`, `TasksEndpointAndImportTests`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `model_racks()` connect `warehouse_design_sim.py` to `warehouse_tasks.py`, `warehouse_variants.py`, `masterdata/services.py`, `blender_scene.py`, `test_model_edit.py`, `studio/views.py`, `build_scene_for_model`, `warehouse_blender.py`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Are the 8 inferred relationships involving `SlotLocator` (e.g. with `BuildPalletsTests` and `ParseCodeTests`) actually correct?**
  _`SlotLocator` has 8 INFERRED edges - model-reasoned connections that need verification._
- **Are the 2 inferred relationships involving `WarehouseModel` (e.g. with `Meta` and `WarehouseModelForm`) actually correct?**
  _`WarehouseModel` has 2 INFERRED edges - model-reasoned connections that need verification._
- **Are the 5 inferred relationships involving `Scan` (e.g. with `HeaderAliasTests` and `KindMappingTests`) actually correct?**
  _`Scan` has 5 INFERRED edges - model-reasoned connections that need verification._
- **What connects `docker-entrypoint.sh script`, `Migration`, `Migration` to the rest of the system?**
  _45 weakly-connected nodes found - possible documentation gaps or missing edges._