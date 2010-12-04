import json

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from Flickr.API import API

class Command(BaseCommand):
    args = '<no args>'
    help = 'Get latest interesting from flickr'

    def handle(self, *args, **options):
        api = API(settings.FLICKR_KEY, secret=None)
        json_result = api.execute_method(
                method='flickr.interestingness.getList',
                args={'format':'json', 'nojsoncallback':1},
                sign=False)
        photo_list = json.load(json_result).get('photos')
        print photo_list

