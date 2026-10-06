// Scena 3D hali — czyste funkcje (bez three.js i DOM), testowane `node --test`
// (twin/tests/js/scene_data.test.mjs). Budowę meshy robi scene-builder.js.
// Konwencja repo (twin/blender_route.py): narożnik (x, y) + kąt θ [°], y „w głąb” = oś Z w three.js;
// group.position = (x, 0, y), group.rotation.y = θ → punkt lokalny (a, c) trafia w
// (x + a·cosθ + c·sinθ, y − a·sinθ + c·cosθ) = u_w·a + u_d·c.
import { zoneColors } from './layout-core.js';
import { edgeSetbacks, entryOnBoundary, insetPolygon, plotPolygon } from './site-geom.js';

// Typy elementów rysowane jako płaskie pola na posadzce (reszta = bryły/rampy).
export const FLAT_KINDS = new Set(['corridor', 'block_zone', 'staging', 'returns', 'fire_route', 'charging',
  'walkway', 'truckway', 'zone_temp', 'zone_adr', 'zone_oversize', 'zone_value']);
export const EDGE_KINDS = new Set(['dock', 'gate']);

// G2d: warstwy płaskie na tej samej wysokości (teren działki, pola na posadzce) nakładają się — bez stałej kolejności
// GPU co klatkę wybiera inną (z-fighting współpłaszczyznowy, żadna precyzja głębi go nie usuwa), a przezroczyste
// zmieniają kolejność z odległością kamery. Kolejność wg rodzaju: polygonOffset (przesunięcie w buforze głębi
// niezależne od odległości) + renderOrder. Ten sam rodzaj = ten sam kolor, więc jego nakładki nie migają.
const LAYERS = ['green', 'yard', 'road', 'parking', ...FLAT_KINDS];
export function stackLayer(mesh, kind) {
  const r = LAYERS.indexOf(kind) + 1 || LAYERS.length + 1;
  Object.assign(mesh.material, { polygonOffset: true, polygonOffsetFactor: -1, polygonOffsetUnits: -2 * r });
  mesh.renderOrder = r;
  return mesh;
}
export const DEFAULT_CLEAR_H = 8.0;   // jak shared.model_columns, gdy hala nie ma wysokości w świetle

/** Punkt lokalny regału (a wzdłuż szerokości, c w głąb) → współrzędne hali; to samo robi grupa three.js. */
export function localToWorld(item, [a, c]) {
  const t = (item.angle || 0) * Math.PI / 180;
  return [item.x + a * Math.cos(t) + c * Math.sin(t), item.y - a * Math.sin(t) + c * Math.cos(t)];
}

/** Stan edytora (S) → dane sceny w formacie widoku modelu (racks_json / features_json). */
export function editorScene(S, featureColors = {}) {
  const colors = zoneColors(S.racks);
  const racks = S.racks.map((r) => ({
    zone: r.zone, rack_id: r.rack_id, x: r.x, y: r.y, angle: r.angle || 0,
    width: r.n_bays * r.bay_width_cm / 100, depth: r.depth_cm / 100, level_h: r.level_height_cm / 100,
    n_bays: r.n_bays, n_levels: r.n_levels, color: colors[r.zone], fill_pct: null, _k: r._k,
  }));
  const h = S.floor.clear_height || DEFAULT_CLEAR_H;
  const features = [
    ...S.features.map((f) => ({ kind: f.kind, label: f.label || '', kind_label: (S.kinds || {})[f.kind] || f.kind,
      x: f.x, y: f.y, width: f.width, depth: f.depth, angle: f.angle || 0,
      color: featureColors[f.kind] || '#6b7280', _k: f._k })),
    ...(S.colList || []).map((c) => ({ kind: 'column', label: '', x: c.x - c.size / 2, y: c.y - c.size / 2,
      width: c.size, depth: c.size, angle: 0, color: '#475569', height: h })),
  ];
  return { floor: { width: S.floor.width, depth: S.floor.depth, clear_height: S.floor.clear_height || null }, racks, features,
    site: S.site || null };
}

/** Obrys sceny: hala albo dalej (+2 m), jeśli narożniki regałów wychodzą poza nią. Z narożników, nie
 *  z „najdłuższego boku w każdą stronę” — tamto powiększało obrys hali o długość regału i psuło kadr. */
