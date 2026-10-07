// Heatmapa ruchu animacji dnia (G9) — czyste funkcje bez three.js (testy: node --test).
// Siatka na posadzce hali: ile przejazdów wózków z paletą przecięło komórkę w ciągu dnia (trasy jak w animacji).
// Kolor w skali log (kilka głównych alejek nie „gasi” reszty), przezroczysty tam, gdzie nikt nie jechał.

/** Pusta siatka pokrywająca posadzkę {width, depth} [m]; komórka `cell` m. */
export function heatGrid(floor, cell = 1) {
  const nx = Math.max(1, Math.ceil(floor.width / cell)), ny = Math.max(1, Math.ceil(floor.depth / cell));
  return { nx, ny, cell, v: new Float32Array(nx * ny) };
}

/** Dolicz trasę (łamana [[x, y], …]) — każda komórka po drodze raz na przejazd; próbka co `step` m. */
export function addPath(g, pts, w = 1, step = 0.5) {
  const hit = new Set();
  for (let k = 1; k < pts.length; k++) {
    const [ax, ay] = pts[k - 1], [bx, by] = pts[k], n = Math.max(1, Math.ceil(Math.hypot(bx - ax, by - ay) / step));
    for (let s = 0; s <= n; s++) {
      const i = Math.floor((ax + (bx - ax) * s / n) / g.cell), j = Math.floor((ay + (by - ay) * s / n) / g.cell);
      if (i >= 0 && j >= 0 && i < g.nx && j < g.ny) hit.add(j * g.nx + i);
    }
  }
  for (const c of hit) g.v[c] += w;
}

// Rampa: żółty → pomarańczowy → czerwony; krycie rośnie z natężeniem.
const RAMP = [[250, 204, 21], [249, 115, 22], [220, 38, 38]];

/** Siatka → RGBA (wiersz j = y), 0 → przezroczyste; log1p(v) / log1p(max). */
export function heatRGBA(g) {
  const out = new Uint8ClampedArray(g.nx * g.ny * 4);
  let max = 0;
  for (const x of g.v) if (x > max) max = x;
  if (!max) return out;
  const lm = Math.log1p(max);
  g.v.forEach((x, k) => {
    if (!x) return;
    const f = Math.log1p(x) / lm, s = f * (RAMP.length - 1), a = Math.min(RAMP.length - 2, Math.floor(s)), u = s - a;
    for (let c = 0; c < 3; c++) out[k * 4 + c] = RAMP[a][c] + (RAMP[a + 1][c] - RAMP[a][c]) * u;
    out[k * 4 + 3] = 70 + 150 * f;
  });
  return out;
}
