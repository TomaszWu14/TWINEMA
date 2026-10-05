// G1 — wygląd sceny: ładunek regałów, kadr izometrii, ściany z przekrojem, jakość. `node --test`.
import assert from 'node:assert/strict';
import test from 'node:test';

import { DECOR_FILL, FAST_ABOVE, PALLET, decorParts, effectiveQuality, extents, hallWalls, hash01, isoView,
  outward, rackMatrices, wallHidden } from '../../static/twin/js/scene-data.js';

const VNA = { x: 0, y: 0, angle: 0, width: 13.5, depth: 1.1, level_h: 1.6, n_bays: 5, n_levels: 6 };
const SHELF = { x: 0, y: 0, angle: 0, width: 10, depth: 0.6, level_h: 0.45, n_bays: 10, n_levels: 5 };

test('decorParts: palety EUR z ładunkiem w gniazdach, deterministycznie, ~DECOR_FILL zapełnienia', () => {
  const a = decorParts(VNA, 3), b = decorParts(VNA, 3);
  assert.deepEqual(a, b);                                       // ten sam layout = te same palety
  const bases = a.filter((p) => p[0] === 'pbase'), loads = a.filter((p) => p[0] === 'pload');
  assert.equal(bases.length, loads.length);
  const slots = 5 * 6 * Math.floor((13.5 / 5 - 0.1) / 0.95);   // gniazda × poziomy × palety w gnieździe
  assert.ok(Math.abs(bases.length / slots - DECOR_FILL) < 0.15, `${bases.length}/${slots}`);
  for (const [, sx, sy, sz, x, y, z] of loads) {
    assert.ok(sy <= VNA.level_h - 0.12 - PALLET.base + 1e-9, 'ładunek mieści się pod belką');
    assert.ok(x > 0 && x < VNA.width && Math.abs(z - VNA.depth / 2) < 1e-9 && sx > 0 && sz > 0 && y > 0);
  }
});

test('decorParts: fill_pct steruje zapełnieniem, półki dostają kartony zamiast palet', () => {
  assert.equal(decorParts({ ...VNA, fill_pct: 0 }, 1).length, 0);
  const full = decorParts({ ...VNA, fill_pct: 100 }, 1).filter((p) => p[0] === 'pbase').length;
  assert.equal(full, 5 * 6 * 2);
  const shelf = decorParts(SHELF, 0);
  assert.ok(shelf.length > 0 && shelf.every((p) => p[0] === 'bin'));
});

test('rackMatrices: partie dowolne (stal i ładunek tą samą ścieżką), 16 liczb na instancję', () => {
  const m = rackMatrices([VNA, { ...VNA, x: 10, angle: 90 }], decorParts);
  const n = [VNA, VNA].map((r, i) => decorParts(i ? { ...r, x: 10, angle: 90 } : r, i).filter((p) => p[0] === 'pload').length);
  assert.equal(m.pload.length / 16, n[0] + n[1]);
  assert.equal(m.pload.length, m.pbase.length);
});

test('hash01: 0..1, różne dla różnych indeksów', () => {
  const v = new Set();
  for (let i = 0; i < 200; i++) { const h = hash01(i, 2, 3, 4); assert.ok(h >= 0 && h < 1); v.add(h); }
  assert.equal(v.size, 200);
});

test('isoView: kamera bliżej niż stary kadr (diag × ~1,1) i celuje w środek hali; wąski panel = dalej', () => {
  const ext = extents([], { width: 307, depth: 184 });
  const wide = isoView(ext, 42, 16 / 9), narrow = isoView(ext, 42, 0.86);
  assert.ok(wide.dist < ext.diag, `${wide.dist} < ${ext.diag}`);
  assert.ok(narrow.dist > wide.dist);
  assert.deepEqual(wide.target, [ext.cx, 0, ext.cz]);
  assert.ok(wide.pos[1] > 0);
});

test('extents: z narożników — długi regał nie powiększa hali w głąb', () => {
  const e = extents([{ x: 240, y: 180, angle: 0, width: 47, depth: 0.6 }], { width: 307, depth: 184 });
  assert.equal(e.z, 184);                                       // stary wzór dawał 180 + 47 + 2
});

test('ściany: przekrój chowa ścianę po stronie kamery, normalna doku = najbliższa ściana', () => {
  const walls = hallWalls({ width: 100, depth: 50 });
  const hidden = walls.filter((w) => wallHidden(w, 140, 25)).map((w) => [w.nx, w.nz]);
  assert.deepEqual(hidden, [[1, 0]]);                           // kamera za prawą ścianą
  assert.equal(walls.filter((w) => wallHidden(w, 50, 25)).length, 0);   // kamera w hali — wszystkie
  assert.deepEqual(outward(99, 20, { width: 100, depth: 50 }), [1, 0]);
  assert.deepEqual(outward(30, 1, { width: 100, depth: 50 }), [0, -1]);
});

test('jakość: wybór użytkownika wygrywa, bez wyboru szybka dla bardzo dużych hal', () => {
  const big = [{ n_bays: FAST_ABOVE + 1, n_levels: 1 }];
  assert.equal(effectiveQuality(null, [VNA]), 'high');
  assert.equal(effectiveQuality(null, big), 'fast');
  assert.equal(effectiveQuality('high', big), 'high');
  assert.equal(effectiveQuality('fast', [VNA]), 'fast');
});

test('zakres głębi (G2c): warstwy 1,2 cm nad posadzką rozróżnialne z każdej odległości — bez migotania', async () => {
  const { depthRange, depthStep } = await import('../../static/twin/js/scene-data.js');
  assert.ok(depthStep(300, 0.05) > 0.05, 'stary near = 0,05 m: ~10 cm rozdzielczości na 300 m (przyczyna stroboskopu)');
  for (const d of [3, 20, 80, 300, 900]) {
    const { near, far } = depthRange(d, 500);
    assert.ok(depthStep(d, near) < 0.005, `odległość ${d} m: ${depthStep(d, near)} m`);
    assert.ok(depthStep(d + 250, near) < 0.01, `dalszy brzeg hali (+250 m) przy ${d} m`);
    assert.ok(near <= Math.max(0.5, d / 20) && far > d * 4, 'cel i hala w kadrze nie są obcinane (orbita: min. 1,5 m od celu)');
  }
});