export function extents(racks, floor) {
  let x = floor.width, z = floor.depth;
  for (const r of racks) {
    for (const p of [[0, 0], [r.width, 0], [0, r.depth], [r.width, r.depth]]) {
      const [wx, wz] = localToWorld({ x: r.x || 0, y: r.y || 0, angle: r.angle }, p);
      if (wx > x) x = wx + 2;
      if (wz > z) z = wz + 2;
    }
  }
  return { x, z, cx: x / 2, cz: z / 2, diag: Math.hypot(x, z) };
}

/** Szczegółowość stali wg liczby gniazdo-poziomów: pełna / lekka (1 słupek, 1 belka) / XL (belka na rząd). */
export function steelMode(racks) {
  const n = racks.reduce((s, r) => s + Math.max(1, r.n_bays) * Math.max(1, r.n_levels), 0);
  return n > 20000 ? 'xl' : n > 3000 ? 'lite' : 'full';
}

/** Macierze instancji stali wszystkich regałów (kolumnowo 4×4, jak InstancedMesh.instanceMatrix):
 *  { up, beam, brace } → Float32Array. */
export function steelMatrices(racks, mode) {
  return { up: new Float32Array(0), beam: new Float32Array(0), brace: new Float32Array(0),
    ...rackMatrices(racks, (r) => steelParts(r, mode)) };
}

/** Części regałów (partsFn(r, i) → [partia, sx, sy, sz, x, y, z, obrótX]) → { partia: Float32Array,
 *  _owner: { partia: Uint32Array } } (_owner = indeks regału każdej instancji — przekolorowanie bez przebudowy).
 *  Złożenie T(regał)·Ry(θ)·T(część)·Rx(a)·S liczone wprost (bez Matrix4/Vector3 na każdy z dziesiątek
 *  tysięcy elementów). */
export function rackMatrices(racks, partsFn) {
  const lists = racks.map((r, i) => partsFn(r, i));
  const n = {};
  lists.forEach((parts) => parts.forEach((p) => { n[p[0]] = (n[p[0]] || 0) + 1; }));
  const out = { _owner: {} }, at = {};
  for (const k of Object.keys(n)) { out[k] = new Float32Array(n[k] * 16); out._owner[k] = new Uint32Array(n[k]); at[k] = 0; }
  racks.forEach((r, i) => {
    const t = (r.angle || 0) * Math.PI / 180, c = Math.cos(t), s = Math.sin(t), rx0 = r.x || 0, rz0 = r.y || 0;
    for (const [b, sx, sy, sz, x, y, z, a = 0] of lists[i]) {
      const ca = Math.cos(a), sa = Math.sin(a), m = out[b], o = at[b];
      m[o] = c * sx; m[o + 1] = 0; m[o + 2] = -s * sx; m[o + 3] = 0;                       // R·(sx,0,0)
      m[o + 4] = s * sa * sy; m[o + 5] = ca * sy; m[o + 6] = c * sa * sy; m[o + 7] = 0;     // R·Rx·(0,sy,0)
      m[o + 8] = s * ca * sz; m[o + 9] = -sa * sz; m[o + 10] = c * ca * sz; m[o + 11] = 0;  // R·Rx·(0,0,sz)
      m[o + 12] = rx0 + c * x + s * z; m[o + 13] = y; m[o + 14] = rz0 - s * x + c * z; m[o + 15] = 1;
      out._owner[b][o / 16] = i;
      at[b] = o + 16;
    }
  });
  return out;
}

/** Elementy stali regału w jego układzie lokalnym: [partia, sx, sy, sz, x, y, z, obrótX].
 *  Partie: up (słupki), beam (belki), brace (kratownice) — po jednym InstancedMesh na partię. */
