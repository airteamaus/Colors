from django.db import models



class Color(models.Model):
    hex_string = models.CharField(max_length=8)
    rgb_red    = models.IntegerField()
    rgb_green  = models.IntegerField()
    rgb_blue   = models.IntegerField()
    rgb_int    = models.IntegerField()
    wavelength = models.IntegerField()
    
    def store_rgb(rgb_tuple):
        pass
    
    def store_rgbint(rgbint, depth=16777216):
        pass
        
    def store_hex(hex_string):
        pass

class Resene(models.Model):
    name  = models.CharField(max_length=24)
    color = models.ForeignKey(Color)
    
class X11(models.Model):
    name  = models.CharField(max_length=24)
    color = models.ForeignKey(Color)
    
class NameThaTColor(models.Model):
    name  = models.CharField(max_length=24)
    color = models.ForeignKey(Color)
    
class Palette(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    origin  = models.CharField(max_length=64)
    depth   = models.IntegerField()
    colors  = models.ManyToManyField()
