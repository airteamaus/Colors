from django.core.management.base import BaseCommand, CommandError
from combos.models import Combo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Process any recently identified flickr images'

    def handle(self, *args, **options):
        combos = Combo.objects.all()
        for combo in combos:
            combo.save()
