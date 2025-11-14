from django.core.management.base import BaseCommand
from data_real_estate.models import Property

class Command(BaseCommand):
    help = "Supprime tous les biens immobiliers de la base de données."

    def handle(self, *args, **kwargs):
        count, _ = Property.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"✔ {count} biens supprimés avec succès !"))
