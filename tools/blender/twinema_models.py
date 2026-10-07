"""TWINEMA → modele 3D sprzętu, ludzi i palety (.glb) dla sceny w przeglądarce (G6).

Uruchomienie (bez GUI):
    blender -b --factory-startup -P tools/blender/twinema_models.py -- web/twin/static/twin/models [--preview DIR]

Konwencja jak w `web/twin/static/twin/js/equipment-models.js`: przód pojazdu = +X, Z w górę (w glTF Y w górę),
początek układu = środek pojazdu na posadzce — te same wymiary, więc `CARRY` (gdzie jedzie paleta) się zgadza.
Każdy model = dwa obiekty: `body` (stoi) i `lift` (wózek wideł / kabina — odtwarzacz podnosi go osobno).
Kolory = materiały o stałych nazwach; przeglądarka robi jedną siatkę instancyjną na materiał.
Kolory nadwozia z EQUIPMENT_COLORS (zmiana tam = zmiana tu).
"""
import math
import os
import sys

import bpy

PAINT = {"reach": 0xc9a227, "vna": 0x4f7cac, "ptruck": 0x5b8c5a, "counterbalance": 0xb5532f,
         "agv": 0x7a6aa8, "amr": 0x3a9ca0}
SWATCH = {"steel": (0x30353a, 0.45, 0.6), "rubber": (0x1f2329, 0.85, 0.0), "glass": (0x1e293b, 0.1, 0.3),
          "seat": (0x111827, 0.7, 0.0), "chrome": (0xb8bec4, 0.3, 0.9), "amber": (0xf59e0b, 0.4, 0.0),
          "mark": (0xe5e7eb, 0.5, 0.0), "sensor": (0x111827, 0.3, 0.2), "wood": (0xa87d4a, 0.85, 0.0),
          "load": (0xb4874f, 0.55, 0.0), "vest": (0xf97316, 0.6, 0.0), "trousers": (0x374151, 0.8, 0.0),
          "skin": (0xe0b48a, 0.7, 0.0), "helmet": (0xfacc15, 0.35, 0.0)}


def srgb(h):
    c = [((h >> s) & 255) / 255 for s in (16, 8, 0)]
    return [x / 12.92 if x <= 0.04045 else ((x + 0.055) / 1.055) ** 2.4 for x in c] + [1.0]


def mat(name, color=None):
    m = bpy.data.materials.get(name)
    if m:
        return m
    hexc, rough, metal = SWATCH.get(name, (color, 0.5, 0.15))
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = next(n for n in m.node_tree.nodes if n.type == "BSDF_PRINCIPLED")
    bsdf.inputs["Base Color"].default_value = srgb(hexc)
    bsdf.inputs["Roughness"].default_value = rough
    bsdf.inputs["Metallic"].default_value = metal
    m.diffuse_color = srgb(hexc)                                               # podgląd Workbench
    return m


