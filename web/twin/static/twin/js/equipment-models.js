// Modele sprzętu magazynowego z prostych brył (G2b) — czyste dane, bez three.js (testy: node --test).
// Część = [długość, wysokość, szerokość, x środka, y dołu, kolor, z środka = 0]; przód pojazdu = +x,
// y w górę, z w bok. `body` stoi na posadzce, `lift` (wózek wideł / kabina) jedzie w górę o wartość podnoszenia.
// Budżet ≤ 16 brył na pojazd: odtwarzacze robią InstancedMesh na część (dziesiątki pojazdów naraz).

/** Kolor nadwozia wg rodzaju sprzętu — jedna mapa dla scen i legend. Spokojne, wzajemnie rozróżnialne. */
export const EQUIPMENT_COLORS = {
  reach: 0xc9a227,          // musztardowy
  vna: 0x4f7cac,            // stalowy niebieski
  ptruck: 0x5b8c5a,         // szałwiowa zieleń
  counterbalance: 0xb5532f, // ceglasty
  agv: 0x7a6aa8,            // przygaszony fiolet
  amr: 0x3a9ca0,            // morski
};
export const EQUIPMENT_LABELS = {
  reach: 'Reach truck', vna: 'Wózek systemowy VNA', ptruck: 'Wózek paletowy', counterbalance: 'Wózek czołowy',
  agv: 'AGV paletowy', amr: 'AMR',
};
export const STEEL = 0x30353a, WHEEL = 0x1f2329, SENSOR = 0x111827, MARK = 0xe5e7eb;

const C = EQUIPMENT_COLORS;
const pair = (part, z) => [[...part, z], [...part, -z]];   // para symetryczna względem osi pojazdu

