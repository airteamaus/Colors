import Image
import scipy
import scipy.misc
import scipy.cluster
from django.db import models
from django.template.defaultfilters import slugify
import django_utils
from color_db.models import RGBColor


DATA_SETS = (
    (0, 'user_uploaded'),
    (1, 'flickr_pool_colorandcolors'),
    (2, 'flickr_interesting'),
)

DEPTH_CHOICES = (
    ('8bit', '256 colors'),
    ('24bit', '16.7m colors')
)

class Combo(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source  = models.CharField(max_length=64)
    reference = django_utils.UUIDField(auto=True)
    dataset = models.CharField(choices=DATA_SETS, max_length=64)
    colors  = models.ManyToManyField(RGBColor)
    depth   = models.CharField(choices=DEPTH_CHOICES, default='24bit', max_length=8)
    slug    = models.SlugField(blank=True)

    def set_colors_from_image(self, image, num_colors=12):
        NUM_CLUSTERS = num_colors
        im = Image.open(image)
        
        im = im.resize((150, 150))      # optional, to reduce time
        ar = scipy.misc.fromimage(im)
        shape = ar.shape
        ar = ar.reshape(scipy.product(shape[:2]), shape[2])

        color_list, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
        for r,g,b in color_list:
            color = RGBColor.objects.get(red=r, green=g, blue=b)
            self.colors.add(color)


    def save(self, *args, **kwargs):
        if not self.slug:
            try:
                from flickr.models import Photo
                title = Photo.objects.get(uuid=self.reference).title
                self.slug = slugify(title)
            except:
                pass
        super(Combo, self).save(*args, **kwargs)