class Model:
    """Zbiera bryły do grup body/lift; `done()` scala każdą grupę w jeden obiekt."""

    def __init__(self, name, paint=None):
        self.name, self.paint, self.parts = name, paint, {"body": [], "lift": []}

    def _add(self, ob, m, group):
        ob.data.materials.append(mat(m) if m != "paint" else mat(f"paint_{self.name}", self.paint))
        self.parts[group].append(ob)
        return ob

    def box(self, size, at, m="paint", bevel=0.02, group="body", rot_y=0.0):
        """size = (dł. X, szer. Y, wys. Z); at = (x, y, z dołu)."""
        bpy.ops.mesh.primitive_cube_add(size=1, location=(at[0], at[1], at[2] + size[2] / 2))
        ob = bpy.context.object
        ob.scale = size
        ob.rotation_euler[1] = rot_y
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        if bevel:
            mod = ob.modifiers.new("b", "BEVEL")
            mod.width, mod.segments, mod.limit_method = min(bevel, min(size) * 0.45), 2, "NONE"
        return self._add(ob, m, group)

    def cyl(self, r, depth, at, m="rubber", axis="Y", group="body", verts=16):
        bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=depth, location=at)
        ob = bpy.context.object
        ob.rotation_euler = {"X": (0, math.pi / 2, 0), "Y": (math.pi / 2, 0, 0), "Z": (0, 0, 0)}[axis]
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=False)
        mod = ob.modifiers.new("b", "BEVEL")
        mod.width, mod.segments, mod.limit_method = min(r, depth) * 0.25, 2, "ANGLE"
        return self._add(ob, m, group)

    def wheel(self, r, w, x, y, hub="steel"):
        self.cyl(r, w, (x, y, r), "rubber")
        self.cyl(r * 0.55, w + 0.01, (x, y, r), hub, verts=12)

    def pair(self, fn, y, *a, **k):
        """Para symetryczna względem osi pojazdu: to samo wywołanie box/cyl z at.y = ±y."""
        i = 1 if fn == self.box else 2                                         # pozycja `at` w argumentach
        for s in (1, -1):
            b = list(a)
            b[i] = (b[i][0], s * y, b[i][2])
            fn(*b, **k)

    def done(self):
        out = []
        for group, obs in self.parts.items():
            if not obs:
                continue
            for ob in obs:
                bpy.context.view_layer.objects.active = ob
                for mod in list(ob.modifiers):
                    bpy.ops.object.modifier_apply(modifier=mod.name)
            bpy.ops.object.select_all(action="DESELECT")
            for ob in obs:
                ob.select_set(True)
            bpy.context.view_layer.objects.active = obs[0]
            bpy.ops.object.join()
            ob = bpy.context.object
            ob.name = ob.data.name = group
            bpy.ops.object.shade_auto_smooth(angle=math.radians(35))
            out.append(ob)
        return out


def overhead_guard(m, x0, x1, z, half_w, post=0.06):
    """Dach ochronny: 4 słupki, rama i 4 poprzeczki."""
    for x in (x0, x1):
        m.pair(m.box, half_w, (post, post, z), (x, 0, 0.0), "steel", 0.015)
    L = x1 - x0
    m.pair(m.box, half_w, (L + post, post, post), ((x0 + x1) / 2, 0, z), "steel", 0.015)
    for k in range(4):
        m.box((0.05, 2 * half_w, 0.03), (x0 + L * (k + 0.5) / 4, 0, z + 0.02), "steel", 0.01)


def mast(m, x, height, half_w, group="body"):
    """Maszt: dwa ceowniki z poprzeczkami."""
    for s in (1, -1):
        m.box((0.12, 0.06, height), (x, s * half_w, 0.05), "steel", 0.015, group)
        m.box((0.05, 0.1, height), (x - 0.04, s * (half_w - 0.06), 0.05), "steel", 0.0, group)
    for z in (0.35, height * 0.55, height - 0.1):
        m.box((0.08, 2 * half_w, 0.1), (x, 0, z), "steel", 0.015, group)


def forks(m, x_plate, length=1.1, half_gap=0.25, z=0.08, backrest=0.9, width=0.95):
    """Płyta wózka wideł + krata oparcia + dwie zwężające się widły (grupa lift)."""
    m.box((0.06, width, 0.35), (x_plate, 0, z), "steel", 0.01, "lift")
    for k in range(5):
        m.box((0.03, 0.03, backrest), (x_plate, -width / 2 + 0.03 + k * (width - 0.06) / 4, z + 0.3), "steel", 0.0, "lift")
    m.box((0.04, width, 0.04), (x_plate, 0, z + 0.3 + backrest - 0.04), "steel", 0.0, "lift")
    for s in (1, -1):
        m.box((0.05, 0.12, 0.5), (x_plate + 0.05, s * half_gap, z), "steel", 0.01, "lift")
        m.box((length, 0.12, 0.05), (x_plate + 0.05 + length / 2, s * half_gap, z), "steel", 0.01, "lift")


def beacon(m, x, z):
    m.cyl(0.05, 0.08, (x, 0, z + 0.04), "amber", "Z", verts=12)


