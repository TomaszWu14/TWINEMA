"""Domyślny katalog: EUR 120×80 (domyślny), paleta przemysłowa 120×100, półpaleta 80×60
oraz klasy wysokości (do 100/140/180 cm) i wagi (do 300/600/1000 kg). Edytowalne w aplikacji."""
from django.db import migrations

CARRIERS = [
    # nazwa, dł, szer, wys, waga, max wys. ładunku, max waga ładunku, domyślny
    ("EUR 120×80", 120, 80, 14.4, 25, 180, 1000, True),
    ("Przemysłowa 120×100", 120, 100, 14.4, 30, 180, 1250, False),
    ("Półpaleta 80×60", 80, 60, 14.4, 10, 120, 500, False),
]
CLASSES = [("height", "do 100 cm", 100), ("height", "do 140 cm", 140), ("height", "do 180 cm", 180),
           ("weight", "do 300 kg", 300), ("weight", "do 600 kg", 600), ("weight", "do 1000 kg", 1000)]


def seed(apps, schema_editor):
    Carrier = apps.get_model("masterdata", "Carrier")
    PalletClass = apps.get_model("masterdata", "PalletClass")
    for name, l, w, h, kg, mh, mkg, default in CARRIERS:
        Carrier.objects.get_or_create(name=name, defaults=dict(
            length_cm=l, width_cm=w, height_cm=h, weight_kg=kg, max_load_h_cm=mh, max_load_kg=mkg,
            is_default=default))
    for kind, label, limit in CLASSES:
        PalletClass.objects.get_or_create(kind=kind, label=label, defaults={"limit": limit})


class Migration(migrations.Migration):
    dependencies = [("masterdata", "0002_opakowania_nosniki")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
