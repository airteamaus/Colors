import json, urllib2, StringIO
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from django.conf import settings

from color_db.models import RGBColor
from flickr.models import Photo
from combos.models import Combo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Process any recently identified flickr images'

    def handle(self, *args, **options):
        photos = Photo.objects.filter(imported=False)
        for photo in photos:
            combo, created = Combo.objects.get_or_create(
                        reference=photo.uuid,
                        dataset = 2,
                        source = photo.get_web_url(),
            )
            if not photo.imported:
                try:
                    combo.save()
                    print photo.url_m
                    img = urllib2.urlopen(photo.url_m).read()
                    combo.set_colors_from_image(StringIO.StringIO(img))
                    photo.imported = True
                    photo.save()
                    combo.save()
                    if combo.colors.all().count() == 0: #lets not import shit
                        combo.delete()
                        photo.delete()
                except:
                    print 'photo %s had a problem' % photo
                    combo.delete()