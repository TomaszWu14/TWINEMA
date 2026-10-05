// Czyste funkcje sceny 3D (scene-data.js). Uruchamia twin/tests/test_layout_editor_js.py (`node --test`).
import assert from 'node:assert/strict';
import test from 'node:test';

import { corners } from '../../static/twin/js/layout-core.js';
import { editorScene, extents, localToWorld, steelMatrices, steelMode, steelParts }
  from '../../static/twin/js/scene-data.js';

const near = (a, b, eps = 1e-9) => assert.ok(Math.abs(a - b) < eps, `${a} ≈ ${b}`);
const near32 = (a, b) => near(a, b, 1e-4);     // Float32Array (instanceMatrix)
const rack = (o) => ({ zone: 'A', rack_id: '001', x: 0, y: 0, angle: 0, n_bays: 4, n_levels: 3,
  bay_width_cm: 270, depth_cm: 110, level_height_cm: 180, ...o });

test('3D: punkt lokalny regału trafia w narożniki edytora 2D (ta sama konwencja osi)', () => {
  for (const angle of [0, 30, 90, 180, 247]) {
    const r = rack({ x: 7, y: 11, angle });
    const [w, d] = [r.n_bays * r.bay_width_cm / 100, r.depth_cm / 100];
    const world = [[0, 0], [w, 0], [w, d], [0, d]].map((p) => localToWorld(r, p));
    corners(r).forEach(([x, y], i) => { near(world[i][0], x); near(world[i][1], y); });
  }
});

test('editorScene: regał edytora → format widoku (metry), słupy jako bryły o wysokości hali', () => {
  const S = { floor: { width: 40, depth: 20, clear_height: 11 }, kinds: { dock: 'Dok' },
    racks: [rack({ _k: 5 })], features: [{ kind: 'dock', label: '', x: 1, y: 2, width: 3, depth: 2, angle: 0, _k: 6 }],
    colList: [{ x: 12, y: 12, size: 0.6 }] };
  const sc = editorScene(S, { dock: '#123456' });
  const r = sc.racks[0];
  assert.deepEqual([r.width, r.depth, r.level_h, r._k], [10.8, 1.1, 1.8, 5]);
  assert.equal(sc.features[0].color, '#123456');
  assert.equal(sc.features[0].kind_label, 'Dok');
  const col = sc.features[1];
  assert.deepEqual([col.kind, col.height], ['column', 11]);
  near(col.x, 11.7); near(col.width, 0.6);
});

test('szczegółowość stali: pełna → lekka (> 3 000 gniazdo-poziomów) → XL (> 20 000)', () => {
  const r = { n_bays: 10, n_levels: 5 };
  assert.equal(steelMode([r]), 'full');
  assert.equal(steelMode(Array(61).fill(r)), 'lite');
  assert.equal(steelMode(Array(401).fill(r)), 'xl');
});

test('steelParts: liczba elementów maleje z trybem, belki XL na całą długość', () => {
  const r = { n_bays: 4, n_levels: 3, width: 10.8, depth: 1.1, level_h: 1.8 };
  const count = (m) => steelParts(r, m).length;
  assert.ok(count('full') > count('lite') && count('lite') > count('xl'));
  const xlBeams = steelParts(r, 'xl').filter((p) => p[0] === 'beam');
  assert.equal(xlBeams.length, 3 * 2);                   // poziom × przód/tył
  near(xlBeams[0][1], 10.8);
  assert.ok(steelParts(r, 'full').every((p) => p.length === 8));
});

test('steelMatrices: przesunięcie = punkt lokalny w hali, kolumny = osie obrócone i przeskalowane', () => {
  const r = { x: 7, y: 11, angle: 30, n_bays: 2, n_levels: 2, width: 5.4, depth: 1.1, level_h: 1.8 };
  const parts = steelParts(r, 'full'), mats = steelMatrices([r], 'full');
  const seen = { up: 0, beam: 0, brace: 0 };
  for (const [b, sx, sy, sz, x, y, z, a] of parts) {
    const m = mats[b].subarray(seen[b] * 16, ++seen[b] * 16);
    const [wx, wz] = localToWorld(r, [x, z]);
    near32(m[12], wx); near32(m[13], y); near32(m[14], wz); near32(m[15], 1);
    near32(Math.hypot(m[0], m[1], m[2]), sx); near32(Math.hypot(m[4], m[5], m[6]), sy); near32(Math.hypot(m[8], m[9], m[10]), sz);
    near32(m[5], Math.cos(a) * sy);                          // obrót kratownicy wokół lokalnej osi X
  }
  assert.deepEqual(Object.values(mats).map((m) => m.length / 16), Object.values(seen));
});

test('extents: hala albo dalej, gdy regał wystaje', () => {
  const e = extents([{ x: 45, y: 5, width: 10, depth: 1 }], { width: 40, depth: 20 });
  assert.deepEqual([e.x, e.z], [57, 20]);
});
