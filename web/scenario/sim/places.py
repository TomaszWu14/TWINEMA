"""Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych (czysty Python).

Rola doku/bramy: jawne pole `dock_role` elementu hali (S3b); puste → zgadywana z etykiety
(`twin.layout.guess_dock_role`: „kontener”, „pacz…/kurier”, „wspóln”, „przyj/paletowy”, reszta → wydania).
Pole odkładcze: „przyj”/„IN” → przyjęć, „wyd”/„OUT” → wydań, bez opisu → połowa na każdą stronę.
Brak doków danej roli → zastępczo inne (hala bez doków kontenerowych dalej się liczy, ale z ostrzeżeniem).
"""

from twin.layout import guess_dock_role

ROLES = ("in_container", "in_pallet", "out", "courier")
ROLE_LABELS = {"in_container": "kontenerowego (przyjęcia kontenerów)", "in_pallet": "paletowego IN (auta)",
               "out": "wydań (auta OUT)", "courier": "kurierskiego (odbiór paczek)"}


def dock_role(f):
    return f.get("dock_role") or guess_dock_role(f.get("label"))


def needed_roles(day):
    """Role doków, których wymaga dzień scenariusza (format `ScenarioDay.sim_day`)."""
    need = set()
    for s in day.get("inbound", []):
        need.add("in_container" if s["kind"] == "container40" else "in_pallet")
    for s in day.get("outbound", []):
        need.add("courier" if s["kind"] == "courier" else "out")
    return need


def staging_side(label):
    s = f" {(label or '').lower()} "
    if "przyj" in s or " in " in s:
        return "in"
    if "wyd" in s or " out " in s:
        return "out"
    return None


def places_from_features(features, needed=None):
    """features: dicty jak `twin.shared.hall_feature_dict` (kind, label, dock_role, width, depth, id).
    needed: role wymagane przez scenariusz (`needed_roles`) — tylko ich brak daje ostrzeżenie; None = wszystkie."""
    docks, roles = [], {r: [] for r in ROLES}
    for i, f in enumerate(features):
        if f["kind"] not in ("dock", "gate"):
            continue
        did = f.get("id") or f"d{i + 1}"
        role = dock_role(f)
        docks.append({"id": did, "label": f.get("label") or "", "role": role})
        for r in (("in_container", "in_pallet", "out", "courier") if role == "shared" else (role,)):
            roles[r].append(did)
    warnings = []
    every = [d["id"] for d in docks]
    fallback = {"in_container": ("in_pallet",), "in_pallet": ("in_container",), "out": ("courier",),
                "courier": ("out",)}
    for r in ROLES:
        if not roles[r]:
            alt = [d for a in fallback[r] for d in roles[a]] or every
            if alt and (needed is None or r in needed):
                warnings.append(f"Brak doku {ROLE_LABELS[r]}, a scenariusz go potrzebuje — symulacja używa "
                                f"zastępczo innych doków. Ustaw rolę doku w edytorze lub w elementach hali.")
            roles[r] = alt
    if not every:
        docks = [{"id": "d0", "label": "Dok zastępczy", "role": "shared"}]
        roles = {r: ["d0"] for r in ROLES}
        warnings.append("Model hali nie ma doków — symulacja zakłada jeden dok zastępczy.")
    m2 = {"in": 0.0, "out": 0.0}
    for f in features:
        if f["kind"] != "staging":
            continue
        area = (f.get("width") or 0) * (f.get("depth") or 0)
        side = staging_side(f.get("label"))
        if side:
            m2[side] += area
        else:
            m2["in"] += area / 2
            m2["out"] += area / 2
    counts = {r: len(roles[r]) for r in ROLES}
    return {"docks": docks, "roles": roles, "counts": counts,
            "staging_m2": {k: round(v, 1) for k, v in m2.items()}, "warnings": warnings}


def with_extra_docks(places, role, k):
    """Kopia miejsc z k dodatkowymi dokami danej roli (do podpowiedzi „+N doków”)."""
    docks = list(places["docks"]) + [{"id": f"x-{role}-{i}", "label": "dodatkowy", "role": role} for i in range(k)]
    roles = {r: list(v) for r, v in places["roles"].items()}
    roles[role] += [f"x-{role}-{i}" for i in range(k)]
    return {**places, "docks": docks, "roles": roles, "counts": {r: len(v) for r, v in roles.items()}}