export function steelParts(r, mode) {
  const out = [];
  const put = (...p) => out.push(p.length === 7 ? [...p, 0] : p);
  const BAYS = Math.max(1, r.n_bays), LEVELS = Math.max(1, r.n_levels);
  const W = r.width, D = r.depth, LH = r.level_h, BW = W / BAYS, H = LEVELS * LH;
  for (let i = 0; i <= BAYS; i++) {
    const x = i * BW;
    if (mode !== 'full') { for (const z of [0, D]) put('up', 0.09, H, 0.075, x, H / 2, z); continue; }
    for (const z of [0, D]) {
      put('up', 0.09, H, 0.02, x, H / 2, z);
      put('up', 0.02, H, 0.075, x - 0.035, H / 2, z + (z > 0 ? -0.045 : 0.045));
      put('up', 0.02, H, 0.075, x + 0.035, H / 2, z + (z > 0 ? -0.045 : 0.045));
      put('brace', 0.17, 0.02, 0.13, x, 0.012, z);
    }
    const steps = Math.max(4, Math.round(H / 1.0)), seg = H / steps;
    for (let s = 0; s < steps; s++) {
      put('brace', 0.035, Math.hypot(D, seg), 0.035, x, seg * (s + 0.5), D / 2, (s % 2 ? 1 : -1) * Math.atan2(D, seg));
      put('brace', 0.035, 0.035, D, x, seg * s + seg, D / 2);
    }
  }
  for (let lvl = 1; lvl <= LEVELS; lvl++) {
    const y = lvl * LH;
    if (mode === 'xl') { for (const z of [0, D]) put('beam', W, 0.115, 0.075, W / 2, y - 0.06, z); continue; }
    for (let b = 0; b < BAYS; b++) {
      const bx = b * BW + BW / 2;
      if (mode === 'lite') { for (const z of [0, D]) put('beam', BW - 0.09, 0.115, 0.075, bx, y - 0.06, z); continue; }
      for (const z of [0, D]) {
        put('beam', BW - 0.09, 0.115, 0.05, bx, y - 0.06, z);
        put('beam', BW - 0.09, 0.03, 0.075, bx, y - 0.005, z);
        put('beam', BW - 0.09, 0.03, 0.075, bx, y - 0.115, z);
      }
      for (let k = 0; k < 2; k++) put('brace', 0.045, 0.03, D, bx + (k ? 0.62 : -0.62), y - 0.02, D / 2);
    }
  }
  return out;
}

// ── G2: kolor regału wg trybu (typy / strefy specjalne / wypełnienie), obrysy, cienie kontaktowe ──────

/** Rodzaj regału: jeden predykat z serwera (rack_class); w edytorze — pole equipment; geometria tylko dla
 *  starych danych. → 'pallet' | 'vna' | 'shelf' */
export function rackClass(r) {
  if (r.rack_class) return r.rack_class;
  if (r.equipment) return r.equipment === 'shelf' || r.equipment === 'vna' ? r.equipment : 'pallet';
  return r.level_h < 1.0 || r.depth < 0.9 ? 'shelf' : 'pallet';
}

// Kolory trybów: nasycone tylko tam, gdzie niosą informację; reszta neutralna (stal ocynk / grafit).
export const COLOR_MODES = { type: 'Typy regałów', zones: 'Strefy specjalne', fill: 'Wypełnienie' };
export const RACK_TYPE_COLORS = { pallet: '#e07a1f', vna: '#2f7fc1', shelf: '#4f9a6b' };
export const RACK_TYPE_LABELS = { pallet: 'Paletowe (reach)', vna: 'VNA (wąska alejka)', shelf: 'Półkowe' };
export const SPECIAL_ZONES = new Set(['zone_temp', 'zone_adr', 'zone_oversize', 'zone_value']);
export const NEUTRAL_RACK = '#8b939c';
export const FILL_COLORS = [[50, '#3fa66b', 'do 50 %'], [80, '#e0a92b', '50–80 %'], [101, '#d4553f', 'powyżej 80 %']];

/** Strefa specjalna (element zone_*), w której leży środek regału — pierwsza pasująca; brak → null. */
export function rackZone(r, features) {
  const [cx, cz] = localToWorld({ x: r.x || 0, y: r.y || 0, angle: r.angle }, [r.width / 2, r.depth / 2]);
  for (const f of features || []) {
    if (!SPECIAL_ZONES.has(f.kind)) continue;
    const t = (f.angle || 0) * Math.PI / 180, dx = cx - f.x, dz = cz - f.y;
    const a = dx * Math.cos(t) - dz * Math.sin(t), c = dx * Math.sin(t) + dz * Math.cos(t);   // odwrotność localToWorld
    if (a >= 0 && a <= f.width && c >= 0 && c <= f.depth) return f;
  }
  return null;
}

