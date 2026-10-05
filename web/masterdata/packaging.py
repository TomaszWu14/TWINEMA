"""Hierarchia opakowań sztuka → karton → paleta (czysty Python, bez Django).

Materiał to dict pól `Material` (cm, kg); nośnik to dict `Carrier`. Funkcje liczą paletę
z przeliczników, przypisują klasę wysokości/wagi i zwracają ostrzeżenia spójności —
ostrzeżenia nie blokują zapisu (dane z WMS bywają niepełne).
"""


def _vol(l, w, h):
    return l * w * h if l and w and h else None


def cartons_per_pallet(m):
    """Kartonów/warstwę × warstw/paletę, gdy oba znane; inaczej wartość wpisana."""
    if m.get("cartons_per_layer") and m.get("layers_per_pallet"):
        return m["cartons_per_layer"] * m["layers_per_pallet"]
    return m.get("cartons_per_pallet")


def pallet_height_cm(m, carrier=None):
    """Wpisana wysokość palety z towarem albo warstwy × wys. kartonu + wys. nośnika."""
    if m.get("pallet_h_cm"):
        return m["pallet_h_cm"]
    if m.get("layers_per_pallet") and m.get("carton_h_cm"):
        return round(m["layers_per_pallet"] * m["carton_h_cm"] + (carrier or {}).get("height_cm", 0), 1)
    return None


def pallet_weight_kg(m, carrier=None):
    cpp = cartons_per_pallet(m)
    if cpp and m.get("carton_kg"):
        return round(cpp * m["carton_kg"] + (carrier or {}).get("weight_kg", 0), 1)
    return None


def classify(value, classes):
    """Najmniejsza klasa z limitem ≥ wartość: classes = [(id, limit)]. Ponad największą → None."""
    if value is None:
        return None
    for cid, limit in sorted(classes, key=lambda c: c[1]):
        if value <= limit:
            return cid
    return None


def warnings(m, carrier=None):
    """Ostrzeżenia spójności danych materiału (lista zdań po polsku)."""
    out = []
    piece = _vol(m.get("piece_l_cm"), m.get("piece_w_cm"), m.get("piece_h_cm"))
    carton = _vol(m.get("carton_l_cm"), m.get("carton_w_cm"), m.get("carton_h_cm"))
    if piece and carton:
        if piece > carton:
            out.append("Sztuka jest większa niż karton.")
        elif m.get("pcs_per_carton") and piece * m["pcs_per_carton"] > carton * 1.02:
            out.append(f"{m['pcs_per_carton']} szt. nie mieści się w kartonie (objętościowo).")
    if m.get("piece_kg") and m.get("pcs_per_carton") and m.get("carton_kg") \
            and m["piece_kg"] * m["pcs_per_carton"] > m["carton_kg"] * 1.02:
        out.append("Sztuki ważą więcej niż cały karton.")
    if (m.get("cartons_per_layer") and m.get("layers_per_pallet") and m.get("cartons_per_pallet")
            and m["cartons_per_pallet"] != cartons_per_pallet(m)):
        out.append(f"Kartonów na palecie wpisano {m['cartons_per_pallet']}, "
                   f"a z warstw wychodzi {cartons_per_pallet(m)} — liczymy z warstw.")
    if carrier:
        if m.get("cartons_per_layer") and m.get("carton_l_cm") and m.get("carton_w_cm"):
            layer = m["cartons_per_layer"] * m["carton_l_cm"] * m["carton_w_cm"]
            if layer > carrier["length_cm"] * carrier["width_cm"] * 1.1:
                out.append(f"Warstwa kartonów jest większa niż nośnik {carrier['name']}.")
        h = pallet_height_cm(m, carrier)
        if h and carrier.get("max_load_h_cm") and h > carrier["max_load_h_cm"] + carrier.get("height_cm", 0):
            out.append(f"Paleta {h:g} cm przekracza max wysokość nośnika {carrier['name']}.")
        kg = pallet_weight_kg(m, carrier)
        if kg and carrier.get("max_load_kg") and kg > carrier["max_load_kg"] + carrier.get("weight_kg", 0):
            out.append(f"Paleta {kg:g} kg przekracza nośność nośnika {carrier['name']}.")
    return out


def weighted_cartons_per_pallet(rows):
    """[(kartonów/paletę, waga)] → średnia ważona (np. liczbą palet na stanie). None, gdy brak danych."""
    rows = [(c, w) for c, w in rows if c and w]
    total = sum(w for _, w in rows)
    return round(sum(c * w for c, w in rows) / total, 1) if total else None
