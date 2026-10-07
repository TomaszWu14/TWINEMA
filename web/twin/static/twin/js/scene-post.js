// Postprocessing sceny 3D: ambient occlusion (GTAO) — cień kontaktowy w stykach regał/posadzka, paleta/belka,
// bez którego obiekty „wiszą”. Tylko w jakości „wysokiej”; w „szybkiej” zwykły render (słabe GPU, wielkie hale).
// Bufor z MSAA (samples: 4) zastępuje antialias kanwy, który przy renderze do tekstury nie działa.
// Tone mapping i sRGB przejmuje OutputPass (czyta ustawienia renderera).
import * as THREE from 'three';
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { GTAOPass } from 'three/addons/postprocessing/GTAOPass.js';
import { OutputPass } from 'three/addons/postprocessing/OutputPass.js';

// Promień w metrach (widok): ~szerokość belki/odstęp palet; większy przyciemnia całe alejki.
export const AO = { radius: 2.0, distanceExponent: 1.0, thickness: 3.0, scale: 1.6, samples: 16 };

/** makePost(renderer, scene, camera) → { render(on), setSize(w, h) }; on=false → render bez efektów. */
export function makePost(renderer, scene, camera) {
  const size = renderer.getSize(new THREE.Vector2());
  const target = new THREE.WebGLRenderTarget(size.x, size.y, { type: THREE.HalfFloatType, samples: 4 });
  const composer = new EffectComposer(renderer, target);
  composer.setPixelRatio(renderer.getPixelRatio());
  composer.setSize(size.x, size.y);
  composer.addPass(new RenderPass(scene, camera));
  const gtao = new GTAOPass(scene, camera, size.x, size.y);
  gtao.updateGtaoMaterial(AO);
  composer.addPass(gtao);
  composer.addPass(new OutputPass());
  return {
    render(on) { if (on) composer.render(); else renderer.render(scene, camera); },
    setSize(w, h) { composer.setSize(w, h); },
  };
}
