from django.core.management.base import BaseCommand, CommandError
from combos.models import Combo, ClientSideColor, ClientSideCombo, ClientSideColorCombo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Generate a new SQLite clientside.db'

    def handle(self, *args, **options):
        combos = Combo.objects.all()
        for combo in combos:
            csc = ClientSideCombo(reference = combo.reference)
            csc.save()
            for elt in combo.colors.all():
                color = ClientSideColor(hex_string=elt.hex_string)
                color.save()
                x = ClientSideColorCombo(color=color, combo=csc)
                x.save()
