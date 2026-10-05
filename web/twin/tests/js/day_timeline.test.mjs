import { test } from 'node:test';
import assert from 'node:assert/strict';
import { STAND_M, buildTracks, countersAt, crewAt, dayRange, hashId, lPath, lPathYaw, orderedSlot, palletAt,
  queueSides, rackFront, rectSlot, seriesAt, slotOrder, stationSpots, upperBound, vehicleAt, vehiclePose, yawOut,
  TRAVEL_S } from '../../static/twin/js/day-timeline.js';

const EV = [
  [3600, 'in1', 'container', 'arrive', 'gate'],
  [4000, 'in1', 'container', 'dock', 'dock:7'],
  [4500, 'in1-p1', 'pallet', 'built', 'palletize'],
  [4600, 'in1-p1', 'pallet', 'staging', 'staging_in'],
  [5000, 'in1-p1', 'pallet', 'move', 'staging_in'],
  [5200, 'in1-p1', 'pallet', 'stored', 'rack'],
  [8000, 'in1', 'container', 'depart', 'dock:7'],
  [9000, 'out1-p1', 'pallet', 'retrieved', 'rack'],
  [9500, 'out1-p1', 'pallet', 'staging', 'staging_out'],
  [10000, 'o1', 'parcel', 'packed', 'pack', 3],
  [10800, 'out1', 'truck', 'arrive', 'gate'],
  [11000, 'out1', 'truck', 'dock', 'dock:9'],
  [11000, 'out1-p1', 'pallet', 'loaded', 'dock:9'],
  [11500, 'k1', 'courier', 'dock', 'dock:9'],
  [12000, 'out1', 'truck', 'depart', 'dock:9'],
  [12500, 'o2', 'parcel', 'packed', 'pack'],
];

test('upperBound — wyszukiwanie binarne', () => {
  assert.equal(upperBound([1, 2, 2, 5], 2), 3);
  assert.equal(upperBound([1, 2, 2, 5], 0), 0);
  assert.equal(upperBound([1, 2, 2, 5], 9), 4);
});

test('pojazd: kolejka → dojazd → dok → odjazd → poza sceną', () => {
  const tr = buildTracks(EV).get('in1');
  assert.equal(vehicleAt(tr, 3000), null);
  assert.equal(vehicleAt(tr, 3700).phase, 'queue');
  const v = vehicleAt(tr, 4000 - TRAVEL_S / 2);
  assert.equal(v.phase, 'in'); assert.equal(v.dock, '7'); assert.ok(Math.abs(v.p - 0.5) < 1e-9);
  assert.equal(vehicleAt(tr, 6000).phase, 'dock');
  assert.equal(vehicleAt(tr, 8000 + TRAVEL_S / 2).phase, 'out');
  assert.equal(vehicleAt(tr, 9000), null);
});

test('paleta: stanowisko → pole → przejazd → regał (znika)', () => {
  const tr = buildTracks(EV).get('in1-p1');
  assert.equal(palletAt(tr, 4400), null);
  assert.deepEqual(palletAt(tr, 4500), { at: 'palletize' });
  assert.deepEqual(palletAt(tr, 4700), { at: 'staging_in' });
  const m = palletAt(tr, 5100);
  assert.equal(m.to, 'rack'); assert.ok(Math.abs(m.p - 0.5) < 1e-9);
  assert.equal(palletAt(tr, 5300), null);
});

test('paleta wydań: z regału na pole (ostatnie 2 min), znika po załadunku', () => {
  const tr = buildTracks(EV).get('out1-p1');
  assert.deepEqual(palletAt(tr, 9100), { at: 'rack' });
  const m = palletAt(tr, 9440);
  assert.equal(m.from, 'rack'); assert.equal(m.to, 'staging_out'); assert.ok(m.p > 0.4 && m.p < 0.6);
  assert.deepEqual(palletAt(tr, 10000), { at: 'staging_out' });
  assert.equal(palletAt(tr, 11001), null);
});

