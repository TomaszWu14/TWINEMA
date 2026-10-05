// Działka-wielokąt (D2) — czyste funkcje (bez three.js i DOM), testowane `node --test` (tests/js/site.test.mjs).
// Lustro twin/site.py: granica = `site.boundary` [[x, y], …] albo prostokąt [0, W] × [0, D]; odległość od granicy
// per krawędź (zwrócona ku stronie dojazdu = „od drogi”); wjazd z boku obrysu promieniem w głąb do granicy.
export const OUT_DIR = { N: [0, -1], S: [0, 1], W: [-1, 0], E: [1, 0] };
const ROAD_EDGE_COS = 0.7;

export function plotPolygon(site) {
  if (site.boundary?.length >= 3) return site.boundary.map(([x, y]) => [x, y]);
  const { width: W, depth: D } = site;
  return [[0, 0], [W, 0], [W, D], [0, D]];
}

/** Pole ze znakiem (wzór Gaussa). */
export function polygonArea(pts) {
  let s = 0;
  pts.forEach((a, i) => { const b = pts[(i + 1) % pts.length]; s += a[0] * b[1] - b[0] * a[1]; });
  return s / 2;
}

const edges = (pts) => pts.map((a, i) => [a, pts[(i + 1) % pts.length]]);

function outward([a, b], sign) {
  const dx = b[0] - a[0], dy = b[1] - a[1], L = Math.hypot(dx, dy) || 1;
  return [(dy / L) * sign, (-dx / L) * sign];
}

/** Odległość od granicy dla każdej krawędzi (kolejność plotPolygon). */
export function edgeSetbacks(site) {
  const pts = plotPolygon(site), sign = polygonArea(pts) > 0 ? 1 : -1, road = OUT_DIR[site.access_side] || OUT_DIR.S;
  const sb = site.setback || {};
  return edges(pts).map((e) => {
    const n = outward(e, sign);
    return (n[0] * road[0] + n[1] * road[1] > ROAD_EDGE_COS ? sb.road : sb.other) || 0;
  });
}

/** Linia zabudowy do rysunku: każda krawędź przesunięta do środka o swój odstęp, narożniki z przecięć
 *  sąsiednich prostych. null, gdy wynik się „wywraca” (odstępy zjadają działkę). */
export function insetPolygon(pts, dists) {
  const sign = polygonArea(pts) > 0 ? 1 : -1;
  const lines = edges(pts).map((e, i) => {
    const n = outward(e, sign), d = dists[i];
    return [[e[0][0] - n[0] * d, e[0][1] - n[1] * d], [e[1][0] - n[0] * d, e[1][1] - n[1] * d]];
  });
  const out = lines.map((l, i) => {
    const [[p1, p2], [q1, q2]] = [lines[(i - 1 + lines.length) % lines.length], l];
    const r = [p2[0] - p1[0], p2[1] - p1[1]], s = [q2[0] - q1[0], q2[1] - q1[1]], den = r[0] * s[1] - r[1] * s[0];
    if (Math.abs(den) < 1e-9) return q1;                  // krawędzie współliniowe
    const t = ((q1[0] - p1[0]) * s[1] - (q1[1] - p1[1]) * s[0]) / den;
    return [p1[0] + t * r[0], p1[1] + t * r[1]];
  });
  // „wywrócenie”: któraś krawędź po przesunięciu odwraca kierunek (odstępy większe niż pół działki)
  const flipped = edges(out).some(([a, b], i) => {
    const [p, q] = edges(pts)[i];
    return (b[0] - a[0]) * (q[0] - p[0]) + (b[1] - a[1]) * (q[1] - p[1]) <= 0;
  });
  return flipped || Math.abs(polygonArea(out)) < 1 ? null : out;
}

/** Wjazd: punkt na boku obrysu → pierwsza krawędź granicy w głąb działki. → {at, dir (do środka)} */
export function entryOnBoundary(site, e) {
  const { width: W, depth: D } = site;
  const p = { N: [e.pos, 0], S: [e.pos, D], W: [0, e.pos], E: [W, e.pos] }[e.side];
  const din = OUT_DIR[e.side].map((v) => -v);
  if (!(site.boundary?.length >= 3)) return { at: p, dir: din };
  const pts = plotPolygon(site), sign = polygonArea(pts) > 0 ? 1 : -1;
  let best = null;
  for (const [a, b] of edges(pts)) {
    const ex = b[0] - a[0], ey = b[1] - a[1], den = din[0] * ey - din[1] * ex;
    if (Math.abs(den) < 1e-12) continue;
    const wx = a[0] - p[0], wy = a[1] - p[1], s = (wx * ey - wy * ex) / den, t = (wx * din[1] - wy * din[0]) / den;
    if (s >= -1e-9 && t >= -1e-9 && t <= 1 + 1e-9 && (!best || s < best.s)) best = { s, e: [a, b] };
  }
  if (!best) return { at: p, dir: din };
  const n = outward(best.e, sign);
  return { at: [p[0] + best.s * din[0], p[1] + best.s * din[1]], dir: [-n[0], -n[1]] };
}

function distSeg(p, a, b) {
  const dx = b[0] - a[0], dy = b[1] - a[1], L2 = dx * dx + dy * dy;
  const t = L2 ? Math.max(0, Math.min(1, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / L2)) : 0;
  return Math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy);
}

/** Indeks, pod który wstawić nowy wierzchołek klikniętego punktu: za początkiem najbliższej krawędzi. */
export function insertIndex(pts, p) {
  let best = 0, bestD = Infinity;
  edges(pts).forEach(([a, b], i) => { const d = distSeg(p, a, b); if (d < bestD) { bestD = d; best = i; } });
  return best + 1;
}