export const MODELS = {
  // Reach truck: napęd z kabiną stojącą z tyłu, nogi podporowe do przodu, maszt teleskopowy, osłona na słupkach.
  reach: {
    body: [[1.3, 1.0, 1.2, -0.75, 0.15, C.reach],
      ...pair([1.3, 0.22, 0.2, 0.5, 0.05, C.reach], 0.5),         // nogi podporowe (wysięgniki)
      ...pair([0.3, 0.2, 0.18, 1.0, 0, WHEEL], 0.5),               // rolki nośne na końcach nóg
      [0.4, 0.35, 0.2, -1.0, 0, WHEEL],                            // koło napędowe
      ...pair([0.12, 4.6, 0.1, 0.32, 0.1, STEEL], 0.4),            // maszt
      [0.12, 0.12, 0.9, 0.32, 4.6, STEEL],
      [1.2, 0.06, 1.15, -0.7, 2.2, STEEL],                         // osłona kabiny
      ...pair([0.07, 2.05, 0.07, -1.28, 0.15, STEEL], 0.5)],
    lift: [[0.08, 0.9, 1.0, 0.45, 0.1, STEEL], ...pair([1.1, 0.06, 0.12, 1.1, 0.08, STEEL], 0.25)],
  },
  // VNA / kombi: długie podwozie, maszt ~8,7 m, kabina jedzie w górę razem z obrotową głowicą wideł.
  vna: {
    body: [[0.9, 1.25, 1.3, -1.35, 0.12, C.vna], [1.4, 0.3, 1.3, -0.25, 0.12, C.vna],
      ...pair([1.2, 0.22, 0.2, 1.0, 0.05, C.vna], 0.55),
      ...pair([0.3, 0.2, 0.18, 1.45, 0, WHEEL], 0.55),
      ...pair([0.18, 8.5, 0.12, -0.8, 0.12, STEEL], 0.5),
      [0.18, 0.15, 1.1, -0.8, 8.6, STEEL]],
    lift: [[1.0, 1.1, 1.15, -0.2, 0.42, C.vna], [1.1, 0.08, 1.2, -0.2, 2.45, STEEL],
      ...pair([0.07, 0.95, 0.07, 0.27, 1.52, STEEL], 0.55),       // słupki przedniej szyby kabiny
      [0.35, 0.9, 1.0, 0.5, 0.15, STEEL],                          // głowica obrotowa
      ...pair([1.1, 0.06, 0.12, 1.25, 0.1, STEEL], 0.22)],
  },
  // Wózek paletowy prowadzony: dyszel z tyłu, korpus napędu, długie widły tuż nad posadzką.
  ptruck: {
    body: [[0.6, 0.8, 0.72, -0.05, 0.08, C.ptruck], [0.5, 0.05, 0.6, -0.05, 0.88, STEEL],
      [0.1, 0.5, 0.6, 0.27, 0.08, STEEL],                          // oparcie wideł
      ...pair([1.15, 0.08, 0.17, 0.88, 0.06, STEEL], 0.25),
      ...pair([0.15, 0.08, 0.12, 1.35, 0, WHEEL], 0.25),
      [0.3, 0.25, 0.12, -0.05, 0, WHEEL],
      [0.06, 0.55, 0.06, -0.42, 0.85, STEEL], [0.14, 0.1, 0.42, -0.5, 1.35, STEEL]],   // dyszel + rączka
    lift: [],
  },
  // Wózek czołowy: przeciwwaga z tyłu, dach ochronny na czterech słupkach, maszt z przodu, 4 koła.
  counterbalance: {
    body: [[1.5, 0.75, 1.1, -0.45, 0.25, C.counterbalance], [0.4, 1.0, 1.15, -1.3, 0.2, STEEL],
      ...pair([0.07, 1.25, 0.07, 0.15, 1.0, STEEL], 0.5), ...pair([0.07, 1.25, 0.07, -1.05, 1.0, STEEL], 0.5),
      [1.3, 0.06, 1.1, -0.45, 2.25, STEEL],
      ...pair([0.6, 0.6, 0.22, 0.0, 0, WHEEL], 0.48), ...pair([0.5, 0.5, 0.2, -1.0, 0, WHEEL], 0.48),
      ...pair([0.1, 3.2, 0.1, 0.42, 0.05, STEEL], 0.35)],
    lift: [[0.06, 0.9, 0.95, 0.52, 0.08, STEEL], ...pair([1.1, 0.05, 0.12, 1.1, 0.08, STEEL], 0.25)],
  },
  // AGV paletowy: niski korpus z podnośnikiem (paleta na wierzchu), zderzaki, słupek czujników — bez kabiny.
  agv: {
    body: [[1.5, 0.3, 0.95, 0, 0.03, C.agv],
      [0.06, 0.12, 0.95, 0.78, 0.08, STEEL], [0.06, 0.12, 0.95, -0.78, 0.08, STEEL],
      [0.03, 0.08, 0.4, 0.82, 0.2, SENSOR],                        // skaner bezpieczeństwa z przodu
      [0.08, 0.75, 0.08, 0.7, 0.33, STEEL, 0.38], [0.14, 0.1, 0.14, 0.7, 1.08, SENSOR, 0.38],
      ...pair([0.22, 0.18, 0.12, 0.55, 0, WHEEL], 0.42), ...pair([0.22, 0.18, 0.12, -0.55, 0, WHEEL], 0.42)],
    lift: [[1.2, 0.04, 0.85, 0, 0.33, STEEL]],
  },
  // AMR: płaska platforma na kołach, jasny pas i strzałka z przodu = kierunek jazdy.
  amr: {
    body: [[1.0, 0.22, 0.7, 0, 0.05, C.amr], [0.04, 0.06, 0.5, 0.5, 0.12, MARK],
      ...pair([0.18, 0.14, 0.06, 0, 0, WHEEL], 0.36), [0.1, 0.06, 0.08, 0.4, 0, WHEEL], [0.1, 0.06, 0.08, -0.4, 0, WHEEL]],
    lift: [[0.95, 0.03, 0.65, 0, 0.27, STEEL], [0.18, 0.02, 0.12, 0.33, 0.3, MARK]],
  },
};

/** Gdzie jedzie paleta: dx = środek palety przed środkiem pojazdu [m], z = spód palety nad posadzką [m]. */
export const CARRY = {
  reach: { dx: 1.15, z: 0.14 }, vna: { dx: 1.3, z: 0.16 }, ptruck: { dx: 0.9, z: 0.14 },
  counterbalance: { dx: 1.15, z: 0.13 }, agv: { dx: 0, z: 0.37 }, amr: { dx: 0, z: 0.3 },
};

/** Typ sprzętu z katalogu (equipment.catalog.KINDS) → model; null = brak modelu pojazdu (przenośnik, sorter…). */
const FROM_CATALOG = { pallet_truck: 'ptruck', counterbalance: 'counterbalance', reach: 'reach', vna: 'vna',
  agv: 'agv', amr: 'amr', stacker: 'reach', order_picker: 'reach' };
export const modelForEquipment = (kind) => FROM_CATALOG[kind] ?? null;

/** Wszystkie bryły modelu (podwozie + część ruchoma) — dla odtwarzacza bez podnoszenia. */
export const modelParts = (kind) => [...MODELS[kind].body, ...MODELS[kind].lift];

/** Wysokość modelu [m] (np. etykieta nad pojazdem). */
export const modelHeight = (kind) => Math.max(...modelParts(kind).map(([, h, , , y]) => y + h));