test('stary format bez „loaded”: paleta znika, gdy jej auto podjeżdża do doku', () => {
  const tr = buildTracks(EV.filter((e) => e[3] !== 'loaded')).get('out1-p1');
  assert.deepEqual(palletAt(tr, 10900), { at: 'staging_out' });
  assert.equal(palletAt(tr, 11001), null);
});

test('liczniki w chwili t', () => {
  const tracks = buildTracks(EV);
  const a = countersAt(tracks, 4700);
  assert.equal(a.palletsIn, 1); assert.equal(a.stagingIn, 1); assert.equal(a.atDock, 1);
  const b = countersAt(tracks, 10500);
  assert.equal(b.parcels, 3); assert.equal(b.pending, 3); assert.equal(b.stagingOut, 1);
  const c = countersAt(tracks, 13000);
  assert.equal(c.palletsOut, 1); assert.equal(c.parcels, 4); assert.equal(c.pending, 1);   // kurier o 11 500 zabrał 3
});

test('zakres dnia, seria osi czasu', () => {
  assert.deepEqual(dayRange(EV), [3600, 12600]);            // ostatnie 12 500 + dojazd 90 s → 12 600
  assert.equal(seriesAt([1, 2, 3], 900, 1000), 2);
  assert.equal(seriesAt([1, 2, 3], 900, 99999), 3);
  assert.equal(seriesAt([], 900, 5), 0);
});

test('geometria: sloty na polu, regał wg id, przejazd w L', () => {
  const rect = { x: 0, y: 0, w: 2.8, d: 1.4, angle: 0 };
  assert.deepEqual(rectSlot(rect, 0), [0.7, 0.7, 0]);
  assert.deepEqual(rectSlot(rect, 1).map((v) => Math.round(v * 1e6) / 1e6), [2.1, 0.7, 0]);
  assert.deepEqual(rectSlot(rect, 2), [0.7, 0.7, 1]);      // pole pełne → druga warstwa
  const racks = [{ x: 10, y: 5, angle: 0, width: 4 }, { x: 20, y: 5, angle: 0, width: 4 }];
  assert.deepEqual(rackFront(racks, 'in1-p1'), rackFront(racks, 'in1-p1'));
  assert.equal(rackFront([], 'x'), null);
  assert.equal(hashId('abc'), hashId('abc'));
  assert.deepEqual(lPath([0, 0], [10, 10], 0.25), [5, 0]);
  assert.deepEqual(lPath([0, 0], [10, 10], 0.75), [10, 5]);
  assert.deepEqual(lPath([0, 0], [10, 10], 2), [10, 10]);
});

// ── G1b: auta przy swoich dokach, kolejka bez nakładania, obsada w czasie ──────────────────────
const DOCKS = {
  1: { x: 2, y: 71.35, out: [-1, 0], wall: [0, 71.35], role: 'in_container' },
  2: { x: 2, y: 76.35, out: [-1, 0], wall: [0, 76.35], role: 'in_container' },
  9: { x: 305, y: 84, out: [1, 0], wall: [307.2, 84], role: 'out' },
};
const BODY = { truck: [-6.8, 9.35], container: [-6.1, 8.65] };   // tył naczepy … przód kabiny (oś +x auta)
function footprint(p, kind) {                                    // obrys osiowy [x0, x1, y0, y1]
  const ux = Math.cos(p.yaw), uy = -Math.sin(p.yaw), [b, f] = BODY[kind];
  const xs = [p.x + ux * b, p.x + ux * f, p.x + uy * 1.3, p.x - uy * 1.3];
  const ys = [p.y + uy * b, p.y + uy * f, p.y + ux * 1.3, p.y - ux * 1.3];
  return [Math.min(...xs), Math.max(...xs), Math.min(...ys), Math.max(...ys)];
}
const overlap = (a, b) => a[0] < b[1] && b[0] < a[1] && a[2] < b[3] && b[2] < a[3];

