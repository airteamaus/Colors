from django.core.management.base import BaseCommand, CommandError
from color_db.models import RGBColor

class Command(BaseCommand):
    args = '<no args>'
    help = 'Populate the color database'

    def handle(self, *args, **options):
        for index in range(0,16777216):
            color = RGBColor()
            color.store_rgbint(index)

