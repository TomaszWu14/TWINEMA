// Scena 3D hali (three.js) wspólna dla widoku modelu i podglądu w edytorze layoutu.
// PBR: tekstury proceduralne, IBL studyjny, ACES; stal regałów przez InstancedMesh (3 draw calle
// niezależnie od liczby regałów — strażnik mesh-explosion w test_warehouse_model_view).
// Render na żądanie: klatka tylko po zmianie kamery/danych (bez pętli 60 fps).
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { EDGE_KINDS, FLAT_KINDS, extents, steelMatrices, steelMode } from './scene-data.js';

const SCENE_MARGIN = 8;
const _unitBox = new THREE.BoxGeometry(1, 1, 1);

// ── Tekstury proceduralne (współdzielone, cache) ─────────────────────────────────────────────
const _texCache = {};
function mkTex(key, size, draw, srgb) {
  if (_texCache[key]) return _texCache[key];
  const c = document.createElement('canvas'); c.width = c.height = size;
  draw(c.getContext('2d'), size);
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  if (srgb) { t.colorSpace = THREE.SRGBColorSpace; t.anisotropy = 8; }
  return (_texCache[key] = t);
}
const hex2rgb = (h) => [parseInt(h.slice(1, 3), 16), parseInt(h.slice(3, 5), 16), parseInt(h.slice(5, 7), 16)];
function noise(x, s, amt, dark, light) {
  const d = hex2rgb(dark), l = hex2rgb(light), img = x.getImageData(0, 0, s, s), p = img.data;
  for (let i = 0; i < p.length; i += 4) {
    const c = Math.random() > 0.5 ? d : l, a = Math.random() * amt;
    p[i] += (c[0] - p[i]) * a; p[i + 1] += (c[1] - p[i + 1]) * a; p[i + 2] += (c[2] - p[i + 2]) * a;
  }
  x.putImageData(img, 0, 0);
}
const steelRough = () => mkTex('steelR', 128, (x, s) => { x.fillStyle = '#6e6e6e'; x.fillRect(0, 0, s, s); noise(x, s, 0.45, '#4a4a4a', '#a0a0a0'); });
const concreteTex = () => mkTex('concrete', 512, (x, s) => {
  x.fillStyle = '#c9cbcb'; x.fillRect(0, 0, s, s); noise(x, s, 0.2, '#9ea1a1', '#e6e8e8');
  for (let i = 0; i < 260; i++) {
    x.fillStyle = `rgba(${120 + Math.random() * 60},${120 + Math.random() * 60},${118 + Math.random() * 60},${Math.random() * 0.25})`;
    x.beginPath(); x.arc(Math.random() * s, Math.random() * s, Math.random() * 3.5, 0, 7); x.fill();
  }
}, true);

// Znak numeru regału: biała cyfra na niebieskim tle (jak magazynowy znak „30").
function signTex(text) {
  return mkTex(`sign:${text}`, 256, (x) => {
    x.fillStyle = '#1e50a0'; x.fillRect(0, 0, 256, 256);
    x.strokeStyle = '#ffffff'; x.lineWidth = 14; x.strokeRect(16, 16, 224, 224);
    x.fillStyle = '#ffffff'; x.textAlign = 'center'; x.textBaseline = 'middle';
    x.font = `bold ${String(text).length > 2 ? 120 : 150}px Arial, sans-serif`;
    x.fillText(String(text), 128, 140);
  }, true);
}
// Etykieta 3D (sprite) — tekstura z cache po tekście i kolorze.
const _lblCache = {};
function makeLabel(text, color) {
  const k = `${color}:${text}`;
  if (!_lblCache[k]) {
    const cv = document.createElement('canvas'); cv.width = 256; cv.height = 64;
    const ctx = cv.getContext('2d');
    ctx.fillStyle = 'rgba(15,23,42,0.75)'; ctx.fillRect(0, 0, 256, 64);
    ctx.fillStyle = color || '#fff'; ctx.font = 'bold 30px sans-serif';
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(String(text).slice(0, 18), 128, 32);
    _lblCache[k] = new THREE.CanvasTexture(cv);
  }
  const tex = _lblCache[k];
  const spr = new THREE.Sprite(new THREE.SpriteMaterial({ map: tex, transparent: true }));
  spr.scale.set(4, 1, 1);
  return spr;
}

const steelMat = (color, rough) => new THREE.MeshStandardMaterial({ color, roughness: rough, metalness: 0.82, roughnessMap: steelRough() });

