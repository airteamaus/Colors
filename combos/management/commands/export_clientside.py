from django.core.management.base import BaseCommand, CommandError
from combos.models import Combo, ClientSideColor, ClientSideCombo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Generate a new SQLite clientside.db'

    def handle(self, *args, **options):
        combos = Combo.objects.all()
        for combo in combos:
            csc = ClientSideCombo(reference = combo.reference)
            for color in combo.colors.all():
                new_color = ClientSideColor()
                new_color.store_rgbint(color.index)
                csc.colors.add(new_color)
            csc.save()