def reach():
    m = Model("reach", PAINT["reach"])
    m.box((1.3, 1.2, 1.0), (-0.75, 0, 0.15), bevel=0.12)                       # podwozie z napędem i baterią
    m.box((0.5, 0.9, 0.06), (-1.15, 0, 1.15), "seat", 0.02)                    # podest operatora (stojący)
    m.box((0.08, 0.5, 0.35), (-0.55, 0.3, 1.15), "seat", 0.02)                 # pulpit
    for s in (1, -1):
        m.box((1.3, 0.2, 0.22), (0.5, s * 0.5, 0.05), bevel=0.05)              # nogi podporowe
        m.wheel(0.1, 0.16, 1.05, s * 0.5)                                      # rolki nośne
    m.wheel(0.17, 0.2, -1.0, 0)                                                 # koło napędowe
    mast(m, 0.32, 4.6, 0.4)
    overhead_guard(m, -1.28, -0.2, 2.2, 0.5)
    beacon(m, -0.75, 2.25)
    forks(m, 0.45)
    return m


def vna():
    m = Model("vna", PAINT["vna"])
    m.box((0.9, 1.3, 1.25), (-1.35, 0, 0.12), bevel=0.1)                        # napęd + bateria
    m.box((1.4, 1.3, 0.3), (-0.25, 0, 0.12), bevel=0.06)
    for s in (1, -1):
        m.box((1.2, 0.2, 0.22), (1.0, s * 0.55, 0.05), bevel=0.05)
        m.wheel(0.1, 0.16, 1.45, s * 0.55)
        m.box((0.18, 0.12, 8.5), (-0.8, s * 0.5, 0.12), "steel", 0.02)         # maszt wysokiego składowania
    m.box((0.18, 1.1, 0.15), (-0.8, 0, 8.6), "steel", 0.02)
    m.wheel(0.2, 0.25, -1.45, 0)
    # kabina jedzie w górę razem z głowicą obrotową wideł
    m.box((1.0, 1.15, 1.1), (-0.2, 0, 0.42), bevel=0.08, group="lift")
    m.box((0.04, 1.0, 0.8), (0.31, 0, 0.6), "glass", 0.0, group="lift")
    m.box((1.1, 1.2, 0.08), (-0.2, 0, 2.45), "steel", 0.02, group="lift")
    for s in (1, -1):
        m.box((0.07, 0.07, 0.95), (0.27, s * 0.55, 1.52), "steel", 0.01, "lift")
        m.box((0.07, 0.07, 0.95), (-0.68, s * 0.55, 1.52), "steel", 0.01, "lift")
    m.box((0.35, 1.0, 0.9), (0.5, 0, 0.15), "steel", 0.04, group="lift")       # głowica obrotowa
    for s in (1, -1):
        m.box((1.1, 0.12, 0.06), (1.25, s * 0.22, 0.1), "steel", 0.01, "lift")
    return m


def ptruck():
    m = Model("ptruck", PAINT["ptruck"])
    m.box((0.6, 0.72, 0.8), (-0.05, 0, 0.08), bevel=0.1)                        # korpus napędu
    m.box((0.5, 0.6, 0.05), (-0.05, 0, 0.88), "seat", 0.02)
    m.box((0.1, 0.6, 0.5), (0.27, 0, 0.08), "steel", 0.02)                      # oparcie wideł
    for s in (1, -1):
        m.box((1.15, 0.17, 0.08), (0.88, s * 0.25, 0.06), "steel", 0.02)
        m.wheel(0.04, 0.12, 1.35, s * 0.25)
    m.wheel(0.12, 0.12, -0.05, 0)
    m.box((0.05, 0.05, 0.6), (-0.42, 0, 0.85), "steel", 0.01, rot_y=-0.35)     # dyszel
    m.box((0.12, 0.42, 0.1), (-0.55, 0, 1.38), "seat", 0.03)                    # rączka
    return m


