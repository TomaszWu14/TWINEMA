"""R2: liczby sztuk całe, godziny floty z wyniku symulacji (nie z % × bieżąca flota), rack_class, liczba zapytań."""
from unittest import TestCase as PlainTestCase

from django.contrib.auth.models import Group, User
from django.db import connection
from django.test import TestCase
from django.test.utils import CaptureQueriesContext
from django.urls import reverse

from core.roles import GROUP_DESIGNER
from scenario import services
from scenario.models import Scenario
from scenario.views_sim import kpi_num
from twin.blender_scene import rack_class
from twin.models import WarehouseModel


class FormatTests(PlainTestCase):
    def test_counts_whole_times_one_decimal(self):
        self.assertEqual(kpi_num(917.5, ""), "918")
        self.assertEqual(kpi_num(1.8, ""), "2")
        self.assertEqual(kpi_num(77.66, "min"), "77.7")
        self.assertEqual(kpi_num(24.0, "%"), "24")

    def test_rack_class_from_equipment_then_geometry(self):
        self.assertEqual(rack_class({"equipment": "shelf", "level_h": 2.0}), "shelf")
        self.assertEqual(rack_class({"equipment": "vna", "level_h": 1.8}), "vna")
        self.assertEqual(rack_class({"equipment": "reach", "level_h": 0.5}), "pallet")   # pole wygrywa z geometrią
        self.assertEqual(rack_class({"level_h": 0.5}), "shelf")                           # stare dane bez pola


class FleetHoursAndQueriesTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("proj", password="x")
        self.user.groups.add(Group.objects.create(name=GROUP_DESIGNER))
        self.client.force_login(self.user)
        self.client.post(reverse("scenario:create"), {"name": "Rok"})
        self.sc = Scenario.objects.get()
        self.wm = WarehouseModel.objects.create(name="Hala", floor_width_m=80, floor_depth_m=50)
        for i, role in enumerate(("in_container", "in_pallet", "out", "courier")):
            self.wm.features.create(kind="dock", label=f"Dok {i}", dock_role=role, x_m=0, y_m=5 * i, width_m=3.5,
                                    depth_m=4)
        self.wm.racks.create(zone="V", rack_id="001", n_bays=10, n_levels=4, bay_width_cm=270, depth_cm=110,
                             x_m=20, y_m=20)

    def test_costs_use_stored_fleet_hours_not_current_fleet(self):
        run = services.simulate(self.sc.days.get(kind="typical"), self.wm, runs=2, user=self.user)
        busy = run.result["agg"]["fleet_busy_h"]["mean"]
        before = services.run_costs(run)["opex"]["items"][1]["qty"]
        self.sc.fleet_units = self.sc.fleet_units * 3                    # zmiana floty PO symulacji
        self.sc.save()
        run.refresh_from_db()
        after = services.run_costs(run)["opex"]["items"][1]["qty"]
        self.assertEqual(before, after)
        self.assertAlmostEqual(after, round(busy * 260), delta=1)

    def test_detail_and_compare_query_count(self):
        a = services.simulate(self.sc.days.get(kind="typical"), self.wm, runs=2, user=self.user)
        b = services.simulate(self.sc.days.get(kind="peak"), self.wm, runs=2, user=self.user)
        for url in (reverse("scenario:detail", args=[self.sc.pk]),
                    reverse("scenario:compare") + f"?ids={a.pk}&ids={b.pk}"):
            with CaptureQueriesContext(connection) as q:
                self.assertEqual(self.client.get(url).status_code, 200)
            self.assertLess(len(q), 120, url)                             # próg: bez N+1 po regałach/przebiegach
