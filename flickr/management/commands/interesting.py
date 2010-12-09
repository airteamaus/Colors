import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from Flickr.API import API
from BeautifulSoup import BeautifulSoup

from flickr.models import Photo

class Command(BaseCommand):
    args = '<no args>'
    help = 'Get latest interesting from flickr'

    def handle(self, *args, **options):
        api = API(settings.FLICKR_KEY, secret=None)
        json_result = api.execute_method(
                method='flickr.interestingness.getList',
                args={ 'format':'json',
                       'nojsoncallback':1,
                       'extras': 'url_m, geo, description'},
                sign=False)
        photo_list = json.load(json_result).get('photos')
        for photo in photo_list.get('photo'):

            desc = photo.get('description').get('_content')
            desc = ''.join(BeautifulSoup(desc).findAll(text=True))
            try:
                record, created = Photo.objects.get_or_create(
                    id = photo.get('id'),
                    title = photo.get('title'),
                    description = desc,
                    owner = photo.get('owner'),
                    secret = photo.get('secret'),
                    farm = photo.get('farm'),
                    server = photo.get('server'),
                    url_m = photo.get('url_m'),
                    latitude = photo.get('latitude'),
                    longitude = photo.get('longitude'),
                )
                if created:
                    print record.description
            except:
                pass
        print len(photo_list)

