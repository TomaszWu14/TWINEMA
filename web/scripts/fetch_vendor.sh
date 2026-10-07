#!/bin/sh
# Biblioteki JS do static/twin/vendor — aplikacja nie zależy od CDN w runtime (CSP, awarie CDN).
# Odpalane w buildzie Dockera (przed collectstatic) i raz ręcznie lokalnie:  sh web/scripts/fetch_vendor.sh
# Sumy SHA-256 z oryginałów z CDN; niezgodność przerywa build. Nowa wersja = nowa suma:
#   curl -fsSL <url> | sha256sum
set -eu

DIR="$(dirname "$0")/../twin/static/twin/vendor"
mkdir -p "$DIR"
TJS=0.163.0

SUMS='
ca330dc6b8e6a0a88a0b707e40a5191110c3e86842c7c6431a7a7a2e972f08f5  three.module.js
f260591ef315aa04888152e7f121865214e33fb54727145cf4e4445058db1297  addons/controls/OrbitControls.js
e21f41b7ef2016f2984a5d27850b42dffa797a6a194a138e288b06576d765a7b  addons/environments/RoomEnvironment.js
e84270bd0cd5bdf60fefc26d00c2a391cb2e81f4d26a7a9ee16185a54773a3cf  echarts.min.js
d234e578618fa816955ebdc059c049c577e203e650e33cf22bde3f232c29e669  addons/postprocessing/EffectComposer.js
1c90c085312871c4bcdccfcf519499c6276dd503363fcf7cb7f703add45cf4a2  addons/postprocessing/RenderPass.js
b3c6128340eaa37e40a6a2f1b738e894c855239417d50959759b34a2b5e89f92  addons/postprocessing/Pass.js
3b28a1ee27e0eb96c0eab137a1f442ccf127a926904eced2d51e125ec44af781  addons/postprocessing/ShaderPass.js
328cf7db0da5d9be83ffe39d54b01d5ac1fddf108cc98182ddbb056f5c8b537f  addons/postprocessing/MaskPass.js
980b036767c439cf2aadd0e869b2e51b2ec00736a75a5ad1bb69dddb03254fe8  addons/postprocessing/GTAOPass.js
32f879d2179087676631c799857a885586b3cdd13b9731bd3b13f06428bd58b7  addons/postprocessing/OutputPass.js
4e3346db194db56a596cd074e9bdb39fb5eb52040c333e0d29dc4eb1324d3b1d  addons/shaders/CopyShader.js
94edb1040c7b5e859b17c2817782c8e895118a2d824ed162cab187aa32cc5a15  addons/shaders/GTAOShader.js
3dab419b23529f8fd59e2713458502f9f51d2dd3af3e1285dc671fcc451d49fb  addons/shaders/PoissonDenoiseShader.js
749b0c6db135541d1be183c8845a901af3a8bd45a013e84da0b1583c24b1ce4c  addons/shaders/OutputShader.js
9b8d541b77b0ddc79afaa6a1de8941452c191b8b9006f04e7b8fc422e2b263f7  addons/math/SimplexNoise.js
e85a5018a689867ae6ee60211956fa59ec5260d70d2cb58316f1ddc4afae637c  addons/loaders/GLTFLoader.js
b0c64fe6f3b9907262921b73fafc4ade874c07ba6b4876e164c87a830c2c2113  addons/utils/BufferGeometryUtils.js
'

fetch() {  # url  plik(może mieć podkatalogi)
  mkdir -p "$(dirname "$DIR/$2")"
  [ -f "$DIR/$2" ] && return 0
  curl -fsSL "$1" -o "$DIR/$2.part"
  sum=$(echo "$SUMS" | awk -v f="$2" '$2 == f {print $1}')
  if ! echo "$sum  $DIR/$2.part" | sha256sum -c - >/dev/null 2>&1; then
    echo "BŁĄD: suma SHA-256 nie zgadza się dla $2" >&2
    rm -f "$DIR/$2.part"; exit 1
  fi
  mv "$DIR/$2.part" "$DIR/$2"
}

fetch "https://cdn.jsdelivr.net/npm/three@${TJS}/build/three.module.js"                        "three.module.js"
fetch "https://cdn.jsdelivr.net/npm/three@${TJS}/examples/jsm/controls/OrbitControls.js"       "addons/controls/OrbitControls.js"
fetch "https://cdn.jsdelivr.net/npm/three@${TJS}/examples/jsm/environments/RoomEnvironment.js" "addons/environments/RoomEnvironment.js"
# RoomEnvironment importuje 'three' gołym specyfikatorem — działa z importmap, ale ścieżka względna jest pewniejsza.
sed -i.bak "s#} from 'three';#} from '../../three.module.js';#" "$DIR/addons/environments/RoomEnvironment.js" && rm -f "$DIR/addons/environments/RoomEnvironment.js.bak"
# Postprocessing (AO w scene-post.js) i GLTFLoader (modele .glb, equipment-glb.js) — importują 'three' gołym specyfikatorem; każda strona ze sceną ma importmap.
for f in postprocessing/EffectComposer.js postprocessing/RenderPass.js postprocessing/Pass.js postprocessing/ShaderPass.js postprocessing/MaskPass.js postprocessing/GTAOPass.js postprocessing/OutputPass.js shaders/CopyShader.js shaders/GTAOShader.js shaders/PoissonDenoiseShader.js shaders/OutputShader.js math/SimplexNoise.js loaders/GLTFLoader.js utils/BufferGeometryUtils.js; do
  fetch "https://cdn.jsdelivr.net/npm/three@${TJS}/examples/jsm/$f" "addons/$f"
done
fetch "https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"                         "echarts.min.js"
echo "Vendor OK → $DIR"
