"""G2: elementy hali z kolorem równym dawnej palecie domyślnej (formularz zapisywał ją do bazy) → bez własnego
koloru, żeby szły za nową, spokojniejszą paletą HALL_FEATURE_COLORS. Własne kolory użytkownika zostają."""
from django.db import migrations

OLD_DEFAULTS = ["#64748b", "#0ea5e9", "#94a3b8", "#a855f7", "#f59e0b", "#f43f5e", "#22c55e", "#eab308", "#6b7280",
                "#dc2626", "#14b8a6", "#4ade80", "#facc15", "#38bdf8", "#ea580c", "#78716c", "#c026d3"]


def forwards(apps, schema_editor):
    Feature = apps.get_model("twin", "WarehouseHallFeature")
    Feature.objects.filter(color_hex__in=OLD_DEFAULTS + [c.upper() for c in OLD_DEFAULTS]).update(color_hex="")


class Migration(migrations.Migration):
    dependencies = [("twin", "0006_sprzet_z_katalogu")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
