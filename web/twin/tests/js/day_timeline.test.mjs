import { test } from 'node:test';
import assert from 'node:assert/strict';
import { buildTracks, countersAt, dayRange, hashId, lPath, palletAt, rackFront, rectSlot, seriesAt, upperBound,
  vehicleAt, TRAVEL_S } from '../../static/twin/js/day-timeline.js';

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
