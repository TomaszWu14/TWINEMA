"""Wersja modelu hali = `WarehouseModel.updated_at`. Każdy zapis/usunięcie regału albo elementu hali ją podbija,
więc klucze cache wyników (symulacja EWM, porównanie wariantów, ślad animacji) nie podają starych liczb po edycji
w formularzach. bulk_create/bulk_update/update() sygnałów nie wysyłają — te ścieżki wołają `touch_model` same."""
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.utils import timezone

from .models import WarehouseHallFeature, WarehouseModel, WarehouseModelRack


def touch_model(model_id):
    WarehouseModel.objects.filter(pk=model_id).update(updated_at=timezone.now())


@receiver([post_save, post_delete], sender=WarehouseModelRack)
@receiver([post_save, post_delete], sender=WarehouseHallFeature)
def _bump_model_version(sender, instance, **kwargs):
    touch_model(instance.model_id)
