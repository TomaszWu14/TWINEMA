// Tekstury proceduralne (bez plików graficznych), etykiety 3D i materiały sceny hali — wydzielone
// ze scene-builder.js (G2). Wszystko z cache: wiele przebudów sceny = te same tekstury.
import * as THREE from 'three';

// ── Tekstury proceduralne (współdzielone, cache) ─────────────────────────────────────────────
const _texCache = {};
function mkTex(key, size, draw, srgb = true) {
  if (_texCache[key]) return _texCache[key];
  const c = document.createElement('canvas'); c.width = c.height = size;
  draw(c.getContext('2d'), size);
  const t = new THREE.CanvasTexture(c);
  t.wrapS = t.wrapT = THREE.RepeatWrapping;
  if (srgb) t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 8;
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
const lines = (x, s, n, horiz, style, w) => {
  x.strokeStyle = style; x.lineWidth = w;
  for (let i = 1; i < n; i++) {
    const p = i * s / n; x.beginPath();
    if (horiz) { x.moveTo(0, p); x.lineTo(s, p); } else { x.moveTo(p, 0); x.lineTo(p, s); }
    x.stroke();
  }
};
const steelRough = () => mkTex('steelR', 128, (x, s) => { x.fillStyle = '#6e6e6e'; x.fillRect(0, 0, s, s); noise(x, s, 0.45, '#4a4a4a', '#a0a0a0'); }, false);
// Posadzka hali: beton + fugi dylatacyjne co 6 m (tekstura = 1 płyta 6 × 6 m).
export const slabTex = () => mkTex('slab', 512, (x, s) => {
  x.fillStyle = '#aeb2b2'; x.fillRect(0, 0, s, s); noise(x, s, 0.18, '#8e9292', '#cdd0d0');
  for (let i = 0; i < 200; i++) {
    x.fillStyle = `rgba(110,112,110,${Math.random() * 0.18})`;
    x.beginPath(); x.arc(Math.random() * s, Math.random() * s, Math.random() * 4, 0, 7); x.fill();
  }
  x.strokeStyle = 'rgba(80,82,82,0.35)'; x.lineWidth = 2; x.strokeRect(0, 0, s, s);
});
export const asphaltTex = () => mkTex('asphalt', 256, (x, s) => { x.fillStyle = '#5a5e62'; x.fillRect(0, 0, s, s); noise(x, s, 0.35, '#3e4246', '#7b8085'); });
// Karton z ładunkiem: 3 × 4 kartony w warstwach + taśma (jedna bryła udaje cały ładunek palety).
export const cartonTex = () => mkTex('carton', 256, (x, s) => {
  x.fillStyle = '#b4874f'; x.fillRect(0, 0, s, s); noise(x, s, 0.14, '#94683a', '#c99f68');
  for (let r = 0; r < 4; r++) { x.fillStyle = 'rgba(238,228,205,0.55)'; x.fillRect(0, r * s / 4 + s / 8 - 5, s, 10); }
  lines(x, s, 4, true, 'rgba(85,55,25,0.6)', 3); lines(x, s, 3, false, 'rgba(85,55,25,0.45)', 3);
});
export const woodTex = () => mkTex('wood', 128, (x, s) => {
  x.fillStyle = '#3d2f22'; x.fillRect(0, 0, s, s);
  for (let i = 0; i < 5; i++) { x.fillStyle = i % 2 ? '#b58a55' : '#a87d4a'; x.fillRect(2, i * s / 5 + 3, s - 4, s / 5 - 6); }
  noise(x, s, 0.18, '#7a5a35', '#d0a670');
});
export const panelTex = () => mkTex('panel', 256, (x, s) => {   // płyta warstwowa ściany: pionowe przetłoczenia
  x.fillStyle = '#d9dde1'; x.fillRect(0, 0, s, s); noise(x, s, 0.06, '#c3c8cd', '#eef0f2');
  lines(x, s, 8, false, 'rgba(120,128,136,0.55)', 2);
});
export const doorTex = () => mkTex('door', 128, (x, s) => {     // brama segmentowa: poziome panele
  x.fillStyle = '#9aa3ab'; x.fillRect(0, 0, s, s); lines(x, s, 6, true, 'rgba(50,55,60,0.7)', 3);
});
// Pole odkładcze: posadzka z malowaną siatką miejsc paletowych (tekstura = 1 miejsce 1,4 × 1,4 m).
export const slotTex = () => mkTex('slot', 128, (x, s) => {
  x.fillStyle = '#b9bdbd'; x.fillRect(0, 0, s, s); noise(x, s, 0.12, '#9ea2a2', '#cfd2d2');
  x.strokeStyle = '#e2b007'; x.lineWidth = 6; x.strokeRect(3, 3, s - 6, s - 6);
});
export const hatchTex = (color) => mkTex(`hatch:${color}`, 128, (x, s) => {
  x.clearRect(0, 0, s, s); x.fillStyle = color;
  for (let i = -s; i < s * 2; i += 32) { x.beginPath(); x.moveTo(i, 0); x.lineTo(i + 16, 0); x.lineTo(i + 16 - s, s); x.lineTo(i - s, s); x.fill(); }
});

// Cień kontaktowy: prostokąt z miękką krawędzią (alfa) — mnożony przez czarny materiał pod regałem.
export const shadowTex = () => mkTex('cshadow', 64, (x, s) => {
  const img = x.createImageData(s, s), edge = (t) => Math.min(1, Math.min(t, 1 - t) / 0.28);
  for (let j = 0; j < s; j++) {
    for (let i = 0; i < s; i++) {
      const a = edge((i + 0.5) / s) * edge((j + 0.5) / s);
      img.data[(j * s + i) * 4 + 3] = Math.round(255 * a * a);
    }
  }
  x.putImageData(img, 0, 0);
}, false);

// Znak numeru regału: biała cyfra na niebieskim tle (jak magazynowy znak „30").
export function signTex(text) {
  return mkTex(`sign:${text}`, 256, (x) => {
    x.fillStyle = '#1e50a0'; x.fillRect(0, 0, 256, 256);
    x.strokeStyle = '#ffffff'; x.lineWidth = 14; x.strokeRect(16, 16, 224, 224);
    x.fillStyle = '#ffffff'; x.textAlign = 'center'; x.textBaseline = 'middle';
    x.font = `bold ${String(text).length > 2 ? 120 : 150}px Arial, sans-serif`;
    x.fillText(String(text), 128, 140);
  });
}
// Etykieta 3D (sprite) — tekstura z cache po tekście i kolorze. `screen`: stały rozmiar na ekranie
// (etykiety elementów hali — czytelny tekst; widoczne tylko z bliska, LABEL_NEAR_M).
const _lblCache = {};
const LABEL_SCREEN_H = 0.024;                    // ułamek wysokości ekranu
export const LABEL_NEAR_M = 55;                         // etykiety elementów tylko z bliska (z daleka nachodzą na siebie)
export function makeLabel(text, color, screen = false) {
  const t = String(text).slice(0, screen ? 28 : 18), k = `${color}:${screen}:${t}`;
  if (!_lblCache[k]) {
    const cv = document.createElement('canvas'), ctx = cv.getContext('2d');
    const font = screen ? 'bold 40px sans-serif' : 'bold 30px sans-serif';
    ctx.font = font;
    cv.width = screen ? Math.ceil(ctx.measureText(t).width) + 40 : 256; cv.height = screen ? 64 : 64;
    ctx.fillStyle = 'rgba(15,23,42,0.82)'; ctx.fillRect(0, 0, cv.width, cv.height);
    ctx.fillStyle = color || '#fff'; ctx.font = font;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(t, cv.width / 2, 33);
    _lblCache[k] = new THREE.CanvasTexture(cv);
    _lblCache[k].colorSpace = THREE.SRGBColorSpace;
  }
  const img = _lblCache[k].image;
  const spr = new THREE.Sprite(new THREE.SpriteMaterial({ map: _lblCache[k], transparent: true, toneMapped: false,
    sizeAttenuation: !screen }));
  if (screen) spr.scale.set(LABEL_SCREEN_H * img.width / img.height, LABEL_SCREEN_H, 1);
  else spr.scale.set(4, 1, 1);
  return spr;
}

export const steelMat = (color, rough) => new THREE.MeshStandardMaterial({ color, roughness: rough, metalness: 0.82, roughnessMap: steelRough() });
export const stdMat = (o) => new THREE.MeshStandardMaterial({ roughness: 0.8, metalness: 0.05, ...o });