/** Kolor regału w trybie: typ → RACK_TYPE_COLORS; strefy → kolor elementu strefy (jak na planie) albo
 *  neutralny; wypełnienie → progi FILL_COLORS (brak danych → neutralny). */
export function rackTint(r, mode, features) {
  if (mode === 'zones') return rackZone(r, features)?.color || NEUTRAL_RACK;
  if (mode === 'fill') {
    if (typeof r.fill_pct !== 'number') return NEUTRAL_RACK;
    return FILL_COLORS.find(([lim]) => r.fill_pct < lim)[1];
  }
  return RACK_TYPE_COLORS[rackClass(r)];
}

/** Legenda trybu: [[kolor, opis]] — tylko pozycje obecne w hali (bez szumu pustych kategorii). */
export function colorLegend(racks, mode, features) {
  if (mode === 'fill') {
    const has = racks.some((r) => typeof r.fill_pct === 'number');
    return has ? FILL_COLORS.map(([, c, l]) => [c, l]) : [[NEUTRAL_RACK, 'brak danych o stanie']];
  }
  if (mode === 'zones') {
    const seen = new Map();
    let outside = false;
    for (const r of racks) {
      const f = rackZone(r, features);
      if (!f) outside = true;
      else if (!seen.has(f.kind)) seen.set(f.kind, [f.color || NEUTRAL_RACK, f.kind_label || f.label || f.kind]);
    }
    return [...seen.values(), ...(outside ? [[NEUTRAL_RACK, 'Poza strefami specjalnymi']] : [])];
  }
  const cs = new Set(racks.map(rackClass));
  return Object.keys(RACK_TYPE_COLORS).filter((k) => cs.has(k)).map((k) => [RACK_TYPE_COLORS[k], RACK_TYPE_LABELS[k]]);
}

/** Obrys bryły regału: 12 krawędzi prostopadłościanu (x, y, z ×2 na krawędź) — jeden LineSegments na halę. */
export function rackOutline(r) {
  const H = Math.max(1, r.n_levels) * r.level_h, base = { x: r.x || 0, y: r.y || 0, angle: r.angle };
  const c = [[0, 0], [r.width, 0], [r.width, r.depth], [0, r.depth]].map((p) => localToWorld(base, p));
  const out = [];
  for (let i = 0; i < 4; i++) {
    const [ax, az] = c[i], [bx, bz] = c[(i + 1) % 4];
    out.push(ax, 0.02, az, bx, 0.02, bz, ax, H, az, bx, H, bz, ax, 0.02, az, ax, H, az);
  }
  return out;
}

/** Cień kontaktowy (miękki ciemny prostokąt na posadzce) — część w formacie steelParts, poszerzona o `pad`. */
export function contactShadowPart(r, pad = 0.35) {
  return [['shadow', r.width + pad * 2, 1, r.depth + pad * 2, r.width / 2, 0.012, r.depth / 2]];
}

// ── G1: wygląd sceny (palety w regałach, kadr, ściany hali, jakość) ─────────────────────────────

export const PALLET = { w: 0.8, d: 1.2, base: 0.144 };   // EUR: 0,8 m wzdłuż regału, 1,2 m w głąb
export const DECOR_FILL = 0.72;                          // zapełnienie „jak w pracującym magazynie”
export const FAST_ABOVE = 120000;                        // gniazdo-poziomów → domyślnie jakość szybka

/** Deterministyczny „los” 0..1 z indeksów (ten sam layout = te same palety po każdej przebudowie). */
export function hash01(a, b, c, d) {
  let h = Math.imul(a + 1, 73856093) ^ Math.imul(b + 1, 19349663) ^ Math.imul(c + 1, 83492791) ^ Math.imul(d + 1, 2654435761);
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  return ((h ^ (h >>> 16)) >>> 0) / 4294967296;
}

/** Ładunek regału w jego układzie lokalnym (format steelParts): palety EUR z ładunkiem na podłodze
 *  i na belkach albo kartony na półkach (regał półkowy). Zapełnienie z `fill_pct`, inaczej DECOR_FILL. */
