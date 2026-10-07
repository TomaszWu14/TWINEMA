// Modele .glb sprzętu, aut przy dokach, ludzi i palety (G6, G7) — budowane skryptem tools/blender/twinema_models.py do ../models/.
// Ładowane raz (top-level await — moduły odtwarzaczy czekają) i rozbite na [geometria, materiał] z wypaloną
// transformacją: odtwarzacz robi jedną siatkę instancyjną na materiał. Brak pliku / błąd / limit czasu →
// brak klucza w GLB i odtwarzacz zostaje przy bryłach z equipment-models.js.
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

export const GLB_KINDS = ['reach', 'vna', 'ptruck', 'counterbalance', 'agv', 'amr', 'person', 'pallet', 'truck', 'container',
  'courier'];
const LOAD_TIMEOUT_MS = 6000;

/** gltf.scene → {body: [[geometry, material]], lift: [...]} (grupa = nazwa węzła-przodka body/lift). */
function split(root) {
  root.updateMatrixWorld(true);
  const out = { body: [], lift: [] };
  root.traverse((o) => {
    if (!o.isMesh) return;
    let g = o;
    while (g && !(g.name in out)) g = g.parent;
    out[g ? g.name : 'body'].push([o.geometry.clone().applyMatrix4(o.matrixWorld), o.material]);
  });
  return out;
}

async function loadAll() {
  const loader = new GLTFLoader(), base = new URL('../models/', import.meta.url);
  const got = await Promise.all(GLB_KINDS.map((k) => loader.loadAsync(new URL(`${k}.glb`, base).href)
    .then((g) => [k, split(g.scene)], () => null)));
  return Object.fromEntries(got.filter(Boolean));
}

/** kind → {body, lift}; pusty obiekt, gdy modele nie doszły na czas. */
export const GLB = await Promise.race([loadAll().catch(() => ({})),
  new Promise((ok) => setTimeout(() => ok({}), LOAD_TIMEOUT_MS))]);
