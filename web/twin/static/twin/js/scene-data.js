// Scena 3D hali — czyste funkcje (bez three.js i DOM), testowane `node --test`
// (twin/tests/js/scene_data.test.mjs). Budowę meshy robi scene-builder.js.
// Konwencja repo (twin/blender_route.py): narożnik (x, y) + kąt θ [°], y „w głąb” = oś Z w three.js;
// group.position = (x, 0, y), group.rotation.y = θ → punkt lokalny (a, c) trafia w
// (x + a·cosθ + c·sinθ, y − a·sinθ + c·cosθ) = u_w·a + u_d·c.
import { zoneColors } from './layout-core.js';

// Typy elementów rysowane jako płaskie pola na posadzce (reszta = bryły/rampy).
export const FLAT_KINDS = new Set(['corridor', 'block_zone', 'staging', 'returns', 'fire_route', 'charging',
  'walkway', 'truckway', 'zone_temp', 'zone_adr', 'zone_oversize', 'zone_value']);
export const EDGE_KINDS = new Set(['dock', 'gate']);
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
  return { floor: { width: S.floor.width, depth: S.floor.depth }, racks, features };
}

/** Obrys sceny: hala albo dalej, jeśli regały wychodzą poza nią (obrót do 90° → większy wymiar). */
export function extents(racks, floor) {
  let x = floor.width, z = floor.depth;
  for (const r of racks) {
    const reach = Math.max(r.width, r.depth) + 2;
    x = Math.max(x, (r.x || 0) + reach);
    z = Math.max(z, (r.y || 0) + reach);
  }
  return { x, z, cx: x / 2, cz: z / 2, diag: Math.hypot(x, z) };
}

/** Szczegółowość stali wg liczby gniazdo-poziomów: pełna / lekka (1 słupek, 1 belka) / XL (belka na rząd). */
export function steelMode(racks) {
  const n = racks.reduce((s, r) => s + Math.max(1, r.n_bays) * Math.max(1, r.n_levels), 0);
  return n > 20000 ? 'xl' : n > 3000 ? 'lite' : 'full';
}

/** Macierze instancji stali wszystkich regałów (kolumnowo 4×4, jak InstancedMesh.instanceMatrix):
 *  { up, beam, brace } → Float32Array. Złożenie T(regał)·Ry(θ)·T(część)·Rx(a)·S liczone wprost
 *  (bez Matrix4/Vector3 na każdy z dziesiątek tysięcy elementów). */
export function steelMatrices(racks, mode) {
  const lists = racks.map((r) => steelParts(r, mode));
  const n = { up: 0, beam: 0, brace: 0 };
  lists.forEach((parts) => parts.forEach((p) => { n[p[0]]++; }));
  const out = { up: new Float32Array(n.up * 16), beam: new Float32Array(n.beam * 16), brace: new Float32Array(n.brace * 16) };
  const at = { up: 0, beam: 0, brace: 0 };
  racks.forEach((r, i) => {
    const t = (r.angle || 0) * Math.PI / 180, c = Math.cos(t), s = Math.sin(t), rx0 = r.x || 0, rz0 = r.y || 0;
    for (const [b, sx, sy, sz, x, y, z, a] of lists[i]) {
      const ca = Math.cos(a), sa = Math.sin(a), m = out[b], o = at[b];
      m[o] = c * sx; m[o + 1] = 0; m[o + 2] = -s * sx; m[o + 3] = 0;                       // R·(sx,0,0)
      m[o + 4] = s * sa * sy; m[o + 5] = ca * sy; m[o + 6] = c * sa * sy; m[o + 7] = 0;     // R·Rx·(0,sy,0)
      m[o + 8] = s * ca * sz; m[o + 9] = -sa * sz; m[o + 10] = c * ca * sz; m[o + 11] = 0;  // R·Rx·(0,0,sz)
      m[o + 12] = rx0 + c * x + s * z; m[o + 13] = y; m[o + 14] = rz0 - s * x + c * z; m[o + 15] = 1;
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
