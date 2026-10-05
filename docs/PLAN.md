# TWINEMA — zakres i plan

> **TWINEMA** = *digital twin* + *cinema*. Aplikacja do projektowania magazynów w 3D
> (hala, regały, pola odkładcze, strefy, flota), symulacji przepływów i produkcji
> prezentacji: render w Blenderze + lektor ElevenLabs → film i deck.
>
> Odbiorcy: zarząd (przegląd możliwości, technologii i kosztów) oraz osoby oceniające
> projekt z zewnątrz (rekruterzy). Scenariusz referencyjny: **budowa nowego centrum
> dystrybucyjnego** — dane demonstracyjne, bez nazw firm i danych klientów.

Status: F0 (fundament) — 2026-10-05.

---

## 1. Decyzje

| # | Decyzja | Wybór |
|---|---|---|
| D1 | Repo | prywatne, `TomaszWu14/TWINEMA` |
| D2 | Historia | czysta; pochodzenie kodu w `PROVENANCE.md` |
| D3 | Odbiorcy | zarząd + zewnętrzni oceniający (nacisk) → wygląd i README „portfolio-grade” |
| D4 | Logowanie | własne konta; bez SSO |
| D5 | Dane | tylko importy plików (xlsx/csv); bez pobierania z innych aplikacji |
| D6 | Render | **worker Blendera na własnym PC** (GPU, Blender już jest), pobiera zlecenia z aplikacji po HTTPS; serwer trzyma tylko aplikację i bazę. Później ten sam worker na wynajętej maszynie GPU, jeśli trzeba |
| D7 | Lektor | własny głos z ElevenLabs Voice Design (plan Creator lub wyższy) |
| D8 | Zakres | tylko projektowanie i animacja przepływów magazynu; bez paletyzacji kartonów (`palletizer`), HU, transportu |
| D9 | Relacja z PalViz | kopia kodu (fork-and-diverge), PalViz nietknięty; nic nie płynie z powrotem |

---

## 2. Zakres

### 2.1 MVP
1. **Dane** — materiały (wymiary/waga jednostek, przeliczniki), nośniki, typy regałów, lokalizacje, historia ruchów (zadania magazynowe), migawki stanów. Importy xlsx/csv z walidacją i raportem odrzuceń.
2. **Model hali** — generator „od zera” z parametrów (pojemność, wysokość hali, proporcje), widok 3D (three.js), warianty, strefy, KPI wariantu, porównanie wariantów.
3. **Symulacja** — dzień projektowy (P95), dyspozytor floty, kalibracja na realnych cyklach.
4. **ML** — prognoza wolumenów, segmentacja SKU pod rozmieszczenie, model czasu cyklu (§4).
5. **Render** — format sceny `twinema.scene` v1, worker Blendera, presety kamery, stills + animacje przepływów.
6. **Studio prezentacji** — scenariusz → lektor → ujęcia pod długość kwestii → montaż → MP4 + PDF (§5).

### 2.2 Po MVP (wsad do burzy mózgów)
- **Katalog rynku**: typy maszyn i systemów (regał paletowy, VNA, shuttle, AS/RS, AMR/AGV, przenośniki, sortery, wózki), producenci, parametry, widełki cen → CAPEX/OPEX wariantu.
- Edytor „jak w grze”: przeciąganie regałów, pól odkładczych, wydzielanie stref w 3D.
- Sezonowość roczna w prognozie (≥ 2 lata historii), wykrywanie anomalii.
- Wersja EN interfejsu i lektora; muzyka; split-screen „obecny vs wariant”.

### 2.3 Poza zakresem
Paletyzacja kartonów, kontrola HU, skanery, transport, integracje online z WMS/ERP.

---

## 3. Architektura

```
web/
  twinema/     projekt Django: config (pydantic, fail-fast), settings, urls
  core/        role (zamrożony kontrakt), middleware, health, logowanie, hub
  masterdata/  F2: Material, UnitConversion, RackType, LoadCarrier, Location, StockSnapshot, TaskHistory
  twin/        F1: WarehouseModel, Rack, HallFeature, BayTemplate, DesignVariant, strefy
  sim/         F1: dzień projektowy, symulacja, kalibracja, KPI, porównanie — czysty Python
  ml/          F4: forecast, sku_segmentation, cycle_time + ModelRun (wersja, metryka)
  render/      F3: scene.py, RenderJob, API dla workera
  studio/      F5: Presentation, Shot, Script, VoiceTrack; pipeline TTS → render → ffmpeg
tools/blender/ design_kit, anim, render_worker.py (pętla: pobierz zlecenie → render → wyślij)
```

