from django.db import models
import django_utils
# Create your models here.
class  Photo(models.Model):
    """
    A Flickr photo
    """
    id = models.IntegerField(primary_key=True, unique=True)
    uuid = django_utils.UUIDField(auto=True)
    title = models.CharField(max_length=128)
    description = models.TextField()
    owner = models.CharField(max_length=32)
    secret = models.CharField(max_length=32)
    farm = models.IntegerField()
    server = models.CharField(max_length=32)
    url_m = models.URLField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    imported = models.BooleanField(default=False)

    def get_web_url(self):
        """
        Gets the full web page ofr this photo
        http://www.flickr.com/photos/{user-id}/{photo-id}
        """
        return "http://www.flickr.com/photos/%s/%s" % (self.owner,self.id)