def counterbalance():
    m = Model("counterbalance", PAINT["counterbalance"])
    m.box((1.5, 1.1, 0.75), (-0.45, 0, 0.25), bevel=0.1)                        # nadwozie
    m.box((0.45, 1.15, 1.0), (-1.3, 0, 0.2), bevel=0.2)                         # przeciwwaga (zaokrąglona)
    m.box((0.5, 0.5, 0.12), (-0.55, 0, 1.0), "seat", 0.04)                      # siedzisko
    m.box((0.12, 0.5, 0.5), (-0.8, 0, 1.05), "seat", 0.04)                      # oparcie
    m.box((0.08, 0.08, 0.45), (0.0, 0, 1.0), "steel", 0.02, rot_y=-0.4)        # kolumna kierownicy
    bpy.ops.mesh.primitive_torus_add(major_radius=0.16, minor_radius=0.02, major_segments=20, minor_segments=6,
                                     location=(-0.1, 0, 1.45), rotation=(0, -0.6, 0))
    m._add(bpy.context.object, "seat", "body")
    for s in (1, -1):
        m.wheel(0.3, 0.22, 0.0, s * 0.48)
        m.wheel(0.25, 0.2, -1.0, s * 0.48)
    overhead_guard(m, -1.05, 0.15, 2.25, 0.5)
    beacon(m, -0.95, 2.3)
    mast(m, 0.42, 3.2, 0.35)
    forks(m, 0.52)
    return m


def agv():
    m = Model("agv", PAINT["agv"])
    m.box((1.5, 0.95, 0.3), (0, 0, 0.03), bevel=0.06)
    for x in (0.78, -0.78):
        m.box((0.06, 0.95, 0.12), (x, 0, 0.08), "rubber", 0.02)                 # zderzaki
    m.box((0.03, 0.4, 0.08), (0.82, 0, 0.2), "sensor", 0.01)                    # skaner bezpieczeństwa
    m.cyl(0.04, 0.75, (0.7, 0.38, 0.33 + 0.375), "steel", "Z", verts=10)
    m.cyl(0.07, 0.1, (0.7, 0.38, 1.13), "sensor", "Z", verts=12)
    m.box((0.6, 0.02, 0.04), (0, 0.48, 0.2), "amber", 0.0)                       # pas świetlny
    for x in (0.55, -0.55):
        m.pair(m.cyl, 0.42, 0.09, 0.12, (x, 0, 0.09), "rubber")
    m.box((1.2, 0.85, 0.04), (0, 0, 0.33), "steel", 0.01, "lift")               # podnośnik
    return m


def amr():
    m = Model("amr", PAINT["amr"])
    m.box((1.0, 0.7, 0.22), (0, 0, 0.05), bevel=0.08)
    m.box((0.04, 0.5, 0.06), (0.5, 0, 0.12), "mark", 0.01)
    m.box((0.02, 0.3, 0.05), (0.51, 0, 0.18), "sensor", 0.01)
    m.pair(m.cyl, 0.36, 0.07, 0.06, (0, 0, 0.07), "rubber")
    m.box((0.95, 0.65, 0.03), (0, 0, 0.27), "steel", 0.01, "lift")
    m.box((0.18, 0.12, 0.02), (0.33, 0, 0.3), "mark", 0.0, "lift")
    return m


def person():
    m = Model("person")
    for s in (1, -1):
        m.cyl(0.075, 0.85, (0, s * 0.1, 0.425), "trousers", "Z", verts=10)     # nogi
        m.box((0.24, 0.1, 0.07), (0.04, s * 0.1, 0.0), "rubber", 0.02)          # buty
        m.cyl(0.05, 0.6, (0, s * 0.27, 1.12), "vest", "Z", verts=8)             # ręce
        m.cyl(0.045, 0.08, (0, s * 0.27, 0.78), "skin", "Z", verts=8)
    m.box((0.26, 0.46, 0.62), (0, 0, 0.83), "vest", 0.08)                       # tułów w kamizelce
    m.box((0.27, 0.47, 0.05), (0, 0, 1.12), "mark", 0.01)                       # pas odblaskowy
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=8, radius=0.12, location=(0, 0, 1.6))
    m._add(bpy.context.object, "skin", "body")
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=0.135, location=(0, 0, 1.64))
    helmet = bpy.context.object
    helmet.scale = (1.05, 1, 0.75)
    m._add(helmet, "helmet", "body")
    m.box((0.12, 0.26, 0.02), (0.12, 0, 1.62), "helmet", 0.0)                   # daszek
    return m


