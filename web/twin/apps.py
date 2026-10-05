from django.apps import AppConfig


class TwinConfig(AppConfig):
    name = "twin"
    verbose_name = "Bliźniak magazynu"

    def ready(self):
        from . import signals  # noqa: F401 — rejestracja odbiorników (wersja modelu hali)
