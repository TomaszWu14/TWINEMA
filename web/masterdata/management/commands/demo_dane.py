from django.core.management.base import BaseCommand, CommandError

from masterdata.services import load_demo
from twin.models import WarehouseModel


class Command(BaseCommand):
    help = "Dane demonstracyjne: materiały + stan magazynu rozłożony po regałach modelu hali."

    def add_arguments(self, parser):
        parser.add_argument("--model", type=int, required=True, help="pk modelu hali (Modele hal)")
        parser.add_argument("--fill", type=float, default=0.7, help="udział zajętych miejsc 0–1")

    def handle(self, *args, model, fill, **opts):
        wm = WarehouseModel.objects.filter(pk=model).first()
        if wm is None:
            raise CommandError(f"Brak modelu hali {model}.")
        n_mat, log = load_demo(wm, fill=fill)
        self.stdout.write(f"Materiały: {n_mat}, stany: {log.rows_ok} pozycji w „{wm.name}”.")
