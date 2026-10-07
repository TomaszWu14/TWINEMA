// Scena 3D hali (three.js) wspólna dla widoku modelu, podglądu w edytorze i animacji dnia.
// PBR: tekstury proceduralne (bez plików graficznych), IBL studyjny, ACES, cienie PCF.
// Stal i ładunek przez InstancedMesh (kilka draw calli niezależnie od liczby regałów — strażnik
// mesh-explosion w test_warehouse_model_view). Render na żądanie: klatka tylko po zmianie kamery/danych.
// Jakość „wysoka” (cienie, palety z ładunkiem) / „szybka” (bez nich) — wybór w localStorage.
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { COLOR_MODES, EDGE_KINDS, FLAT_KINDS, camAt, colorLegend, contactShadowPart, decorParts, depthRange, effectiveQuality, extents,
  hallWalls, isoView, localToWorld, outward, rackMatrices, rackOutline, rackTint, sitePlan, stackLayer, steelMatrices,
  steelMode, wallHidden } from './scene-data.js';
import { buildSite } from './scene-site.js';
import { makePost } from './scene-post.js';
import { asphaltTex, cartonTex, doorTex, hatchTex, LABEL_NEAR_M, makeLabel, panelTex, signTex, slabTex, slotTex,
  shadowTex, stdMat, steelMat, woodTex } from './scene-materials.js';

const YARD = 25;                                  // plac wokół hali [m]
const QKEY = 'tw3d.quality', CKEY = 'tw3d.colors';
// Ile koloru trybu przyjmuje ładunek palet: w trybie typów delikatnie (realizm), w pozostałych mocniej (czytelność z daleka).
const LOAD_TINT = { type: 0.22, zones: 0.5, fill: 0.55 };
const _unitBox = new THREE.BoxGeometry(1, 1, 1);
const _lw = new THREE.Vector3();
const _shadowPlane = new THREE.PlaneGeometry(1, 1).rotateX(-Math.PI / 2);
const HATCH = new Set(['fire_route', 'walkway', 'truckway']);

function readPref(k) { try { return localStorage.getItem(k); } catch { return null; } }
function savePref(k, v) { try { localStorage.setItem(k, v); } catch { /* tryb prywatny — tylko na tę sesję */ } }

/**
 * createViewer({canvas, wrap, labels, fill, decor}) → { scene, camera, renderer, controls, requestRender,
 *   setData({floor, racks, features}, {frame}), highlight(keys), view('top'|'iso'|'sel'), resize(),
 *   renderNow(), setDecor(on), setQuality('high'|'fast'), quality() }
 *   labels: numery regałów i etykiety elementów (wyłącz przy bardzo dużych halach),
 *   fill: wskaźnik wypełnienia regału (widok modelu), decor: palety z ładunkiem w regałach.
 */
