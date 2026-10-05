// G2b — modele sprzętu z brył (equipment-models.js). `node --test`.
import assert from 'node:assert/strict';
import test from 'node:test';

import { CARRY, EQUIPMENT_COLORS, MODELS, modelForEquipment, modelHeight, modelParts }
  from '../../static/twin/js/equipment-models.js';

const KINDS = ['reach', 'vna', 'ptruck', 'counterbalance', 'agv', 'amr'];

test('każdy rodzaj ma bryły o dodatnich wymiarach, w budżecie i z kolorem rodzaju', () => {
  for (const k of KINDS) {
    const parts = modelParts(k);
    assert.ok(parts.length > 3 && parts.length <= 16, `${k}: ${parts.length} brył`);
    for (const [l, h, w, x, y, color, z = 0] of parts) {
      assert.ok(l > 0 && h > 0 && w > 0, `${k}: wymiary`);
      assert.ok(y >= 0 && Number.isFinite(x + z) && Number.isInteger(color), `${k}: położenie/kolor`);
    }
    assert.ok(MODELS[k].body.some((p) => p[5] === EQUIPMENT_COLORS[k]), `${k}: nadwozie w kolorze rodzaju`);
    assert.ok(CARRY[k] && CARRY[k].z > 0, `${k}: paleta na pojeździe`);
  }
});

test('wysokości: maszt VNA > reach > czołowy; AMR < 0,5 m; AGV bez kabiny powyżej 1,2 m', () => {
  assert.ok(modelHeight('vna') > modelHeight('reach'));
  assert.ok(modelHeight('reach') > modelHeight('counterbalance'));
  assert.ok(modelHeight('amr') < 0.5);
  assert.ok(modelHeight('agv') <= 1.2);
  assert.ok(MODELS.vna.lift.length && MODELS.reach.lift.length, 'ruchoma kabina/wózek wideł');
});

test('kolory rodzajów są różne', () => {
  const cs = KINDS.map((k) => EQUIPMENT_COLORS[k]);
  assert.equal(new Set(cs).size, KINDS.length);
});

test('typ z katalogu → model', () => {
  assert.equal(modelForEquipment('agv'), 'agv');
  assert.equal(modelForEquipment('amr'), 'amr');
  assert.equal(modelForEquipment('pallet_truck'), 'ptruck');
  assert.equal(modelForEquipment('conveyor'), null);
  assert.equal(modelForEquipment(''), null);
});
