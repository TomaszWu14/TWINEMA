from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand

from core.roles import ALL_GROUPS


class Command(BaseCommand):
    help = "Tworzy grupy ról (idempotentnie)."

    def handle(self, *args, **options):
        for name in ALL_GROUPS:
            _, created = Group.objects.get_or_create(name=name)
            self.stdout.write(f"{'+' if created else '='} {name}")