test('auto w doku: tył naczepy 0,3 m od ściany, na zewnątrz, tyłem do bramy', () => {
  const sides = queueSides(DOCKS);
  const p = vehiclePose({ phase: 'dock' }, DOCKS[1], 'truck', sides);
  assert.ok(Math.abs(p.x + STAND_M.truck) < 1e-9 && Math.abs(p.y - 71.35) < 1e-9);
  assert.equal(p.yaw, yawOut([-1, 0]));
  assert.ok(Math.abs(footprint(p, 'truck')[1] - -0.3) < 1e-9);       // tył naczepy 0,3 m przed ścianą x = 0
  const q = footprint(vehiclePose({ phase: 'dock' }, DOCKS[9], 'truck', sides), 'truck');
  assert.ok(Math.abs(q[0] - 307.5) < 1e-9);                           // po stronie wydań — poza halą, nie w ścianie
});

test('auta w dokach i w kolejce nie nachodzą na siebie', () => {
  const sides = queueSides(DOCKS);
  const fps = [
    footprint(vehiclePose({ phase: 'dock' }, DOCKS[1], 'container', sides), 'container'),
    footprint(vehiclePose({ phase: 'dock' }, DOCKS[2], 'truck', sides), 'truck'),
    ...[0, 1, 2, 3, 4, 5].map((i) => footprint(vehiclePose({ phase: 'queue' }, DOCKS[1], 'truck', sides, i), 'truck')),
  ];
  for (let i = 0; i < fps.length; i++) {
    for (let j = i + 1; j < fps.length; j++) assert.ok(!overlap(fps[i], fps[j]), `${i} vs ${j}`);
  }
  const qo = vehiclePose({ phase: 'queue' }, DOCKS[9], 'truck', sides, 0);
  assert.ok(qo.x > 307.2 + 20);                                       // kolejka wydań przed swoją ścianą, nie w hali
});

test('dojazd: z pasa przed dokiem do postoju (bez jazdy przez halę)', () => {
  const sides = queueSides(DOCKS), d = DOCKS[1];
  const a = vehiclePose({ phase: 'in', p: 0 }, d, 'truck', sides), b = vehiclePose({ phase: 'in', p: 1 }, d, 'truck', sides);
  assert.ok(a.x < -30 && Math.abs(a.y - 71.35) < 1e-9);
  assert.ok(Math.abs(b.x + STAND_M.truck) < 1e-9);
  const o = vehiclePose({ phase: 'out', p: 0.5 }, d, 'truck', sides);
  assert.ok(o.x < b.x && o.x > a.x);                                 // odjazd tą samą drogą na zewnątrz
});

test('pole odkładcze rośnie od doków; kierunek jazdy na L', () => {
  const r = { x: 13, y: 1, w: 11, d: 182, angle: 0 };
  const order = slotOrder(r, [2, 90]);
  const [x, y] = orderedSlot(r, order, 0);
  assert.ok(Math.abs(y - 90) < 1.5 && x < 15);                       // pierwsza paleta najbliżej doków
  assert.equal(orderedSlot(r, order, order.length)[2], 1);          // po zapełnieniu — druga warstwa
  assert.equal(lPathYaw([0, 0], [10, 5], 0.2), 0);
  assert.equal(lPathYaw([0, 0], [10, 5], 0.9), -Math.PI / 2);
  assert.equal(lPathYaw([10, 0], [0, -5], 0.2), Math.PI);
});

test('obsada w chwili t z osi czasu (co 15 min) i miejsca przy stołach', () => {
  const people = { pack: [0, 4, 6], pick: [8, 8, 2] };
  assert.deepEqual(crewAt(people, 900, 1000), { pack: 4, pick: 8 });
  assert.deepEqual(crewAt(people, 900, 99999), { pack: 6, pick: 2 });
  const spots = stationSpots([{ x: 0, y: 0, w: 4, d: 4, angle: 0 }, { x: 10, y: 0, w: 4, d: 4, angle: 0 }], 3);
  assert.equal(spots.length, 3);
  assert.deepEqual(spots[0], [2, -0.5]);                             // przed pierwszym stołem
  assert.deepEqual(spots[1], [12, -0.5]);                            // potem kolejny stół
  assert.notDeepEqual(spots[2], spots[0]);
  assert.deepEqual(stationSpots([], 5), []);
});