export function decorParts(r, i) {
  const out = [];
  const BAYS = Math.max(1, r.n_bays), LEVELS = Math.max(1, r.n_levels);
  const D = r.depth, LH = r.level_h, BW = r.width / BAYS;
  const fill = typeof r.fill_pct === 'number' ? Math.max(0, Math.min(100, r.fill_pct)) / 100 : DECOR_FILL;
  // jeden predykat z serwera (rack_class); w edytorze — pole equipment; geometria tylko dla starych danych
  const shelf = rackClass(r) === 'shelf';
  const clear = LH - 0.12;                                 // światło pod belką wyższego poziomu
  for (let lvl = 0; lvl < LEVELS; lvl++) {
    const y = lvl * LH;
    for (let b = 0; b < BAYS; b++) {
      const slots = shelf ? Math.max(1, Math.floor(BW / 0.6)) : Math.max(1, Math.floor((BW - 0.1) / 0.95));
      for (let s = 0; s < slots; s++) {
        if (hash01(i, b, lvl, s) >= fill) continue;
        const x = b * BW + (s + 0.5) * BW / slots, k = hash01(s, lvl, b, i);
        if (shelf) {
          const sy = Math.max(0.12, clear * (0.45 + 0.4 * k));
          out.push(['bin', BW / slots * 0.82, sy, D * 0.85, x, y + sy / 2, D / 2]);
          continue;
        }
        const sz = Math.min(PALLET.d, D + 0.1), lh = Math.max(0.3, Math.min(1.8, clear - 0.2) * (0.65 + 0.35 * k));
        out.push(['pbase', PALLET.w, PALLET.base, sz, x, y + PALLET.base / 2, D / 2]);
        out.push(['pload', PALLET.w - 0.04, lh, sz - 0.06, x, y + PALLET.base + lh / 2, D / 2]);
      }
    }
  }
  return out;
}

/** Zakres głębi kamery z odległości do celu `d` i przekątnej sceny (G2c). Stałe near = 0,05 m przy far = 4000 m
 *  dawało ~10 cm rozdzielczości bufora głębi na 300 m — warstwy 1–2 cm nad posadzką (pola, cienie kontaktowe,
 *  teren działki) mrugały przy ruchu kamery (z-fighting). near ∝ d trzyma rozdzielczość w milimetrach.
 *  → {near, far} */
export function depthRange(d, diag) {
  return { near: Math.min(25, Math.max(0.5, d * 0.02)), far: Math.max(500, d * 8 + diag * 4) };
}

/** Rozdzielczość bufora głębi 24-bit [m] na odległości z (do testów i diagnostyki). */
export const depthStep = (z, near) => (z * z) / (near * 2 ** 24);

/** Izometria kadrowana do hali: kamera tak blisko, żeby obrys hali wypełnił kadr (zamiast stałego
 *  „diag × 1,1”, które przy szerokich halach odsuwało kamerę daleko). → { pos, target, dist } */
export function isoView({ cx, cz, x, z }, fovDeg = 42, aspect = 16 / 9, elevDeg = 34, azimDeg = 32) {
  const r = 0.5 * Math.hypot(x, z);
  const vf = fovDeg * Math.PI / 360, hf = Math.atan(Math.tan(vf) * aspect);
  // Ciasno w szerokim kadrze (hala i tak jest szersza niż wyższa na ekranie), luźniej w wąskim panelu.
  const k = 0.62 + 0.3 * Math.min(1, Math.max(0, (1.6 - aspect) / 1.0));
  const dist = (r / Math.sin(Math.min(vf, hf))) * k + 4;
  const e = elevDeg * Math.PI / 180, a = azimDeg * Math.PI / 180;
  return { pos: [cx + dist * Math.cos(e) * Math.sin(a), dist * Math.sin(e), cz + dist * Math.cos(e) * Math.cos(a)],
    target: [cx, 0, cz], dist };
}

