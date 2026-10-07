// Wnętrze hali (G10): kratownice dachu, płatwie i lampy high-bay — InstancedMesh (kilka draw calli), bez
// prawdziwych świateł i cieni (koszt). Widoczne tylko przy niskiej kamerze (ujęcia z bliska, przeloty);
// z góry i w izometrii całej hali chowane, żeby nie zasłaniać regałów.
import * as THREE from 'three';
import { interiorLayout } from './scene-data.js';

const BOX = new THREE.BoxGeometry(1, 1, 1);
const LAMP = new THREE.CylinderGeometry(0.32, 0.22, 0.4, 14);
const LENS = new THREE.CylinderGeometry(0.21, 0.21, 0.02, 14);
export const TRUSS_H = 1.4;

function instances(geo, mat, list) {
  const m = new THREE.InstancedMesh(geo, mat, Math.max(1, list.length)), M = new THREE.Matrix4();
  const Q = new THREE.Quaternion(), E = new THREE.Euler(), P = new THREE.Vector3(), S = new THREE.Vector3();
  list.forEach(([x, y, z, sx, sy, sz, rx = 0], i) => m.setMatrixAt(i, M.compose(P.set(x, y, z), Q.setFromEuler(E.set(rx, 0, 0)), S.set(sx, sy, sz))));
  m.count = list.length;
  return m;
}

/** → THREE.Group (userData.showBelow = wysokość kamery, poniżej której wnętrze widać); h = wysokość ścian. */
export function buildInterior(floor, h, features, track) {
  const { trusses, lamps } = interiorLayout(floor, features);
  // h = wysokość w świetle + 1,5 m → pas dolny ≈ wysokość w świetle; lampy tuż pod nim kończą się ~0,5 m niżej,
  // czyli nad najwyższym dopuszczalnym regałem (E2b: regał > wysokość − 0,5 m = błąd).
  const top = h - 0.2, bot = top - TRUSS_H, D = floor.depth, steel = [], housing = [], lens = [];
  for (const x of trusses) {
    steel.push([x, top, D / 2, 0.2, 0.2, D], [x, bot, D / 2, 0.16, 0.16, D]);          // pas górny i dolny
    const k = Math.max(2, Math.round(D / 2.5)), seg = D / k, len = Math.hypot(seg, TRUSS_H), a = Math.atan2(seg, TRUSS_H);
    for (let i = 0; i < k; i++) steel.push([x, (top + bot) / 2, (i + 0.5) * seg, 0.08, len, 0.08, i % 2 ? a : -a]);   // krzyżulce
  }
  for (let z = 3; z < D; z += 3) steel.push([floor.width / 2, top + 0.2, z, floor.width, 0.16, 0.12]);   // płatwie
  for (const [x, z] of lamps) {
    housing.push([x, bot - 0.2, z, 1, 1, 1]);
    lens.push([x, bot - 0.41, z, 1, 1, 1]);
  }
  const steelMat = track(new THREE.MeshStandardMaterial({ color: 0x8b929b, roughness: 0.55, metalness: 0.35 }));
  const g = new THREE.Group();
  g.add(instances(BOX, steelMat, steel),
    instances(LAMP, track(new THREE.MeshStandardMaterial({ color: 0x3f4650, roughness: 0.4, metalness: 0.6 })), housing),
    instances(LENS, track(new THREE.MeshBasicMaterial({ color: 0xfff1d0, toneMapped: false })), lens));
  g.userData.showBelow = h * 1.6;
  return g;
}
