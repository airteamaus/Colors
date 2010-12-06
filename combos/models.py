from django.db import models
import django_utils
from color_db.models import RGBColor
from combos import algorithms as algos

class Combo(models.Model):
    DATA_SETS = (
        (0, 'user_uploaded'),
        (1, 'flickr_pool_colorandcolors'),
        (2, 'flickr_interesting'),
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source  = models.CharField(max_length=64)
    reference = django_utils.UUIDField(auto=True)
    dataset = models.CharField(choices=DATA_SETS, max_length=64)
    depth   = models.IntegerField()
    colors  = models.ManyToManyField(RGBColor)

    def set_colors_from_image(self, image):
        color_list = algos.quant256(image)
        print color_list
        colors = RGBColor.objects.filter(index__in = color_list)
        for color in colors:
            self.colors.add(color)

