from django.db import migrations

# Kopia klas z equipment/catalog.py na dzień migracji (migracja nie importuje kodu aplikacji, żeby późniejsza
# zmiana katalogu nie zmieniała historii). Wartości przybliżone, syntetyczne — anonimowe klasy, bez producentów.
CLASSES = [
    ("pallet_truck", "Wózek paletowy elektryczny 2,0 t", 6, 6, 0.04, 0.05, 0.2, 2000, [], 2.2, 15, 15, 6, 2, 1.6, 1.8,
     0.72, None),
    ("counterbalance", "Wózek czołowy 2,5 t / 4,5 m", 16, 17, 0.45, 0.5, 4.5, 2500, [[3.5, 2500], [4.5, 2200]], 3.8,
     20, 20, 6, 2, 2.1, 3.4, 1.2, None),
    ("reach", "Reach truck 1,6 t / 10 m", 11, 12, 0.4, 0.5, 10, 1600, [[6, 1600], [8, 1400], [10, 1000]], 2.9,
     25, 25, 6, 2, 1.7, 2.5, 1.25, None),
    ("reach", "Reach truck 2,0 t / 12 m", 11, 12, 0.45, 0.5, 12.5, 2000, [[7, 2000], [10, 1600], [12.5, 1150]], 3.0,
     25, 25, 6, 2, 1.8, 2.6, 1.27, None),
    ("vna", "VNA kombi 1,5 t / 14 m", 9, 10, 0.4, 0.45, 14, 1500, [[10, 1500], [14, 1200]], 1.8, 35, 35, 8, 2,
     2.5, 3.8, 1.5, None),
    ("vna", "VNA kombi 1,2 t / 17 m", 9, 10, 0.4, 0.45, 17, 1200, [[12, 1200], [17, 1000]], 1.9, 35, 35, 8, 2,
     2.6, 4.0, 1.6, None),
    ("agv", "AGV paletowy 1,5 t", 5, 6, 0.1, 0.1, 0.2, 1500, [], 2.5, 30, 30, 8, 1, 1.5, 2.0, 1.0, None),
    ("amr", "AMR półkowy 600 kg", 5.4, 6.5, 0.05, 0.05, 0.1, 600, [], 1.5, 10, 10, 10, 1.5, 0.6, 1.0, 0.8, None),
    ("conveyor", "Przenośnik rolkowy (palety)", 0.72, 0.72, None, None, None, 1200, [], None, None, None, None, None,
     None, None, None, 120),
    ("sorter", "Sorter paczek", 7.2, 7.2, None, None, None, 50, [], None, None, None, None, None, None, None, None,
     4000),
]
FIELDS = ["kind", "name", "speed_loaded_kmh", "speed_empty_kmh", "lift_speed_ms", "lower_speed_ms", "max_lift_m",
          "capacity_kg", "lift_curve", "aisle_m", "pick_s", "drop_s", "battery_h", "charge_h", "turn_radius_m",
          "length_m", "width_m", "throughput_h"]


def seed(apps, schema_editor):
    Equipment = apps.get_model("equipment", "Equipment")
    for row in CLASSES:
        Equipment.objects.get_or_create(name=row[1], is_system=True, defaults=dict(zip(FIELDS, row, strict=True)))


class Migration(migrations.Migration):
    dependencies = [("equipment", "0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
