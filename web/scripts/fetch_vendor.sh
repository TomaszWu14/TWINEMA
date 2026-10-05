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
fetch "https://cdn.jsdelivr.net/npm/echarts@5.5.1/dist/echarts.min.js"                         "echarts.min.js"
echo "Vendor OK → $DIR"
