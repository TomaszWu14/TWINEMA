import { test } from 'node:test';
import assert from 'node:assert/strict';
import { nearestEntry, sitePlan, siteToHall } from '../../static/twin/js/scene-data.js';
import { ENTER_S, TRAVEL_S, vehicleAt, vehiclePose } from '../../static/twin/js/day-timeline.js';

const SITE = { width: 200, depth: 150, hall: { x: 45, y: 30, angle: 0 }, setback: { road: 12, other: 6 }, access_side: 'S',
  entries: [{ kind: 'truck', side: 'S', pos: 20, width: 10 }, { kind: 'truck', side: 'S', pos: 180, width: 10 },
    { kind: 'car', side: 'S', pos: 100, width: 6 }],
  areas: [{ kind: 'yard', label: 'Plac', x: 0, y: 30, width: 45, depth: 80, angle: 0 }] };
const close = (a, b) => assert.ok(Math.abs(a - b) < 1e-9, `${a} ≈ ${b}`);

test('siteToHall: narożnik hali = (0, 0), obrót odwrotny do położenia hali', () => {
  assert.deepEqual(siteToHall(SITE, [45, 30]), [0, 0]);
  const rot = { ...SITE, hall: { x: 10, y: 20, angle: 90 } };
  const [a, c] = siteToHall(rot, [10, 15]);                // u_w(90°) = (0, −1) → 5 m wzdłuż hali
  close(a, 5); close(c, 0);
});

test('sitePlan: granica, linie zabudowy (od drogi po stronie dojazdu), wjazdy skierowane w głąb działki', () => {
  const p = sitePlan(SITE);
  assert.deepEqual(p.plot[0], [-45, -30]);
  assert.deepEqual(p.building[0], [6 - 45, 6 - 30]);
  assert.deepEqual(p.building[2], [200 - 6 - 45, 150 - 12 - 30]);
  assert.deepEqual(p.entries[0].at, [20 - 45, 150 - 30]);
  assert.deepEqual(p.entries[0].dir, [0, -1]);
  assert.equal(p.areas[0].pts.length, 4);
  assert.equal(sitePlan({}), null);
});

test('nearestEntry: wg rodzaju; bez wjazdu osobowego — najbliższy dla tirów', () => {
  const p = sitePlan(SITE);
  assert.equal(nearestEntry(p, [140, 50]).at[0], 180 - 45);
  assert.equal(nearestEntry(p, [0, 0], 'car').kind, 'car');
  const noCar = sitePlan({ ...SITE, entries: SITE.entries.filter((e) => e.kind === 'truck') });
  assert.equal(nearestEntry(noCar, [0, 0], 'car').kind, 'truck');
  assert.equal(nearestEntry(null, [0, 0]), null);
});

test('vehicleAt z działką: dojazd przed kolejką, wyjazd po odjeździe; bez działki bez zmian', () => {
  const tr = { t: [1000, 3000, 6000], what: ['arrive', 'dock', 'depart'], place: ['gate', 'dock:1', 'dock:1'], t0: 1000, t1: 6000 };
  assert.equal(vehicleAt(tr, 1010, ENTER_S).phase, 'enter');
  assert.equal(vehicleAt(tr, 1010).phase, 'queue');
  assert.equal(vehicleAt(tr, 1000 + ENTER_S + 1, ENTER_S).phase, 'queue');
  assert.equal(vehicleAt(tr, 6000 + TRAVEL_S + 10, ENTER_S).phase, 'leave');
  assert.equal(vehicleAt(tr, 6000 + TRAVEL_S + 10), null);
  assert.equal(vehicleAt(tr, 6000 + TRAVEL_S + ENTER_S + 1, ENTER_S), null);
});

test('vehiclePose: dojazd od wjazdu działki do pasa przed dokiem i powrót', () => {
  const d = { wall: [0, 20], out: [-1, 0] }, entry = [-25, 120];
  const s = vehiclePose({ phase: 'enter', p: 0 }, d, 'truck', {}, 0, entry);
  assert.deepEqual([s.x, s.y], entry);
  const e = vehiclePose({ phase: 'enter', p: 1 }, d, 'truck', {}, 0, entry);
  close(e.x, -34); close(e.y, 20);                          // pas doku: QUEUE_M = 34 m od ściany
  const back = vehiclePose({ phase: 'leave', p: 1 }, d, 'truck', {}, 0, entry);
  assert.deepEqual([back.x, back.y], entry);
});

// ── D2: granica-wielokąt (lustro testów twin/tests/test_site.py PolygonPlotTests) ──
import { edgeSetbacks, entryOnBoundary, insertIndex, insetPolygon, plotPolygon, polygonArea }
  from '../../static/twin/js/site-geom.js';

const L = [[0, 0], [120, 0], [120, 60], [200, 60], [200, 160], [0, 160]];
const POLY = { ...SITE, width: 200, depth: 160, boundary: L };

test('wielokąt: pole, odstęp od drogi tylko na krawędzi zwróconej ku dojazdowi', () => {
  assert.equal(Math.abs(polygonArea(plotPolygon(POLY))), 200 * 160 - 80 * 60);
  assert.deepEqual(edgeSetbacks(POLY), [6, 6, 6, 6, 12, 6]);
  assert.equal(plotPolygon(SITE).length, 4);                           // bez boundary — prostokąt
});

test('linia zabudowy wielokąta: krawędzie przesunięte do środka o swój odstęp', () => {
  const b = insetPolygon(L, edgeSetbacks(POLY));
  assert.deepEqual(b.map(([x, y]) => [Math.round(x), Math.round(y)]),
    [[6, 6], [114, 6], [114, 66], [194, 66], [194, 148], [6, 148]]);
  assert.equal(insetPolygon([[0, 0], [10, 0], [10, 10], [0, 10]], [8, 8, 8, 8]), null);   // odstępy zjadają działkę
});

test('wjazd od północy na x = 160 trafia w krawędź wcięcia (y = 60), kierunek w głąb', () => {
  const { at, dir } = entryOnBoundary(POLY, { side: 'N', pos: 160 });
  assert.deepEqual(at, [160, 60]);
  close(dir[0], 0); close(dir[1], 1);
  assert.deepEqual(entryOnBoundary(SITE, { side: 'S', pos: 20 }).at, [20, 150]);   // prostokąt jak D1
});

test('wstawianie wierzchołka kliknięciem: za początkiem najbliższej krawędzi', () => {
  assert.equal(insertIndex(L, [60, 1]), 1);                             // krawędź (0,0)→(120,0)
  assert.equal(insertIndex(L, [199, 100]), 4);                          // krawędź (200,60)→(200,160)
  assert.equal(insertIndex(L, [1, 80]), 6);                             // krawędź zamykająca (0,160)→(0,0)
});
