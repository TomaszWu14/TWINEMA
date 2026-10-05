// Edytor layoutu — czyste funkcje (bez DOM), testowane przez `node --test` (twin/tests/test_layout_editor_js.py).
// Konwencja repo (twin/blender_route.py): narożnik (x, y) + kąt θ [°], y „w głąb” hali,
// oś szerokości u_w = (cos θ, −sin θ), oś głębokości u_d = (sin θ, cos θ). Front regału po stronie −u_d.

export const ZONE_PALETTE = ['#3b82f6', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6', '#f97316', '#06b6d4',
  '#ec4899', '#14b8a6', '#6b7280'];   // jak warehouse_model_view (kolory stref w 3D)
export const SNAP_M = 0.1;
export const BACK_GAP_M = 0.1;       // zapas; właściwa wartość z konfiguracji edytora (design_catalog.BACK_GAP_M)

export const rad = (deg) => (deg || 0) * Math.PI / 180;
export const round = (v, d = 3) => Math.round(v * 10 ** d) / 10 ** d;

export function axes(angle) {
  const t = rad(angle);
  return [[Math.cos(t), -Math.sin(t)], [Math.sin(t), Math.cos(t)]];
}

/** Wymiary prostokąta [szer., głęb.] w metrach — regał albo element hali. */
export function size(item) {
  return item.n_bays !== undefined ? [item.n_bays * item.bay_width_cm / 100, item.depth_cm / 100]
    : [item.width, item.depth];
}

export function corners(item) {
  const [w, d] = size(item);
  const [uw, ud] = axes(item.angle);
  return [[0, 0], [w, 0], [w, d], [0, d]].map(([a, c]) =>
    [item.x + uw[0] * a + ud[0] * c, item.y + uw[1] * a + ud[1] * c]);
}

export function bbox(points) {
  const xs = points.map((p) => p[0]), ys = points.map((p) => p[1]);
  return [Math.min(...xs), Math.min(...ys), Math.max(...xs), Math.max(...ys)];
}

export function center(item) {
  const c = corners(item);
  return [(c[0][0] + c[2][0]) / 2, (c[0][1] + c[2][1]) / 2];
}

/** Atrybut `transform` SVG (y w dół = y „w głąb”): rotate(−θ) daje u_w = (cos θ, −sin θ). */
export function svgTransform(item) {
  return `translate(${item.x} ${item.y}) rotate(${-(item.angle || 0)})`;
}

export function snap(v, step = SNAP_M) {
  return round(Math.round(v / step) * step);
}

/** Obrót punktu wokół środka o θ w konwencji repo (dodatni kąt = jak u_w). */
export function rotateAround([px, py], [cx, cy], angle) {
  const t = rad(angle), dx = px - cx, dy = py - cy;
  return [cx + dx * Math.cos(t) + dy * Math.sin(t), cy - dx * Math.sin(t) + dy * Math.cos(t)];
}

/** Obraca elementy jako grupę wokół środka ich obrysu (zmienia obiekty w miejscu). */
export function rotateGroup(items, angle) {
  if (!items.length) return;
  const [x0, y0, x1, y1] = bbox(items.flatMap(corners));
  const c = [(x0 + x1) / 2, (y0 + y1) / 2];
  for (const it of items) {
    [it.x, it.y] = rotateAround([it.x, it.y], c, angle).map((v) => round(v));
    it.angle = round(((it.angle || 0) + angle) % 360 + 360) % 360;
  }
}

/** Kolor strefy: strefy posortowane alfabetycznie → kolejne kolory palety (jak w widoku 3D). */
export function zoneColors(racks) {
  const zones = [...new Set(racks.map((r) => r.zone))].sort();
  return Object.fromEntries(zones.map((z, i) => [z, ZONE_PALETTE[i % ZONE_PALETTE.length]]));
}

/** Następny wolny numer regału w strefie, z wiodącymi zerami jak w istniejących (domyślnie 3 cyfry). */
export function nextRackIds(racks, zone, count) {
  const inZone = racks.filter((r) => r.zone === zone).map((r) => r.rack_id);
  const width = Math.max(3, ...inZone.map((id) => id.length));
  let n = Math.max(0, ...inZone.map((id) => parseInt(id, 10)).filter(Number.isFinite));
  const taken = new Set(inZone);
  const out = [];
  while (out.length < count) {
    const id = String(++n).padStart(width, '0');
    if (!taken.has(id)) out.push(id);
  }
  return out;
}

/** Blok regałów: `rows` rzędów po `bays` gniazd, parami plecami do siebie (opcjonalnie), między
 *  parami alejka `aisle` [m]. Rząd nieparzysty w parze jest obrócony o 180° (front do alejki). */
export function makeBlock({ x, y, rows, bays, levels, bayWidthCm, depthCm, levelHeightCm, aisle,
  zone, ids, backToBack = true, backGap = BACK_GAP_M }) {
  const w = bays * bayWidthCm / 100, d = depthCm / 100;
  const out = [];
  let yy = y;
  for (let i = 0; i < rows; i++) {
    const back = backToBack && i % 2 === 1;
    const base = { zone, rack_id: ids[i], n_bays: bays, n_levels: levels, bay_width_cm: bayWidthCm,
      depth_cm: depthCm, level_height_cm: levelHeightCm };
    // 180°: narożnik w (x + w, y + d) — prostokąt zajmuje to samo pole, front zwrócony w +y
    out.push(back ? { ...base, x: round(x + w), y: round(yy + d), angle: 180 } : { ...base, x: round(x), y: round(yy), angle: 0 });
    yy += d + (backToBack && i % 2 === 0 && i + 1 < rows ? backGap : aisle);
  }
  return out;
}

/** Stos cofnij/ponów na migawkach JSON (limit, żeby pamięć nie rosła bez końca). */
export class History {
  constructor(limit = 100) { this.limit = limit; this.past = []; this.future = []; }
  push(snapshot) {
    this.past.push(snapshot);
    if (this.past.length > this.limit) this.past.shift();
    this.future = [];
  }
  undo(current) {
    if (!this.past.length) return null;
    this.future.push(current);
    return this.past.pop();
  }
  redo(current) {
    if (!this.future.length) return null;
    this.past.push(current);
    return this.future.pop();
  }
}

/** Wartość najczęstsza (typowe parametry regałów modelu do „Dodaj blok”). */
export function mode(values, fallback) {
  const count = new Map();
  for (const v of values) count.set(v, (count.get(v) || 0) + 1);
  let best = fallback, n = 0;
  for (const [v, c] of count) if (c > n) { best = v; n = c; }
  return best;
}
