"""seed_demo: idempotencja, --reset tylko dla obiektów demo, konto `demo` w roli Podgląd."""
from io import StringIO

from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase, override_settings

from core.management.commands.seed_demo import demo_stock_name
from core.roles import GROUP_VIEWER
from masterdata.models import ImportLog, StockItem
from scenario.management.commands.demo_scenariusz import HALL
from scenario.models import Scenario
from twin.models import WarehouseModel


def seed(*args):
    call_command("seed_demo", *args, stdout=StringIO())


def counts():
    return (WarehouseModel.objects.count(), Scenario.objects.count(), ImportLog.objects.count(),
            StockItem.objects.count())


@override_settings(DEMO_PASSWORD="demo-haslo-123")
class SeedDemoTests(TestCase):
    def test_idempotent_and_creates_viewer_account(self):
        seed()
        first = counts()
        assert StockItem.objects.exists() and ImportLog.objects.filter(name=demo_stock_name()).count() == 1
        seed()
        self.assertEqual(counts(), first)
        demo = User.objects.get(username="demo")
        self.assertEqual(list(demo.groups.values_list("name", flat=True)), [GROUP_VIEWER])
        self.assertFalse(demo.is_staff or demo.is_superuser)
        self.assertTrue(demo.check_password("demo-haslo-123"))

    def test_reset_recreates_demo_objects_and_keeps_others(self):
        own = WarehouseModel.objects.create(name="Moja hala", floor_width_m=10, floor_depth_m=10, clear_height_m=8)
        seed()
        old_hall = WarehouseModel.objects.get(name=HALL).pk
        seed("--reset")
        self.assertTrue(WarehouseModel.objects.filter(pk=own.pk).exists())
        self.assertNotEqual(WarehouseModel.objects.get(name=HALL).pk, old_hall)
        self.assertEqual(ImportLog.objects.filter(name=demo_stock_name()).count(), 1)

    @override_settings(DEMO_PASSWORD="")
    def test_without_password_no_account(self):
        seed()
        self.assertFalse(User.objects.filter(username="demo").exists())
        self.assertTrue(WarehouseModel.objects.filter(name=HALL).exists())
