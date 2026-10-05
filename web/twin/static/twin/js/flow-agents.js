// Bryły agentów odtwarzacza przepływów (flow-player.js): wózki z equipment-models.js, pracownicy, etykiety.
// Układ lokalny: X do przodu, Y w górę, Z w bok; `carriage` = część ruchoma (wózek wideł / kabina VNA).
import * as THREE from 'three';
import { MODELS, STEEL, WHEEL, SENSOR, modelHeight } from './equipment-models.js';

export const UNIT_BOX = new THREE.BoxGeometry(1, 1, 1);
const SKIN = 0xf2c9a0, TROUSERS = 0x374151;
const DARK = new Set([STEEL, WHEEL, SENSOR]);

// Rodzaj agenta ze sceny „twinema.scene” → model sprzętu (ept = pracownik prowadzący wózek paletowy).
export const AGENT_MODEL = { forklift: 'reach', kombi: 'vna', agv: 'agv', ept: 'ptruck' };

// Pudełka jak w skrypcie Blendera: (cx, cy, cz, sx, sy, sz, idx) — X do przodu, Z w górę.
function boxes(list, mats, parent) {
  for (const [cx, cy, cz, sx, sy, sz, mi] of list) {
    const mesh = new THREE.Mesh(UNIT_BOX, mats[mi]);
    mesh.position.set(cx, cz, cy); mesh.scale.set(sx, sz, sy);
    mesh.castShadow = true;
    parent.add(mesh);
  }
}

// Części modelu [l, h, w, x, y dołu, kolor, z] → siatki (wspólna geometria, materiał na kolor).
function parts(list, parent) {
  const mats = new Map();
  for (const [l, h, w, x, y, color, z = 0] of list) {
    if (!mats.has(color)) {
      mats.set(color, new THREE.MeshStandardMaterial({ color, roughness: 0.6, metalness: DARK.has(color) ? 0.4 : 0.1 }));
    }
    const mesh = new THREE.Mesh(UNIT_BOX, mats.get(color));
    mesh.position.set(x, y + h / 2, z); mesh.scale.set(l, h, w);
    mesh.castShadow = true;
    parent.add(mesh);
  }
}

function labelSprite(text) {
  const cv = document.createElement('canvas'); cv.width = 256; cv.height = 56;
  const x = cv.getContext('2d');
  x.fillStyle = 'rgba(15,23,42,0.78)'; x.fillRect(0, 0, 256, 56);
  x.fillStyle = '#fff'; x.font = 'bold 26px sans-serif'; x.textAlign = 'center'; x.textBaseline = 'middle';
  x.fillText(String(text).slice(0, 18), 128, 29);
  const tex = new THREE.CanvasTexture(cv); tex.colorSpace = THREE.SRGBColorSpace;
  const spr = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, depthTest: false }));
  spr.scale.set(2.2, 0.48, 1); spr.renderOrder = 10;
  return spr;
}

/** Agent sceny → {obj, carriage, label}; kolor kamizelki pracownika = a.color, wózki w kolorze rodzaju sprzętu. */
export function buildAgent(a) {
  const obj = new THREE.Group();
  const model = AGENT_MODEL[a.kind];
  let carriage = null;
  if (model) {
    parts(MODELS[model].body, obj);
    if (MODELS[model].lift.length) { carriage = new THREE.Group(); parts(MODELS[model].lift, carriage); obj.add(carriage); }
  }
  if (!model || a.kind === 'ept') {
    const x = a.kind === 'ept' ? -1.0 : 0;                   // operator za dyszlem wózka paletowego
    boxes([[x, 0, 0.45, 0.22, 0.3, 0.9, 1], [x, 0, 1.2, 0.26, 0.46, 0.62, 0],
           [x, 0, 1.66, 0.22, 0.2, 0.26, 2], [x + 0.14, 0, 1.2, 0.05, 0.3, 0.05, 0]],
          [new THREE.MeshStandardMaterial({ color: a.color, roughness: 0.55, metalness: 0.1 }),
           new THREE.MeshStandardMaterial({ color: TROUSERS, roughness: 0.8 }),
           new THREE.MeshStandardMaterial({ color: SKIN, roughness: 0.7 })], obj);
  }
  const label = labelSprite(a.label);
  label.position.set(0, model && a.kind !== 'ept' ? modelHeight(model) + 0.5 : 2.3, 0);
  obj.add(label);
  return { obj, carriage, label };
}
