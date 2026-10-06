"""R3: brakujące dni (typowy/szczytowy) starych scenariuszy zakładane raz tutaj, a nie przy każdym GET widoku
scenariusza (dawne `ensure_days` w scenario_detail). Bez domyślnych strumieni — jak dotychczasowy GET."""
from django.db import migrations

KINDS = ("typical", "peak")


def forwards(apps, schema_editor):
    Scenario, Day = apps.get_model("scenario", "Scenario"), apps.get_model("scenario", "ScenarioDay")
    have = set(Day.objects.values_list("scenario_id", "kind"))
    Day.objects.bulk_create([Day(scenario_id=pk, kind=k) for pk in Scenario.objects.values_list("pk", flat=True)
                             for k in KINDS if (pk, k) not in have])


class Migration(migrations.Migration):
    dependencies = [("scenario", "0006_prezentacja_3d")]
    operations = [migrations.RunPython(forwards, migrations.RunPython.noop)]
