"""Miejsca z layoutu hali dla symulacji: role doków i powierzchnia pól odkładczych (czysty Python).

Rolę doku/bramy czytamy z etykiety (generator i edytor nadają opisowe etykiety):
  „kontener” → rozładunek kontenerów · „pacz…”/„kurier” → odbiór paczek · „wspóln” → dok wspólny IN+OUT ·
  „przyj”/„paletowy”/„ IN” → przyjęcia palet · reszta (FTL, busy, „wyd”, „OUT”) → wydania.
Pole odkładcze: „przyj”/„IN” → przyjęć, „wyd”/„OUT” → wydań, bez opisu → połowa na każdą stronę.
Brak doków danej roli → zastępczo inne (hala bez doków kontenerowych dalej się liczy, ale z ostrzeżeniem).
"""

ROLES = ("in_container", "in_pallet", "out", "courier")


def dock_role(label):
    s = f" {(label or '').lower()} "
    if "wspóln" in s:
        return "shared"
    if "pacz" in s or "kurier" in s:
        return "courier"
    if "kontener" in s:
        return "in_container"
    if "przyj" in s or "paletowy" in s or " in " in s:
        return "in_pallet"
    return "out"


def staging_side(label):
    s = f" {(label or '').lower()} "
    if "przyj" in s or " in " in s:
        return "in"
    if "wyd" in s or " out " in s:
        return "out"
    return None


def places_from_features(features):
    """features: dicty jak `twin.shared.hall_feature_dict` (kind, label, width, depth, id)."""
    docks, roles = [], {r: [] for r in ROLES}
    for i, f in enumerate(features):
        if f["kind"] not in ("dock", "gate"):
            continue
        did = f.get("id") or f"d{i + 1}"
        role = dock_role(f.get("label"))
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
            if alt:
                warnings.append(f"Brak doków roli „{r}” — symulacja używa zastępczo innych doków.")
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
