// G2: kolor regału wg trybu, strefa pod regałem, legenda, obrys, cień kontaktowy, właściciele instancji.
import { test } from 'node:test';
import assert from 'node:assert/strict';
import { colorLegend, contactShadowPart, decorParts, localToWorld, NEUTRAL_RACK, rackClass, rackMatrices, rackOutline,
  rackTint, rackZone, RACK_TYPE_COLORS } from '../../static/twin/js/scene-data.js';

const rack = (o = {}) => ({ x: 0, y: 0, angle: 0, width: 5.4, depth: 1.1, level_h: 1.8, n_bays: 2, n_levels: 3, ...o });
const ADR = { kind: 'zone_adr', kind_label: 'Strefa ADR', x: 20, y: 10, width: 12, depth: 8, angle: 30, color: '#d07a3a' };

test('rackClass: pole z serwera > equipment z edytora > geometria starych danych', () => {
  assert.equal(rackClass(rack({ rack_class: 'vna', equipment: 'shelf' })), 'vna');
  assert.equal(rackClass(rack({ equipment: 'reach' })), 'pallet');
  assert.equal(rackClass(rack({ equipment: 'shelf' })), 'shelf');
  assert.equal(rackClass(rack({ level_h: 0.5 })), 'shelf');
  assert.equal(rackClass(rack()), 'pallet');
});

test('rackZone: środek regału w obróconej strefie — tak; obok — nie', () => {
  const [x, y] = localToWorld(ADR, [6, 4]);
  assert.equal(rackZone(rack({ x: x - 2.7, y: y - 0.55 }), [ADR]), ADR);
  assert.equal(rackZone(rack({ x: x + 20, y }), [ADR]), null);
  assert.equal(rackZone(rack({ x: x - 2.7, y: y - 0.55 }), [{ ...ADR, kind: 'corridor' }]), null);   // nie strefa specjalna
});

test('rackTint: typ, strefa (kolor elementu jak na planie), wypełnienie z progami; brak danych = neutralny', () => {
  const [x, y] = localToWorld(ADR, [6, 4]), inZone = rack({ x: x - 2.7, y: y - 0.55, rack_class: 'vna' });
  assert.equal(rackTint(inZone, 'type', [ADR]), RACK_TYPE_COLORS.vna);
  assert.equal(rackTint(inZone, 'zones', [ADR]), '#d07a3a');
  assert.equal(rackTint(rack(), 'zones', [ADR]), NEUTRAL_RACK);
  assert.deepEqual([10, 60, 95].map((p) => rackTint(rack({ fill_pct: p }), 'fill', [])), ['#3fa66b', '#e0a92b', '#d4553f']);
  assert.equal(rackTint(rack(), 'fill', []), NEUTRAL_RACK);
});

test('colorLegend: tylko kategorie obecne w hali', () => {
  assert.deepEqual(colorLegend([rack({ equipment: 'vna' })], 'type', []).map(([c]) => c), [RACK_TYPE_COLORS.vna]);
  const [x, y] = localToWorld(ADR, [6, 4]);
  const zones = colorLegend([rack({ x: x - 2.7, y: y - 0.55 }), rack()], 'zones', [ADR]);
  assert.deepEqual(zones, [['#d07a3a', 'Strefa ADR'], [NEUTRAL_RACK, 'Poza strefami specjalnymi']]);
  assert.equal(colorLegend([rack()], 'fill', []).length, 1);                                       // brak danych o stanie
});

test('rackOutline: 12 krawędzi (24 wierzchołki) od posadzki do wierzchu regału, narożniki po obrocie', () => {
  const r = rack({ x: 3, y: 4, angle: 90 }), v = rackOutline(r);
  assert.equal(v.length, 24 * 3);
  const ys = new Set(v.filter((_, i) => i % 3 === 1));
  assert.deepEqual([...ys].sort((a, b) => a - b), [0.02, 5.4]);
  const [wx, wz] = localToWorld(r, [r.width, 0]);
  assert.ok(v.some((_, i) => i % 3 === 0 && Math.abs(v[i] - wx) < 1e-9 && Math.abs(v[i + 2] - wz) < 1e-9));
});

test('cień kontaktowy szerszy od regału; właściciele instancji wskazują regał', () => {
  const [[, sx, , sz]] = contactShadowPart(rack(), 0.35);
  assert.ok(sx > 5.4 && sz > 1.1);
  const racks = [rack(), rack({ x: 10, n_bays: 4 })], m = rackMatrices(racks, decorParts);
  const per = racks.map((r, i) => decorParts(r, i).filter((p) => p[0] === 'pload').length);
  assert.equal(m._owner.pload.length, per[0] + per[1]);
  assert.equal(m._owner.pload[0], 0);
  assert.equal(m._owner.pload[m._owner.pload.length - 1], 1);
});
