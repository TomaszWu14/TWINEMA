from django.db import migrations

# Stawki domyślne (C1) — widełki syntetyczne, przybliżone, w zł netto; bez cenników konkretnych firm.
# (klucz, etykieta, jednostka, od, do)
RATES = [
    ("rack_reach", "Regał paletowy standard (reach) — miejsce paletowe", "zł/miejsce", 180, 320),
    ("rack_vna", "Regał VNA (z prowadzeniem) — miejsce paletowe", "zł/miejsce", 260, 450),
    ("rack_shelf", "Regał półkowy / kompletacji — miejsce", "zł/miejsce", 120, 250),
    ("dock", "Dok: rampa, brama, uszczelnienie", "zł/szt.", 60000, 110000),
    ("station", "Stanowisko (paletyzacja, pakowanie, kontrola)", "zł/szt.", 15000, 40000),
    ("building_m2", "Hala magazynowa (budynek)", "zł/m²", 2800, 4200),
    ("fleet_unit", "Wózek bez parametrów kosztu w katalogu — zakup", "zł/szt.", 150000, 350000),
    ("fleet_hour", "Wózek bez parametrów kosztu w katalogu — godzina pracy", "zł/h", 15, 35),
    ("labor_h", "Praca — stawka godzinowa z narzutami", "zł/h", 45, 70),
]
# koszty klas systemowych z katalogu: (nazwa klasy, zakup od, do, godzina od, do)
EQUIPMENT = [
    ("Wózek paletowy elektryczny 2,0 t", 25000, 45000, 3, 6),
    ("Wózek czołowy 2,5 t / 4,5 m", 90000, 160000, 12, 22),
    ("Reach truck 1,6 t / 10 m", 180000, 280000, 15, 25),
    ("Reach truck 2,0 t / 12 m", 220000, 320000, 16, 26),
    ("VNA kombi 1,5 t / 14 m", 450000, 700000, 25, 40),
    ("VNA kombi 1,2 t / 17 m", 550000, 850000, 28, 45),
    ("AGV paletowy 1,5 t", 250000, 420000, 10, 20),
    ("AMR półkowy 600 kg", 120000, 220000, 6, 12),
]


def seed(apps, schema_editor):
    CostRate = apps.get_model("equipment", "CostRate")
    for i, (key, label, unit, low, high) in enumerate(RATES):
        CostRate.objects.get_or_create(key=key, defaults={"label": label, "unit": unit, "low": low, "high": high,
                                                          "order": i})
    Equipment = apps.get_model("equipment", "Equipment")
    for name, pl, ph, hl, hh in EQUIPMENT:
        Equipment.objects.filter(name=name, is_system=True, cost_purchase__isnull=True).update(
            cost_purchase=pl, cost_purchase_max=ph, cost_per_hour=hl, cost_per_hour_max=hh)


class Migration(migrations.Migration):
    dependencies = [("equipment", "0003_koszty")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
