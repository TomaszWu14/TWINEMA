"""Modele .glb (tools/blender/twinema_models.py → web/twin/static/twin/models/) w Blenderze — dla
twinema_warehouse_anim.py: te same wózki, ludzie i palety co w przeglądarce. Inny katalog: env TWINEMA_MODELS."""
import os

import bpy

HERE = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.environ.get("TWINEMA_MODELS") or os.path.join(HERE, "..", "..", "web", "twin", "static", "twin", "models")
_GLB = {}


def clear():
    _GLB.clear()


def glb(kind):
    """Model .glb → {"body": Mesh, "lift": Mesh | None} z wypaloną transformacją; brak pliku → None."""
    if kind not in _GLB:
        path, _GLB[kind] = os.path.join(MODELS_DIR, f"{kind}.glb"), None
        if os.path.isfile(path):
            before = set(bpy.data.objects)
            bpy.ops.import_scene.gltf(filepath=path)
            new = [ob for ob in bpy.data.objects if ob not in before]
            meshes = {}
            for ob in new:
                if ob.type == "MESH":
                    ob.data.transform(ob.matrix_world)
                    meshes[ob.name.split(".")[0]] = ob.data
            for ob in new:
                bpy.data.objects.remove(ob)
            if meshes.get("body"):
                _GLB[kind] = {"body": meshes["body"], "lift": meshes.get("lift")}
    return _GLB[kind]


def pallet_base():
    """Sam drewniany spód europalety (bez ładunku) — pod ładunek dowolnej wysokości."""
    g = glb("pallet")
    if not g:
        return None
    if "base" not in g:
        import bmesh
        me = g["body"].copy()
        bm = bmesh.new()
        bm.from_mesh(me)
        load = [i for i, m in enumerate(me.materials) if m and m.name.startswith("load")]
        bmesh.ops.delete(bm, geom=[f for f in bm.faces if f.material_index in load], context="FACES")
        bm.to_mesh(me)
        bm.free()
        g["base"] = me
    return g["base"]
