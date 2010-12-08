import re, json
import demjson
from django.core.management.base import BaseCommand, CommandError
from flickr.models import Photo

from BeautifulSoup import BeautifulSoup

class Command(BaseCommand):
    args = '<no args>'
    help = 'Process any recently identified flickr images'

    def handle(self, *args, **options):
        photos = Photo.objects.all()
        for photo in photos:
            desc = photo.description
            desc = ''.join(BeautifulSoup(desc).findAll(text=True))
            desc = desc.replace('u\'', '"').replace('\':', '":').replace('\'}', '"}').replace('u"', '"')

            try:
                desc = demjson.decode(desc)
                desc = desc.get('_content')
            except:
                desc = ''
            photo.description = desc
            #photo.save()