/** Przelot kamery: ujęcie {pos, target} w chwili k ∈ [0, 1] (smoothstep — łagodny start i hamowanie). */
export function camAt(a, b, k) {
  const t = Math.min(1, Math.max(0, k)), e = t * t * (3 - 2 * t);
  const mix = (u, v) => u.map((x, i) => x + (v[i] - x) * e);
  return { pos: mix(a.pos, b.pos), target: mix(a.target, b.target) };
}

/** Ściany hali (w osiach sceny: x, z = y hali) z normalną na zewnątrz. */
export function hallWalls({ width, depth }) {
  return [
    { x0: 0, z0: 0, x1: width, z1: 0, nx: 0, nz: -1 },
    { x0: width, z0: 0, x1: width, z1: depth, nx: 1, nz: 0 },
    { x0: 0, z0: depth, x1: width, z1: depth, nx: 0, nz: 1 },
    { x0: 0, z0: 0, x1: 0, z1: depth, nx: -1, nz: 0 },
  ];
}

/** Przekrój: ściana między kamerą a halą (kamera po jej zewnętrznej stronie) jest ukryta. */
export function wallHidden(w, camX, camZ) {
  return (camX - w.x0) * w.nx + (camZ - w.z0) * w.nz > 0;
}

/** Normalna najbliższej ściany hali dla punktu (dok, brama) — tam stoją drzwi i auto. */
export function outward(cx, cz, { width, depth }) {
  return [[cx, [-1, 0]], [width - cx, [1, 0]], [cz, [0, -1]], [depth - cz, [0, 1]]].sort((a, b) => a[0] - b[0])[0][1];
}

/** Jakość grafiki: wybór użytkownika, a bez wyboru — szybka dla bardzo dużych hal. */
export function effectiveQuality(stored, racks) {
  if (stored === 'fast' || stored === 'high') return stored;
  const n = racks.reduce((s, r) => s + Math.max(1, r.n_bays) * Math.max(1, r.n_levels), 0);
  return n > FAST_ABOVE ? 'fast' : 'high';
}

// ── Działka (D1, format twin/site.py) — w układzie HALI (scena 3D i animacja liczą w nim wszystko) ──

/** Punkt działki → punkt hali (odwrotność położenia hali na działce: narożnik + kąt, osie jak regał). */
export function siteToHall(site, [px, py]) {
  const t = ((site.hall?.angle || 0) * Math.PI) / 180, dx = px - (site.hall?.x || 0), dy = py - (site.hall?.y || 0);
  return [dx * Math.cos(t) - dy * Math.sin(t), dx * Math.sin(t) + dy * Math.cos(t)];
}

const rectPts = (r) => [[0, 0], [r.width, 0], [r.width, r.depth], [0, r.depth]].map((p) => localToWorld(r, p));

/** Działka → wielokąty w układzie hali: granica (prostokąt albo wielokąt D2), linie zabudowy (odstęp per krawędź),
 *  elementy terenu, wjazdy ({at, dir} — dir w głąb działki). */
export function sitePlan(site) {
  if (!site?.width) return null;
  const toH = (p) => siteToHall(site, p), plot = plotPolygon(site);
  const entries = (site.entries || []).map((e) => {
    const { at, dir } = entryOnBoundary(site, e), a = toH(at), c = toH([at[0] + dir[0], at[1] + dir[1]]);
    return { kind: e.kind, width: e.width, side: e.side, at: a, dir: [c[0] - a[0], c[1] - a[1]] };
  });
  const building = insetPolygon(plot, edgeSetbacks(site));
  return {
    plot: plot.map(toH),
    building: building ? building.map(toH) : null,
    areas: (site.areas || []).map((a) => ({ kind: a.kind, label: a.label, pts: rectPts(a).map(toH), w: a.width, d: a.depth })),
    entries,
  };
}

/** Najbliższy wjazd danego rodzaju (brak osobowego → tir) do punktu hali; null bez działki/wjazdów. */
export function nearestEntry(plan, [x, y], kind = 'truck') {
  const all = plan?.entries || [];
  const list = all.some((e) => e.kind === kind) ? all.filter((e) => e.kind === kind) : all.filter((e) => e.kind === 'truck');
  let best = null;
  for (const e of list) if (!best || Math.hypot(e.at[0] - x, e.at[1] - y) < Math.hypot(best.at[0] - x, best.at[1] - y)) best = e;
  return best;
}