export function createViewer({ canvas, wrap, labels = true, fill = true, decor = true }) {
  const debug = new URLSearchParams(location.search).has('debug3d');
  const renderer = new THREE.WebGLRenderer({ canvas, antialias: true, preserveDrawingBuffer: debug });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
  renderer.setSize(wrap.clientWidth || 1, wrap.clientHeight || 1);
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.outputColorSpace = THREE.SRGBColorSpace; renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.0;

  const scene = new THREE.Scene();
  scene.background = new THREE.Color(0xb7c0c7);
  scene.environment = new THREE.PMREMGenerator(renderer).fromScene(new RoomEnvironment(), 0.04).texture;
  scene.fog = new THREE.Fog(0xb7c0c7, 200, 900);

  const camera = new THREE.PerspectiveCamera(42, (wrap.clientWidth || 1) / (wrap.clientHeight || 1), 0.05, 4000);
  const controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true; controls.dampingFactor = 0.08;
  controls.maxPolarAngle = Math.PI * 0.495;
  controls.minDistance = 1.5;
  const post = makePost(renderer, scene, camera);   // AO tylko w jakości „wysokiej”

  scene.add(new THREE.HemisphereLight(0xf4f7fb, 0x7d8388, 0.5));
  const key = new THREE.DirectionalLight(0xfff1dc, 2.4);
  key.castShadow = true;
  key.shadow.bias = -0.0015; key.shadow.normalBias = 0.06;   // mniej → prążki („acne”) na posadzce dużej hali
  scene.add(key, key.target);
  const fillLight = new THREE.DirectionalLight(0xcfe0ff, 0.45);
  scene.add(fillLight);

  // Słupki grafitowe, kratownice ocynk; kolor trybu (typ / strefa / wypełnienie) niosą belki — instancje, bez przebudowy.
  const matUp = steelMat(0x3b4452, 0.42), matBeam = steelMat(0xffffff, 0.38), matBrace = steelMat(0x9aa0a6, 0.5);
  const matShadow = new THREE.MeshBasicMaterial({ color: 0x000000, map: shadowTex(), transparent: true, opacity: 0.38,
    depthWrite: false, polygonOffset: true, polygonOffsetFactor: -2 });
  const matOutline = new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 0.85 });
  const matWood = stdMat({ map: woodTex(), roughness: 0.9 });
  const matLoad = stdMat({ map: cartonTex(), roughness: 0.85 });
  const slabMat = stdMat({ map: slabTex(), roughness: 0.82, metalness: 0.02 });
  const yardMat = stdMat({ map: asphaltTex(), roughness: 0.95 });
  const wallMat = stdMat({ map: panelTex(), roughness: 0.6, metalness: 0.3, side: THREE.DoubleSide });
  const doorMat = stdMat({ map: doorTex(), roughness: 0.5, metalness: 0.5 });
  const darkMat = stdMat({ color: 0x24282c, roughness: 0.7 });
  const colMat = stdMat({ color: 0x9aa0a6, roughness: 0.7 });
  // Zaznaczenie: cyjan — odróżnia się od pomarańczowych belek, niebieskich ram i kartonów.
  const hiMat = new THREE.MeshBasicMaterial({ color: 0x22d3ee, transparent: true, opacity: 0.32, depthWrite: false });
  const hiLine = new THREE.LineBasicMaterial({ color: 0x22d3ee });

  let content = new THREE.Group(), hiGroup = new THREE.Group(), decorGroup = new THREE.Group(), disposables = [], nearLabels = [];
  let ext = extents([], { width: 50, depth: 30 }), boxes = new Map(), walls = [], last = null;
  let quality = 'high', decorOn = decor, colorMode = COLOR_MODES[readPref(CKEY)] ? readPref(CKEY) : 'type';
  let tinted = [], outline = null;                   // tinted: [InstancedMesh, właściciele instancji, rodzaj, kolory bazowe]
  scene.add(content, hiGroup);

  function track(obj) { disposables.push(obj); return obj; }

  function placeLights() {
    const { x, z, cx, cz } = ext, rr = Math.max(x, z) * 0.72 + 6;
    key.position.set(cx + x * 0.35, Math.max(x, z) * 0.8 + 20, cz + z * 0.45);
    key.target.position.set(cx, 0, cz);
    Object.assign(key.shadow.camera, { left: -rr, right: rr, top: rr, bottom: -rr, near: 0.5, far: rr * 4 + 120 });
    key.shadow.camera.updateProjectionMatrix();
    const ms = ext.diag > 120 ? 4096 : 2048;
    if (key.shadow.mapSize.x !== ms) { key.shadow.mapSize.set(ms, ms); key.shadow.map?.dispose(); key.shadow.map = null; }
    fillLight.position.set(cx - x * 0.3, z * 0.4 + 6, cz - z * 0.3);
    controls.maxDistance = ext.diag * 3 + 60;
  }

  const _p = new THREE.Vector3(), _s = new THREE.Vector3(1, 1, 1), _q = new THREE.Quaternion(), _up = new THREE.Vector3(0, 1, 0);

  function instanced(mat, arr, shadow) {
    const inst = new THREE.InstancedMesh(_unitBox, mat, arr.length / 16);
    inst.instanceMatrix.array.set(arr);
    inst.instanceMatrix.needsUpdate = true;
    inst.computeBoundingSphere();
    inst.castShadow = shadow; inst.receiveShadow = shadow;
    return inst;
  }

  // Stal i ładunek liczą funkcje czyste (scene-data.js); tu znaki numerów, wskaźnik wypełnienia, obrys.
  function buildRack(r) {
    const rackM = new THREE.Matrix4().compose(_p.set(r.x || 0, 0, r.y || 0),
      _q.setFromAxisAngle(_up, THREE.MathUtils.degToRad(r.angle || 0)), _s);
    const W = r.width, D = r.depth, H = Math.max(1, r.n_levels) * r.level_h, BW = W / Math.max(1, r.n_bays);
    if (r._k !== undefined) boxes.set(r._k, { m: rackM, w: W, h: H, d: D });
    const pct = typeof r.fill_pct === 'number' ? Math.max(0, Math.min(100, r.fill_pct)) : null;
    if (!(fill && pct !== null) && !labels) return;
    const group = new THREE.Group();
    group.matrixAutoUpdate = false;
    group.matrix.copy(rackM);
    content.add(group);
    if (fill && pct !== null) {                  // bez danych o stanie — bez etykiety (był szum „brak danych”)
      const spr = makeLabel(`${pct}%`, pct >= 80 ? '#fca5a5' : pct >= 50 ? '#fde68a' : '#bbf7d0');
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

  function buildDecor(racks) {
    decorGroup = new THREE.Group();
    const b = rackMatrices(racks, decorParts), shadow = quality === 'high';
    if (b.pbase) decorGroup.add(instanced(matWood, b.pbase, shadow));
    for (const k of ['pload', 'bin']) {
      if (!b[k]) continue;
      const inst = instanced(matLoad, b[k], shadow), base = new Float32Array(inst.count * 3);
      for (let i = 0; i < inst.count; i++) {   // lekka zmienność odcienia kartonów (i folii) na paletę
        const h = (Math.sin(i * 12.9898) * 43758.5453) % 1, v = Math.abs(h);
        base.set(v > 0.88 ? [0.92, 0.95, 1.0] : [0.86 + v * 0.14, 0.84 + v * 0.14, 0.8 + v * 0.12], i * 3);
      }
      tinted.push([inst, b._owner[k], 'load', base]);
      decorGroup.add(inst);
    }
    decorGroup.visible = decorOn;
    content.add(decorGroup);
  }

  // Cień kontaktowy pod regałem (miękka krawędź) „przykleja” bryły do posadzki bez post-processingu;
  // obrys brył = jedna geometria linii na całą halę, kolor trybu w atrybucie wierzchołków.
  function buildShadowsAndOutline(racks) {
    const s = instanced(matShadow, rackMatrices(racks, (r) => contactShadowPart(r)).shadow, false);
    s.geometry = _shadowPlane; s.renderOrder = 1;
    const pos = new Float32Array(racks.flatMap(rackOutline)), geo = track(new THREE.BufferGeometry());
    geo.setAttribute('position', new THREE.BufferAttribute(pos, 3));
    geo.setAttribute('color', new THREE.BufferAttribute(new Float32Array(pos.length), 3));
    outline = new THREE.LineSegments(geo, matOutline);
    content.add(s, outline);
  }

  function buildHall(floor, racks, site) {
    const plan = sitePlan(site);
    if (plan) buildSite(content, plan, { track, asphalt: yardMat.map });   // D1: teren działki zamiast placu
    else {
      const yard = new THREE.Mesh(track(new THREE.PlaneGeometry(ext.x + YARD * 2, ext.z + YARD * 2)), yardMat);
      yardMat.map.repeat.set((ext.x + YARD * 2) / 8, (ext.z + YARD * 2) / 8);
      yard.rotation.x = -Math.PI / 2; yard.position.set(ext.cx, -0.02, ext.cz); yard.receiveShadow = true;
      content.add(yard);
    }
    const slab = new THREE.Mesh(track(new THREE.PlaneGeometry(floor.width, floor.depth)), slabMat);
    slabMat.map.repeat.set(floor.width / 6, floor.depth / 6);
    slab.rotation.x = -Math.PI / 2; slab.position.set(floor.width / 2, 0, floor.depth / 2); slab.receiveShadow = true;
    content.add(slab);
    const rackH = racks.reduce((m, r) => Math.max(m, Math.max(1, r.n_levels) * r.level_h), 0);
    const h = Math.max(6, floor.clear_height ? floor.clear_height + 1.5 : rackH + 2.5);
    walls = hallWalls(floor).map((w) => {
      const len = Math.hypot(w.x1 - w.x0, w.z1 - w.z0);
      const m = new THREE.Mesh(_unitBox, wallMat);
      m.scale.set(len, h, 0.25);
      m.position.set((w.x0 + w.x1) / 2 + w.nx * 0.12, h / 2, (w.z0 + w.z1) / 2 + w.nz * 0.12);
      m.rotation.y = w.nx ? Math.PI / 2 : 0;
      m.castShadow = m.receiveShadow = true;
      content.add(m);
      return { w, m };
    });
    wallMat.map.repeat.set(Math.max(floor.width, floor.depth) / 8, 1);
  }

  function buildFeature(f, floor) {
    const w = f.width, d = f.depth, col = new THREE.Color(f.color || '#6b7280');
    const group = new THREE.Group();
    group.position.set(f.x, 0, f.y);
    group.rotation.y = THREE.MathUtils.degToRad(f.angle || 0);
    content.add(group);
    if (FLAT_KINDS.has(f.kind)) {
      const mat = HATCH.has(f.kind)
        ? track(new THREE.MeshStandardMaterial({ map: hatchTex(`#${col.getHexString()}`), transparent: true, roughness: 0.6 }))
        : f.kind === 'staging'
          ? track(new THREE.MeshStandardMaterial({ map: slotTex(), roughness: 0.8 }))
          : track(new THREE.MeshStandardMaterial({ color: col, transparent: true, opacity: 0.42, roughness: 0.6, depthWrite: false }));
      if (mat.map) {
        const tile = f.kind === 'staging' ? 1.4 : 1.2;
        mat.map = mat.map.clone(); mat.map.needsUpdate = true; mat.map.repeat.set(w / tile, d / tile); track(mat.map);
      }
      const m = new THREE.Mesh(track(new THREE.PlaneGeometry(w, d)), mat);
      m.rotation.x = -Math.PI / 2; m.position.set(w / 2, 0.02, d / 2); m.receiveShadow = true; stackLayer(m, f.kind);
      // Obwódka jak malowana linia na posadzce (pełny kolor).
      const edge = new THREE.LineSegments(track(new THREE.EdgesGeometry(track(new THREE.PlaneGeometry(w, d)))),
        track(new THREE.LineBasicMaterial({ color: col })));
      edge.rotation.x = -Math.PI / 2; edge.position.set(w / 2, 0.03, d / 2);
      group.add(m, edge);
    } else if (EDGE_KINDS.has(f.kind)) {
      // Dok/brama: płyta przeładunkowa w hali + brama segmentowa i odbojnice na najbliższej ścianie.
      const plate = new THREE.Mesh(_unitBox, darkMat);
      plate.scale.set(w, 0.06, d); plate.position.set(w / 2, 0.03, d / 2); plate.receiveShadow = true;
      group.add(plate);
      const [cxw, czw] = localToWorld(f, [w / 2, d / 2]), [nx, nz] = outward(cxw, czw, floor);
      const dw = f.kind === 'gate' ? Math.min(Math.max(w, d), 5.0) : 3.0, dh = f.kind === 'gate' ? 4.5 : 3.2;
      const wx = nx ? (nx > 0 ? floor.width : 0) : cxw, wz = nz ? (nz > 0 ? floor.depth : 0) : czw;
      const door = new THREE.Mesh(_unitBox, doorMat);
      // Po wewnętrznej stronie ściany (z zewnątrz i tak zasłania ją ściana, a przekrój pokazuje wnętrze).
      door.scale.set(dw, dh, 0.14); door.position.set(wx - nx * 0.12, dh / 2, wz - nz * 0.12);
      door.rotation.y = nx ? Math.PI / 2 : 0; door.castShadow = true;
      content.add(door);
      if (f.kind === 'dock') {
        for (const sgn of [-1, 1]) {
          const bump = new THREE.Mesh(_unitBox, darkMat);
          bump.scale.set(0.25, 0.5, 0.15);
          bump.position.set(wx - nx * 0.25 + (nz ? sgn * 1.7 : 0), 1.0, wz - nz * 0.25 + (nx ? sgn * 1.7 : 0));
          bump.rotation.y = door.rotation.y;
          content.add(bump);
        }
      }
    } else {
      const h = f.height || 1.0;                       // słup: wysokość hali
      const m = new THREE.Mesh(_unitBox, f.kind === 'column' ? colMat
        : track(stdMat({ color: col, roughness: 0.55 })));
      m.scale.set(w, h, d); m.position.set(w / 2, h / 2, d / 2);
      m.castShadow = m.receiveShadow = true;
      group.add(m);
    }
    if (f._k !== undefined) {
      group.updateMatrixWorld(true);
      boxes.set(f._k, { m: group.matrixWorld.clone(), w, h: f.height || 1, d });
    }
    if (labels && EDGE_KINDS.has(f.kind)) {
      // Dok/brama: tablica z numerem nad bramą (z obu stron ściany) zamiast pływającej etykiety —
      // doki co 4–5 m mają czytelne, nienachodzące na siebie oznaczenia jak w realnej hali.
      const [cxw, czw] = localToWorld(f, [w / 2, d / 2]), [nx, nz] = outward(cxw, czw, floor);
      const wx = nx ? (nx > 0 ? floor.width : 0) : cxw, wz = nz ? (nz > 0 ? floor.depth : 0) : czw;
      const text = String(f.label || f.kind_label || f.kind).replace(/\s*\([^)]*\)/g, '');
      const spr = makeLabel(text, '#ffffff', true), tex = spr.material.map, ratio = tex.image.width / tex.image.height;
      spr.material.dispose();
      const signMat = track(new THREE.MeshBasicMaterial({ map: tex, toneMapped: false }));
      const ph = 0.55, pw = Math.min(4.2, ph * ratio), plane = track(new THREE.PlaneGeometry(pw, ph));
      const top = (f.kind === 'gate' ? 4.5 : 3.2) + 0.55;
      for (const s of [1, -1]) {                      // na zewnątrz i do wewnątrz hali
        const m = new THREE.Mesh(plane, signMat);
        m.position.set(wx + nx * 0.16 * s, top, wz + nz * 0.16 * s);
        m.rotation.y = Math.atan2(nx * s, nz * s);
        content.add(m);
      }
    } else if (labels && f.kind !== 'column') {
      const lbl = makeLabel(f.label || f.kind_label || f.kind, '#e2e8f0', true);
      track(lbl.material);
      lbl.position.set(w / 2, FLAT_KINDS.has(f.kind) ? 1.2 : EDGE_KINDS.has(f.kind) ? 4.2 : 2.6, d / 2);
      group.add(lbl); nearLabels.push(lbl);
    }
  }

  /** Przebudowa całej zawartości (regały, ładunek, hala, elementy). Zwraca czas [ms]. */
  function setData(data, { frame = false } = {}) {
    const t0 = performance.now();
    last = data;
    const { floor, racks, features, site } = data;
    quality = effectiveQuality(readPref(QKEY), racks);
    scene.remove(content);
    disposables.forEach((x) => x.dispose());
    content.traverse((c) => { if (c.isInstancedMesh) c.dispose(); });
    disposables = []; boxes = new Map(); nearLabels = []; tinted = []; outline = null;
    content = new THREE.Group();
    scene.add(content);
    ext = extents(racks, floor);
    const mode = steelMode(racks), batches = steelMatrices(racks, mode), high = quality === 'high';
    racks.forEach(buildRack);
    [['up', matUp], ['beam', matBeam], ['brace', matBrace]].forEach(([k, mat]) => {
      if (!batches[k].length) return;
      const inst = instanced(mat, batches[k], high && mode !== 'xl');
      if (k === 'beam') tinted.push([inst, batches._owner.beam, 'steel']);
      content.add(inst);
    });
    if (racks.length) buildShadowsAndOutline(racks);
    if (high) buildDecor(racks);
    recolor();
    buildHall(floor, racks, site);
    features.forEach((f) => buildFeature(f, floor));
    key.castShadow = high;
    placeLights();
    if (frame) view('iso');
    requestRender();
    syncQualityButton();
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

  // Przelot kamery: płynne przejście (domyślnie 0,6 s; prezentacja wydłuża) — render na żądanie podtrzymuje klatki.
  let fly = null, flyMs = 600;
  function look(px, py, pz, tx, ty, tz, animate = false) {
    if (!animate) {
      camera.position.set(px, py, pz); controls.target.set(tx, ty, tz); controls.update(); requestRender(); return;
    }
    fly = { t0: performance.now(), a: pose(), b: { pos: [px, py, pz], target: [tx, ty, tz] } };
    requestRender();
  }
  /** Ujęcia: 'top' z góry, 'iso' izometria kadrowana do hali, 'sel' przelot do zaznaczenia. */
  function view(kind) {
    const { cx, cz } = ext;
    if (kind === 'top') {
      const v = isoView(ext, camera.fov, camera.aspect, 89, 0);
      return look(cx, v.dist, cz + 0.01, cx, 0, cz, true);
    }
    if (kind === 'sel' && selKeys.length) {
      const box = new THREE.Box3();
      hiGroup.children.forEach((o) => box.expandByObject(o));
      if (!box.isEmpty()) {
        const c = box.getCenter(new THREE.Vector3()), r = box.getSize(new THREE.Vector3()).length() + 6;
        return look(c.x + r * 0.6, c.y + r * 0.7, c.z + r * 0.9, c.x, c.y * 0.5, c.z, true);
      }
    }
    const v = isoView(ext, camera.fov, camera.aspect);
    return look(...v.pos, ...v.target, kind === 'iso' && last !== null && camera.position.lengthSq() > 0);
  }

  // Mgła i przekrój ścian zależne od kamery (mgła ze stałych metrów wypierała kolor przy dalekim ujęciu).
  function cameraDependent() {
    const d = camera.position.distanceTo(controls.target);
    scene.fog.near = d * 1.4 + 20; scene.fog.far = d * 4.5 + 200;
    // G2c: near ∝ odległość (bez z-fightingu warstw przy posadzce); obrysy wygaszane z daleka (aliasing 1-px linii)
    const z = depthRange(d, ext.diag);
    if (z.near !== camera.near || z.far !== camera.far) Object.assign(camera, z).updateProjectionMatrix();
    matOutline.opacity = Math.max(0.25, Math.min(0.85, 0.85 - (d - 120) / 600));
    for (const { w, m } of walls) m.visible = !wallHidden(w, camera.position.x, camera.position.z);
    for (const l of nearLabels) l.visible = camera.position.distanceTo(l.getWorldPosition(_lw)) < LABEL_NEAR_M;
  }

  // Render na żądanie (pętla 60 fps z cieniami trzymała GPU na 100 %). Damping dogrywa ruch.
  let queued = false;
  function frameFn() {
    queued = false;
    if (document.hidden) return;
    if (fly) {
      const k = Math.min(1, (performance.now() - fly.t0) / flyMs), c = camAt(fly.a, fly.b, k);
      camera.position.set(...c.pos); controls.target.set(...c.target);
      if (k >= 1) fly = null;
    }
    const moving = controls.update();
    cameraDependent();
    post.render(quality === 'high');
    if (moving || fly) requestRender();
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
    renderer.setSize(w, h); post.setSize(w, h);
    requestRender();
  }
  controls.addEventListener('change', requestRender);
  document.addEventListener('visibilitychange', () => { if (!document.hidden) requestRender(); });
  window.addEventListener('resize', resize);
  new ResizeObserver(resize).observe(wrap);     // przejście 0 → realny rozmiar dorysowuje 1. klatkę

  /** Kolor trybu na belkach, ładunku i obrysie — bez przebudowy geometrii (zmiana trybu = jedno przejście). */
  const _c = new THREE.Color(), _t = new THREE.Color();
  function recolor() {
    if (!last) return;
    const { racks, features } = last, tints = racks.map((r) => new THREE.Color(rackTint(r, colorMode, features)));
    const k = LOAD_TINT[colorMode];
    for (const [inst, owner, kind, base] of tinted) {
      for (let i = 0; i < inst.count; i++) {
        const t = tints[owner[i]];
        inst.setColorAt(i, kind === 'steel' ? t : _c.fromArray(base, i * 3).lerp(_t.copy(t), k));
      }
      inst.instanceColor.needsUpdate = true;
    }
    if (outline) {
      const col = outline.geometry.attributes.color;
      racks.forEach((r, i) => {
        _c.copy(tints[i]).multiplyScalar(0.75);
        for (let v = 0; v < 24; v++) col.setXYZ(i * 24 + v, _c.r, _c.g, _c.b);
      });
      col.needsUpdate = true;
    }
    renderLegend();
    requestRender();
  }

  // Nakładka w rogu sceny: legenda trybu, jakość i kolorowanie (dostępne z klawiatury, etykiety po polsku).
  const panel = document.createElement('div');
  panel.style.cssText = 'position:absolute;left:10px;bottom:10px;z-index:3;display:flex;flex-direction:column;gap:6px;'
    + 'align-items:flex-start;max-width:calc(100% - 20px)';
  const legend = document.createElement('ul');
  legend.setAttribute('aria-label', 'Legenda kolorów regałów');
  legend.style.cssText = 'list-style:none;margin:0;padding:6px 10px;border-radius:8px;background:rgba(15,23,42,.78);'
    + 'color:#e2e8f0;font:12px/1.5 system-ui,sans-serif;display:flex;flex-wrap:wrap;gap:4px 12px';
  legend.hidden = true;
  const row = Object.assign(document.createElement('div'), { style: 'display:flex;gap:6px;flex-wrap:wrap' });
  const cSel = document.createElement('select');
  cSel.className = 'form-control'; cSel.setAttribute('aria-label', 'Kolorowanie regałów');
  cSel.style.cssText = 'width:auto;padding:2px 8px;height:auto;font-size:13px';
  for (const [k, l] of Object.entries(COLOR_MODES)) cSel.add(new Option(`Kolory: ${l.toLowerCase()}`, k, false, k === colorMode));
  cSel.addEventListener('change', () => setColorMode(cSel.value));
  function renderLegend() {
    legend.replaceChildren(...colorLegend(last.racks, colorMode, last.features).map(([c, l]) => {
      const li = document.createElement('li'), sw = document.createElement('span');
      sw.style.cssText = `display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:6px;background:${c}`;
      li.append(sw, l);
      return li;
    }));
    legend.hidden = !last.racks.length;
  }
  function setColorMode(m) {
    colorMode = COLOR_MODES[m] ? m : 'type';
    savePref(CKEY, colorMode);
    cSel.value = colorMode;
    recolor();
  }

  // Przełącznik jakości (nakładka w rogu sceny): wysoka = cienie + palety z ładunkiem, szybka = bez nich.
  const qBtn = document.createElement('button');
  qBtn.type = 'button';
  qBtn.className = 'btn btn-secondary btn-sm';
  qBtn.title = 'Wysoka: cienie i palety z ładunkiem. Szybka: dla słabszych komputerów i bardzo dużych hal.';
  if (getComputedStyle(wrap).position === 'static') wrap.style.position = 'relative';
  row.append(qBtn, cSel);
  panel.append(legend, row);
  wrap.appendChild(panel);
  function syncQualityButton() {
    qBtn.textContent = `Jakość: ${quality === 'high' ? 'wysoka' : 'szybka'}`;
    qBtn.setAttribute('aria-pressed', String(quality === 'high'));
  }
  function setQuality(q) {
    savePref(QKEY, q);
    if (last) setData(last); else { quality = q; syncQualityButton(); }
  }
  qBtn.addEventListener('click', () => setQuality(quality === 'high' ? 'fast' : 'high'));
  syncQualityButton();

  function setDecor(on) {
    decorOn = on;
    decorGroup.visible = on;
    requestRender();
  }

  function pose() {
    return { pos: camera.position.toArray(), target: controls.target.toArray() };
  }

  const api = { scene, camera, renderer, controls, requestRender, setData, highlight, view, resize, setDecor, setColorMode,
    colorMode: () => colorMode,
    setQuality, quality: () => quality, look, pose, setFlyMs: (ms) => { flyMs = ms; },
    renderNow: () => { fly && (camera.position.set(...fly.b.pos), controls.target.set(...fly.b.target), fly = null);
      controls.update(); cameraDependent(); post.render(quality === 'high'); } };
  if (debug) window.__tw3d = api;              // diagnostyka: ?debug3d=1 (zachowany bufor do readPixels)
  return api;
}