Stack: Python 3.13, Django 5.2 LTS, PostgreSQL 17, Docker + Coolify, gunicorn + WhiteNoise.
Celery + Redis dochodzą w F3 (kolejka TTS/montażu); rendery robi zewnętrzny worker.

**Worker renderujący (D6):** skrypt na PC z Blenderem odpytuje `/api/render/next` (token),
pobiera scenę JSON, renderuje `blender -b -P`, odsyła MP4/PNG. Serwer bez GPU i bez
otwartych portów do Redisa — wystarczy HTTPS. PC wyłączony = zlecenia czekają w kolejce.

---

## 4. Uczenie maszynowe

| # | Model | Dane | Punkt wyjścia | Cel | Miernik |
|---|---|---|---|---|---|
| ML1 | Prognoza wolumenów | tygodnie × strumień | log-trend, P50/P90 | Holt-Winters/ETS, wybór wariantu przez MAPE, przedział 80 % | MAPE backtest vs log-trend |
| ML2 | Segmentacja SKU | rotacja, pobrania, wymiary, współwystępowanie | ABC | ABC×XYZ + k-means → strefy/poziomy w generatorze | droga w symulacji vs ABC |
| ML3 | Czas cyklu | realne cykle per zasób | mediana real÷sym | gradient boosting od dystansu, wysokości, typu wózka, pory | MAE na odłożonych dniach |

Zasada: baseline + backtest zawsze widoczne; model zastępuje baseline tylko, gdy wygrywa miernik.

---

## 5. Studio prezentacji

```
KPI wariantu → Scenariusz (Claude + edycja) → Lektor (ElevenLabs, timestamps)
            → Ujęcia (Blender, długość = kwestia) → Montaż (ffmpeg: głos, napisy, plansze) → MP4 + PDF
```

- Presety kamery: przelot nad halą, orbita strefy, przejazd korytarzem, zbliżenie regału, porównanie.
- Napisy SRT z znaczników czasu lektora.
- Cache po hashu wejścia (tekst+głos / scena+ujęcie): poprawka zdania nie renderuje całego filmu.
- Statusy: szkic → tekst zatwierdzony → audio → render → gotowe (nie renderujemy przed akceptacją tekstu).
- Na zewnątrz (ElevenLabs/Claude) idzie wyłącznie tekst narracji.

---

## 6. Fazy

| Faza | Cel | Kryterium „done” |
|---|---|---|
| **F0 Fundament** | repo, CI/CD, logowanie, hub, health | CI zielone, deploy na Coolify, `/health/` zwraca SHA |
| **F1 Przeszczep rdzenia** | generator, model 3D, symulacja, eksport sceny | skopiowane testy czystego Pythona zielone; generator + widok 3D działają |
| **F2 Dane** | modele + importy plików | import demonstracyjnych zadań i materiałów → symulacja dnia liczy się |
| **F3 Render** | worker Blendera + presety kamery | klik „Renderuj” → MP4/PNG w aplikacji |
| **F4 ML v1** | ML1 + ML2 | backtest z MAPE; segmentacja skraca drogę vs ABC |
| **F5 Studio MVP** | pierwszy film | 2–3 min film PL z lektorem i napisami, z aplikacji |
| **F6 Szlif** | ML3, porównania, katalog rynku | wg burzy mózgów |

Ścieżka krytyczna: F0 → F1 → F2 → F3 → F5; F4 równolegle z F3.

---

## 7. Ryzyka

| Ryzyko | Mitygacja |
|---|---|
| Dryf z kodem źródłowym | po F1 nowe prace projektowe tylko tu |
| Koszt ElevenLabs/Claude przy iteracjach | cache po hashu, akceptacja tekstu przed TTS, limit znaków na prezentację |
| Mało historii do ML | baseline + backtest zawsze pokazany |
| Nieobejrzane wizualnie 3D | każda faza z renderem kończy się przeglądem obrazu |
| Dane wrażliwe w demo | tylko dane syntetyczne/zanonimizowane; brak nazw firm w repo |