def pallet():
    """Europaleta 120×80 z ładunkiem w folii (wysokość jak PARTS.pallet: 0,144 + 1,1 m). Deski bez fazek —
    palet są na scenie setki (≈ 300 trójkątów na sztukę)."""
    m = Model("pallet")
    for y in (-0.35, 0, 0.35):
        m.box((1.2, 0.1, 0.022), (0, y, 0), "wood", 0)                      # deski dolne
        for x in (-0.5, 0, 0.5):
            m.box((0.145, 0.1, 0.078), (x, y, 0.022), "wood", 0)            # klocki
    for x in (-0.5, 0, 0.5):
        m.box((0.145, 0.8, 0.022), (x, 0, 0.1), "wood", 0)                  # deski poprzeczne
    for k in range(5):
        m.box((1.2, 0.1 if k % 2 else 0.145, 0.022), (0, -0.3275 + k * 0.16375, 0.122), "wood", 0)
    m.box((1.16, 0.76, 1.1), (0, 0, 0.144), "load", 0.04)
    return m


BUILDERS = {"reach": reach, "vna": vna, "ptruck": ptruck, "counterbalance": counterbalance, "agv": agv,
            "amr": amr, "person": person, "pallet": pallet}


def export(name, objs, out):
    bpy.ops.object.select_all(action="DESELECT")
    for ob in objs:
        ob.select_set(True)
    path = os.path.join(out, f"{name}.glb")
    bpy.ops.export_scene.gltf(filepath=path, use_selection=True, export_format="GLB", export_yup=True,
                              export_apply=True, export_normals=True, export_texcoords=False,
                              export_materials="EXPORT", export_extras=False, export_cameras=False,
                              export_lights=False, export_animations=False)
    tris = sum(sum(len(p.vertices) - 2 for p in ob.data.polygons) for ob in objs)
    print(f"{name}: {os.path.getsize(path) / 1024:.0f} kB, {tris} trójkątów")


def preview(objs, path):
    """Szybki podgląd (Workbench) — tylko do oceny kształtu."""
    sc = bpy.context.scene
    sc.render.engine = "BLENDER_WORKBENCH"
    sc.display.shading.color_type = "MATERIAL"
    sc.display.shading.light = "STUDIO"
    sc.display.shading.show_cavity = True
    sc.render.resolution_x, sc.render.resolution_y = 640, 480
    sc.render.filepath = path
    zs = [v[2] for ob in objs for v in ob.bound_box]
    h = max(zs)
    cam_data = bpy.data.cameras.new("c")
    cam = bpy.data.objects.new("c", cam_data)
    sc.collection.objects.link(cam)
    d = max(3.5, h * 1.6)
    cam.location = (d * 0.8, -d * 0.9, h * 0.6 + d * 0.35)
    target = bpy.data.objects.new("t", None)
    sc.collection.objects.link(target)
    target.location = (0, 0, h * 0.4)
    con = cam.constraints.new("TRACK_TO")
    con.target = target
    sc.camera = cam
    bpy.ops.render.render(write_still=True)
    bpy.data.objects.remove(cam)
    bpy.data.objects.remove(target)


def main():
    argv = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else []
    out = os.path.abspath(argv[0] if argv else "web/twin/static/twin/models")
    prev = argv[argv.index("--preview") + 1] if "--preview" in argv else None
    os.makedirs(out, exist_ok=True)
    for name, build in BUILDERS.items():
        bpy.ops.wm.read_factory_settings(use_empty=True)
        objs = build().done()
        export(name, objs, out)
        if prev:
            os.makedirs(prev, exist_ok=True)
            preview(objs, os.path.join(prev, f"{name}.png"))


main()
