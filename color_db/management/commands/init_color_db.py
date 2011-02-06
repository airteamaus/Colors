from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from color_db.models import RGBColor

class Command(BaseCommand):
    args = '<no args>'
    help = 'Populate the color database'

    @transaction.commit_manually
    def handle(self, *args, **options):
        for index in range(1060000,16777216):
            color = RGBColor()
            color.store_rgbint(index)
            if index % 20000 == 0:
                transaction.commit()
        transaction.commit()

