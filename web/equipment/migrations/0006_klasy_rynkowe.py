from django.db import migrations

# K2: klasy ogólne uzupełnione o typowe zakresy rynkowe (przegląd ofert wózków magazynowych): wyższe reach
# i VNA, cięższy czołowy, wózek podnośnikowy, wózki do kompletacji, ciągnik, AGV z masztem. Anonimowe,
# wartości przybliżone — konkretne modele użytkownik importuje jako własne (nazwy tylko w jego bazie).
CLASSES = [
    ("reach", "Reach truck 2,5 t / 14 m", 10, 11.5, 0.4, 0.5, 14, 2500, [[8, 2500], [11, 1800], [14, 1200]], 3.1,
     25, 25, 6, 2, 1.9, 2.7, 1.3, None),
    ("vna", "VNA kombi 1,6 t / 18 m", 9, 10, 0.4, 0.45, 18, 1600, [[12, 1600], [18, 1100]], 1.9, 35, 35, 8, 2,
     2.7, 4.2, 1.6, None),
    ("counterbalance", "Wózek czołowy 3,5 t / 7 m", 17, 18, 0.5, 0.55, 7, 3500, [[4.5, 3500], [7, 2600]], 4.2,
     20, 20, 6, 2, 2.4, 3.8, 1.3, None),
    ("stacker", "Wózek podnośnikowy 1,6 t / 6 m", 6, 6, 0.15, 0.2, 6, 1600, [[4.5, 1600], [6, 1200]], 2.4,
     20, 20, 6, 2, 1.6, 2.0, 0.85, None),
    ("order_picker", "Wózek do kompletacji poziomej 2,0 t", 12, 12, 0.05, 0.05, 0.2, 2000, [], 2.6, 15, 15, 8, 2,
     2.0, 3.0, 0.8, None),
    ("order_picker", "Wózek do kompletacji pionowej 1,2 t / 14 m", 9, 10, 0.35, 0.4, 14, 1200,
     [[10, 1200], [14, 1000]], 1.6, 30, 30, 8, 2, 2.4, 3.5, 1.4, None),
    ("tractor", "Ciągnik akumulatorowy 5 t", 14, 16, None, None, None, 5000, [], None, 15, 15, 8, 2,
     1.6, 1.9, 0.9, None),
    ("agv", "AGV paletowy z masztem 1,5 t / 6 m", 5, 6, 0.2, 0.25, 6, 1500, [[4, 1500], [6, 1200]], 2.8, 30, 30,
     8, 1, 1.7, 2.2, 1.0, None),
]
FIELDS = ["kind", "name", "speed_loaded_kmh", "speed_empty_kmh", "lift_speed_ms", "lower_speed_ms", "max_lift_m",
          "capacity_kg", "lift_curve", "aisle_m", "pick_s", "drop_s", "battery_h", "charge_h", "turn_radius_m",
          "length_m", "width_m", "throughput_h"]


def seed(apps, schema_editor):
    Equipment = apps.get_model("equipment", "Equipment")
    for row in CLASSES:
        Equipment.objects.get_or_create(name=row[1], is_system=True, defaults=dict(zip(FIELDS, row, strict=True)))


def unseed(apps, schema_editor):
    apps.get_model("equipment", "Equipment").objects.filter(is_system=True, name__in=[r[1] for r in CLASSES]).delete()


class Migration(migrations.Migration):
    dependencies = [("equipment", "0005_osprzet_producent")]
    operations = [migrations.RunPython(seed, unseed)]