/**
 * createViewer({canvas, wrap, labels, fill}) → { scene, camera, renderer, controls, requestRender,
 *   setData({floor, racks, features}, {frame}), highlight(keys), view('top'|'iso'|'sel'), resize() }
 *   labels: numery regałów i etykiety elementów (wyłącz przy bardzo dużych halach),
 *   fill: wskaźnik wypełnienia regału (widok modelu; w edytorze — brak danych, więc wyłączony).
 */
export function createViewer({ canvas, wrap, labels = true, fill = true }) {
  const debug = new URLSearchParams(location.search).has('debug3d');
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: debug });
  // 1.5 zamiast devicePixelRatio 2+: ostry obraz przy dużo mniejszym koszcie GPU na 4K/retina.
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
  renderer.setSize(wrap.clientWidth || 1, wrap.clientHeight || 1);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.12;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xd7dcdf);
  scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
  scene.fog = new THREE.Fog(0xd7dcdf, 60, 280);

  const camera = new THREE.PerspectiveCamera(42, (wrap.clientWidth || 1) / (wrap.clientHeight || 1), 0.05, 3000);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.08;
  controls.maxPolarAngle = Math.PI * 0.495;
  controls.minDistance = 1.5;

  scene.add(new THREE.HemisphereLight(0xffffff, 0x9aa0a4, 0.5));
  const key = new THREE.DirectionalLight(0xfff4e2, 2.0);
  key.castShadow = true;
  key.shadow.mapSize.set(1024, 1024);
  key.shadow.bias = -0.0006; key.shadow.normalBias = 0.02;
  scene.add(key, key.target);
  const fillLight = new THREE.DirectionalLight(0xcfe0ff, 0.4);
  scene.add(fillLight);

  const matUp = steelMat(0x2f4f86, 0.42), matBeam = steelMat(0xd9660f, 0.38), matBrace = steelMat(0x8f9499, 0.5);
  const floorMat = new THREE.MeshStandardMaterial({ map: concreteTex(), roughness: 0.88, metalness: 0.02, color: 0xe8eaea });
  // Zaznaczenie: cyjan — odróżnia się od pomarańczowych belek i niebieskich ram regałów.
  const hiMat = new THREE.MeshBasicMaterial({ color: 0x22d3ee, transparent: true, opacity: 0.32, depthWrite: false });
  const hiLine = new THREE.LineBasicMaterial({ color: 0x22d3ee });

  let content = new THREE.Group(), hiGroup = new THREE.Group(), disposables = [];
  let ext = extents([], { width: 50, depth: 30 }), boxes = new Map();   // _k → [Box3]
  scene.add(content, hiGroup);

  function placeLights() {
    const { x, z, cx, cz } = ext, rr = Math.max(x, z) * 0.85 + 6;
    key.position.set(cx + x * 0.3, Math.max(x, z) * 0.9 + 12, cz + z * 0.3);
    key.target.position.set(cx, 0, cz);
    Object.assign(key.shadow.camera, { left: -rr, right: rr, top: rr, bottom: -rr, near: 0.5, far: rr * 4 + 80 });
    key.shadow.camera.updateProjectionMatrix();
    fillLight.position.set(cx - x * 0.3, z * 0.4 + 6, cz - z * 0.3);
    // Mgła skalowana do hali (stałe 280 m zakrywało hale > ~200 m).
    scene.fog.near = Math.max(60, ext.diag * 0.4); scene.fog.far = Math.max(280, ext.diag * 2.2);
    controls.maxDistance = ext.diag * 3 + 60;
  }

  function track(obj) { disposables.push(obj); return obj; }

  const _p = new THREE.Vector3(), _s = new THREE.Vector3(1, 1, 1), _q = new THREE.Quaternion(), _up = new THREE.Vector3(0, 1, 0);

  // Stal liczy steelMatrices (scene-data.js); tu tylko znaki numerów, wskaźnik wypełnienia i obrys do podświetlenia.
  function buildRack(r) {
    const rackM = new THREE.Matrix4().compose(_p.set(r.x || 0, 0, r.y || 0),
      _q.setFromAxisAngle(_up, THREE.MathUtils.degToRad(r.angle || 0)), _s);
    const W = r.width, D = r.depth, H = Math.max(1, r.n_levels) * r.level_h, BW = W / Math.max(1, r.n_bays);
    if (r._k !== undefined) boxes.set(r._k, { m: rackM, w: W, h: H, d: D });
    if (!fill && !labels) return;
    const group = new THREE.Group();
    group.matrixAutoUpdate = false;
    group.matrix.copy(rackM);
    content.add(group);
    if (fill) {
      // Wskaźnik wypełnienia: 0–49 % zielony, 50–79 % żółty, ≥ 80 % czerwony; null → „brak danych”.
      const pct = typeof r.fill_pct === 'number' ? Math.max(0, Math.min(100, r.fill_pct)) : null;
      if (pct) {
        const fh = Math.max(0.06, H * pct / 100);
        const box = new THREE.Mesh(track(new THREE.BoxGeometry(Math.max(0.1, W - 0.12), fh, Math.max(0.1, D - 0.12))),
          track(new THREE.MeshBasicMaterial({ color: pct >= 80 ? 0xef4444 : pct >= 50 ? 0xf59e0b : 0x22c55e,
            transparent: true, opacity: 0.3, depthWrite: false })));
        box.position.set(W / 2, fh / 2, D / 2);
        group.add(box);
      }
      const spr = makeLabel(pct === null ? 'brak danych' : `${pct}%`, '#ffffff');
      track(spr.material);
      spr.scale.set(2.0, 0.5, 1); spr.position.set(W / 2, H + 0.5, D / 2);
      group.add(spr);
    }
    if (!labels) return;
    const signMat = track(new THREE.MeshBasicMaterial({ map: signTex(r.rack_id), toneMapped: false }));
    const s = Math.min(1.0, BW * 0.55), sy = Math.min(H - 0.55, H * 0.5 + 0.6);
    const plane = track(new THREE.PlaneGeometry(s, s));
    const front = new THREE.Mesh(plane, signMat); front.position.set(W / 2, sy, -0.16); front.rotation.y = Math.PI;
    const back = new THREE.Mesh(plane, signMat); back.position.set(W / 2, sy, D + 0.16);
    group.add(front, back);
  }

  function buildFeature(f) {
    const w = f.width, d = f.depth, col = new THREE.Color(f.color || '#6b7280');
    const group = new THREE.Group();
    group.position.set(f.x, 0, f.y);
    group.rotation.y = THREE.MathUtils.degToRad(f.angle || 0);
    content.add(group);
    let m;
    if (FLAT_KINDS.has(f.kind)) {
      m = new THREE.Mesh(track(new THREE.PlaneGeometry(w, d)),
        track(new THREE.MeshLambertMaterial({ color: col, transparent: true, opacity: 0.35, side: THREE.DoubleSide })));
      m.rotation.x = -Math.PI / 2; m.position.set(w / 2, 0.02, d / 2);
    } else {
      const h = f.height || (EDGE_KINDS.has(f.kind) ? 0.4 : 1.0);   // słup: wysokość hali
      m = new THREE.Mesh(_unitBox, track(new THREE.MeshLambertMaterial({ color: col, transparent: true, opacity: 0.85 })));
      m.scale.set(w, h, d); m.position.set(w / 2, h / 2, d / 2);
      m.castShadow = m.receiveShadow = true;
    }
    group.add(m);
    if (f._k !== undefined) {
      group.updateMatrixWorld(true);
      boxes.set(f._k, { m: group.matrixWorld.clone(), w, h: f.height || 1, d });
    }
    if (labels && f.kind !== 'column') {
      const lbl = makeLabel(f.label || f.kind_label || f.kind, '#e2e8f0');
      track(lbl.material);
      lbl.position.set(w / 2, FLAT_KINDS.has(f.kind) ? 1.2 : 1.8, d / 2);
      group.add(lbl);
    }
  }

  /** Przebudowa całej zawartości (regały, elementy, posadzka). Zwraca czas [ms]. */
  function setData({ floor, racks, features }, { frame = false } = {}) {
    const t0 = performance.now();
    scene.remove(content);
    disposables.forEach((d) => d.dispose());
    content.children.filter((c) => c.isInstancedMesh).forEach((c) => c.dispose());
    disposables = []; boxes = new Map();
    content = new THREE.Group();
    scene.add(content);
    ext = extents(racks, floor);
    const mode = steelMode(racks), batches = steelMatrices(racks, mode);
    racks.forEach(buildRack);
    [['up', matUp], ['beam', matBeam], ['brace', matBrace]].forEach(([k, mat]) => {
      if (!batches[k].length) return;
      const inst = new THREE.InstancedMesh(_unitBox, mat, batches[k].length / 16);
      inst.instanceMatrix.array.set(batches[k]);
      inst.instanceMatrix.needsUpdate = true;
      inst.computeBoundingSphere();
      inst.castShadow = inst.receiveShadow = mode === 'full';
      content.add(inst);
    });
    const SW = ext.x + SCENE_MARGIN * 2, SD = ext.z + SCENE_MARGIN * 2;
    floorMat.map.repeat.set(Math.max(4, SW / 6), Math.max(4, SD / 6));
    const floorMesh = new THREE.Mesh(track(new THREE.PlaneGeometry(SW, SD)), floorMat);
    floorMesh.rotation.x = -Math.PI / 2; floorMesh.position.set(ext.cx, 0, ext.cz); floorMesh.receiveShadow = true;
    content.add(floorMesh);
    features.forEach(buildFeature);
    placeLights();
    if (frame) view('iso');
    requestRender();
    return performance.now() - t0;
  }

  /** Podświetlenie zaznaczonych (klucze `_k` edytora): półprzezroczysta bryła + krawędzie. */
  let selKeys = [];
  function highlight(keys) {
    selKeys = keys;
    hiGroup.children.forEach((c) => c.geometry !== _unitBox && c.geometry.dispose());
    hiGroup.clear();
    const edges = new THREE.EdgesGeometry(_unitBox);
    for (const k of keys) {
      const b = boxes.get(k);
      if (!b) continue;
      const local = new THREE.Matrix4().compose(new THREE.Vector3(b.w / 2, b.h / 2, b.d / 2), new THREE.Quaternion(),
        new THREE.Vector3(b.w + 0.1, b.h + 0.1, b.d + 0.1)).premultiply(b.m);
      for (const o of [new THREE.Mesh(_unitBox, hiMat), new THREE.LineSegments(edges, hiLine)]) {
        o.matrixAutoUpdate = false; o.matrix.copy(local); hiGroup.add(o);
      }
    }
    requestRender();
  }

  function look(px, py, pz, tx, ty, tz) {
    camera.position.set(px, py, pz);
    controls.target.set(tx, ty, tz);
    controls.update();
    requestRender();
  }
  /** Ujęcia: 'top' z góry, 'iso' izometria całej hali, 'sel' przelot do zaznaczenia. */
  function view(kind) {
    const { cx, cz, diag } = ext;
    if (kind === 'top') return look(cx, diag * 1.1 + 10, cz + 0.01, cx, 0, cz);
    if (kind === 'sel' && selKeys.length) {
      const box = new THREE.Box3();
      hiGroup.children.forEach((o) => box.expandByObject(o));
      if (!box.isEmpty()) {
        const c = box.getCenter(new THREE.Vector3()), r = box.getSize(new THREE.Vector3()).length() + 6;
        return look(c.x + r * 0.6, c.y + r * 0.7, c.z + r * 0.9, c.x, c.y * 0.5, c.z);
      }
    }
    return look(cx + diag * 0.55, diag * 0.6 + 4, cz + diag * 0.95, cx, 2, cz);
  }

  // Render na żądanie (pętla 60 fps z cieniami trzymała GPU na 100 %). Damping dogrywa ruch,
  // bo controls.update() zwraca true, dopóki kamera się porusza. Karta w tle nie rysuje.
  let queued = false;
  function frameFn() {
    queued = false;
    if (document.hidden) return;
    const moving = controls.update();
    renderer.render(scene, camera);
    if (moving) requestRender();
  }
  function requestRender() {
    if (queued) return;
    queued = true;
    requestAnimationFrame(frameFn);
  }
  function resize() {
    const w = wrap.clientWidth, h = wrap.clientHeight;
    if (!w || !h) return;                      // panel ukryty albo bez layoutu — poczekaj na obserwatora
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
    requestRender();
  }
  controls.addEventListener('change', requestRender);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) requestRender(); });
  window.addEventListener('resize', resize);
  new ResizeObserver(resize).observe(wrap);     // przejście 0 → realny rozmiar dorysowuje 1. klatkę

  const api = { scene, camera, renderer, controls, requestRender, setData, highlight, view, resize,
    renderNow: () => { controls.update(); renderer.render(scene, camera); } };
  if (debug) window.__tw3d = api;              // diagnostyka: ?debug3d=1 (zachowany bufor do readPixels)
  return api;
}
