"""S1 — master data materiału: opakowania, nośniki, klasy, ABC, strefy specjalne, import i role."""
from unittest import TestCase as PureTestCase

from django.contrib.auth.models import Group, User
from django.test import TestCase
from django.urls import reverse

from core.roles import GROUP_DESIGNER, GROUP_VIEWER
from masterdata import packaging, services
from masterdata.demo import demo_materials
from masterdata.models import Carrier, ImportLog, Material, PalletClass

EUR = {"name": "EUR", "length_cm": 120, "width_cm": 80, "height_cm": 14.4, "weight_kg": 25,
       "max_load_h_cm": 180, "max_load_kg": 1000}


class PackagingTests(PureTestCase):
    def test_cartons_height_weight_from_layers(self):
        m = {"cartons_per_layer": 8, "layers_per_pallet": 5, "cartons_per_pallet": 99, "carton_h_cm": 25,
             "carton_kg": 10}
        self.assertEqual(packaging.cartons_per_pallet(m), 40)                   # warstwy wygrywają
        self.assertEqual(packaging.pallet_height_cm(m, EUR), 139.4)           # 5 × 25 + 14,4
        self.assertEqual(packaging.pallet_weight_kg(m, EUR), 425)             # 40 × 10 + 25
        self.assertEqual(packaging.cartons_per_pallet({"cartons_per_pallet": 30}), 30)
        self.assertEqual(packaging.pallet_height_cm({"pallet_h_cm": 120, "layers_per_pallet": 9}, EUR), 120)

    def test_classify_smallest_fitting_class(self):
        classes = [(3, 180), (1, 100), (2, 140)]
        self.assertEqual(packaging.classify(139.4, classes), 2)
        self.assertEqual(packaging.classify(100, classes), 1)
        self.assertIsNone(packaging.classify(181, classes))                    # ponad największą
        self.assertIsNone(packaging.classify(None, classes))

    def test_consistency_warnings(self):
        m = {"piece_l_cm": 50, "piece_w_cm": 50, "piece_h_cm": 50, "carton_l_cm": 40, "carton_w_cm": 30,
             "carton_h_cm": 30, "pcs_per_carton": 2, "cartons_per_layer": 20, "layers_per_pallet": 10,
             "cartons_per_pallet": 150, "carton_kg": 10}
        w = " ".join(packaging.warnings(m, EUR))
        self.assertIn("Sztuka jest większa niż karton", w)
        self.assertIn("z warstw wychodzi 200", w)
        self.assertIn("większa niż nośnik", w)                                 # 20 × 40 × 30 > 120 × 80
        self.assertIn("przekracza max wysokość", w)                           # 10 × 30 + 14,4 > 180 + 14,4
        self.assertIn("przekracza nośność", w)                                # 200 × 10 kg > 1000 kg
        ok = {"piece_l_cm": 10, "piece_w_cm": 10, "piece_h_cm": 10, "carton_l_cm": 40, "carton_w_cm": 30,
              "carton_h_cm": 30, "pcs_per_carton": 6, "cartons_per_layer": 8, "layers_per_pallet": 4,
              "carton_kg": 8}
        self.assertEqual(packaging.warnings(ok, EUR), [])

    def test_weighted_average(self):
        self.assertEqual(packaging.weighted_cartons_per_pallet([(40, 3), (20, 1), (None, 5)]), 35.0)
        self.assertIsNone(packaging.weighted_cartons_per_pallet([]))

    def test_demo_materials_are_consistent(self):
        rows = demo_materials(n=200)
        self.assertTrue(all(packaging.warnings(r, EUR) == [] for r in rows))
        self.assertTrue(any(r["adr"] for r in rows) and not any(r["adr"] and r["group"] != "Chemia gospodarcza"
                                                                 for r in rows))


class SeedAndImportTests(TestCase):
    def test_seed_default_carrier_and_classes(self):
        self.assertEqual(Carrier.objects.get(is_default=True).name, "EUR 120×80")
        self.assertEqual(list(PalletClass.objects.filter(kind="height").values_list("limit", flat=True)),
                         [100, 140, 180])

    def test_import_new_columns_resolves_refs_and_classifies(self):
        log = services.import_file("materials", "m.csv", (
            "Kod;Karton wys [cm];Karton waga [kg];Kartonów na warstwę;Warstw na palecie;Nośnik;Klasa wagi;ABC;ADR\n"
            "M1;25;10;8;5;przemysłowa 120×100;;b;tak\n"
            "M2;20;5;6;4;Paleta X;;;\n"
            "M3;20;5;6;4;;do 1000 kg;D;\n").encode("utf-8"))
        self.assertEqual((log.rows_ok, log.rows_rejected), (1, 2))
        reasons = " ".join(r["reason"] for r in log.rejects)
        self.assertIn("M2: nośnik: nie ma „Paleta X”", reasons)
        self.assertIn("klasa ABC", reasons)
        m = Material.objects.get(code="M1")
        self.assertEqual((m.carrier.name, m.abc_manual, m.adr), ("Przemysłowa 120×100", "B", True))
        self.assertEqual(m.height_class.label, "do 140 cm")                    # 5 × 25 + 14,4 = 139,4
        self.assertEqual(m.weight_class.label, "do 600 kg")                    # 40 × 10 + 30 = 430

    def test_reimport_only_changes_columns_in_file(self):
        services.import_file("materials", "a.csv", "Kod;ADR;Kartonów na palecie\nM1;x;40\n".encode())
        services.import_file("materials", "b.csv", "Kod;Nazwa\nM1;Rozpuszczalnik\n".encode())
        m = Material.objects.get(code="M1")
        self.assertEqual((m.name, m.adr, m.cartons_per_pallet), ("Rozpuszczalnik", True, 40))

    def test_cartons_per_pallet_hint_weighted_by_stock(self):
        self.assertIsNone(services.cartons_per_pallet_hint())
        Material.objects.create(code="A", cartons_per_layer=8, layers_per_pallet=5)   # 40
        Material.objects.create(code="B", cartons_per_pallet=20)
        self.assertEqual(services.cartons_per_pallet_hint(), (30.0, 2, "materiały"))
        services.import_file("stock", "s.csv", "Lokalizacja;Materiał\nL1;A\nL2;A\nL3;A\nL4;B\n".encode())
        self.assertEqual(services.cartons_per_pallet_hint(), (35.0, 2, "stan magazynu"))


class MasterDataViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.designer = User.objects.create_user("proj", password="x")
        cls.designer.groups.add(Group.objects.get_or_create(name=GROUP_DESIGNER)[0])
        cls.viewer = User.objects.create_user("widz", password="x")
        cls.viewer.groups.add(Group.objects.get_or_create(name=GROUP_VIEWER)[0])
        cls.m = Material.objects.create(code="M1", name="Klej", carton_h_cm=25, carton_kg=10,
                                        cartons_per_layer=8, layers_per_pallet=5, adr=True)

    def test_viewer_sees_only_aggregates(self):
        self.client.force_login(self.viewer)
        home = self.client.get(reverse("masterdata:home"))
        self.assertContains(home, "Strefy specjalne")
        self.assertNotContains(home, reverse("masterdata:materials"))
        for url in (reverse("masterdata:materials"), reverse("masterdata:material_edit", args=[self.m.pk]),
                    reverse("masterdata:catalog")):
            self.assertEqual(self.client.get(url).status_code, 403, url)
        log = ImportLog.objects.create(kind="materials", name="x")
        self.assertEqual(self.client.get(reverse("masterdata:log_detail", args=[log.pk])).status_code, 403)

    def test_filters_and_edit(self):
        self.client.force_login(self.designer)
        Material.objects.create(code="M2", name="Kubek")
        r = self.client.get(reverse("masterdata:materials"), {"flaga": "adr"})
        self.assertContains(r, "M1")
        self.assertNotContains(r, ">M2<")
        url = reverse("masterdata:material_edit", args=[self.m.pk])
        page = self.client.get(url)
        self.assertContains(page, "139,4 cm")
        data = {k: ("" if v is None else v) for k, v in page.context["form"].initial.items() if k != "id"}
        data.update(layers_per_pallet=6, abc_manual="A", adr="on", height_class="", weight_class="")
        data = {k: v for k, v in data.items() if v is not False}
        self.assertRedirects(self.client.post(url, data), url)
        self.m.refresh_from_db()
        self.assertEqual((self.m.layers_per_pallet, self.m.abc_manual, self.m.height_class.label),
                         (6, "A", "do 180 cm"))                                  # 6 × 25 + 14,4 = 164,4

    def test_scenario_shows_cartons_hint_next_to_norm(self):
        from scenario.models import Scenario

        sc = Scenario.objects.create(name="Rok bazowy")
        self.client.force_login(self.designer)
        r = self.client.get(reverse("scenario:detail", args=[sc.pk]))
        self.assertContains(r, "z master daty: 40 (1 materiałów, wg: materiały)")
        sc.refresh_from_db()
        self.assertEqual(sc.cartons_per_pallet, 40)                  # domyślna norma, nie nadpisana

    def test_catalog_keeps_single_default(self):
        self.client.force_login(self.designer)
        page = self.client.get(reverse("masterdata:catalog"))
        fs = page.context["carriers"]
        n = fs.initial_form_count()                                  # bez pustego wiersza „nowy nośnik”
        data = {"which": "carriers", "c-TOTAL_FORMS": n, "c-INITIAL_FORMS": n,
                "c-MIN_NUM_FORMS": 0, "c-MAX_NUM_FORMS": 1000}
        for i, f in enumerate(fs.forms[:n]):
            for name in f.fields:
                v = f.initial.get(name)
                if name == "id":
                    v = f.instance.pk or ""
                if name == "is_default":
                    v = "on" if (f.instance.pk and f.instance.name.startswith("Przem")) or v else None
                if v not in (None, False, ""):
                    data[f"c-{i}-{name}"] = v
        r = self.client.post(reverse("masterdata:catalog"), data, follow=True)
        self.assertContains(r, "Domyślny może być jeden")
        self.assertEqual(Carrier.objects.filter(is_default=True).count(), 1)
