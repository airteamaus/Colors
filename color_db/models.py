import struct
from django.db import models

class RGBColor(models.Model):
    index  = models.IntegerField(primary_key=True, unique=True)
    hex_string = models.CharField(max_length=8, unique=True)
    red    = models.IntegerField()
    green  = models.IntegerField()
    blue   = models.IntegerField()

    def store_rgb(self, rgb_tuple):
        """ rgb_tuple of the form (red, green, blue) """
        self.red, self.green, self.blue = rgb_tuple
        self.hex_string = struct.pack('BBB',*rgb_tuple).encode('hex')
        self.index = int(self.hex_string,16)
        self.save()

    def store_rgbint(self, rgbint):
        """ rgbint is an integer between 0-16777215 """
        blue  = rgbint & 255
        green = (rgbint >> 8) & 255
        red   = (rgbint >> 16) & 255
        return self.store_rgb((red,green,blue))

    def store_hex(self, hex_string):
        """ six chars eg: 0a0a0a """
        rgb_tuple = struct.unpack('BBB',hex_string.decode('hex'))
        return self.store_rgb(rgb_tuple)

class Resene(models.Model):
    name  = models.CharField(max_length=24)
    rgb   = models.ForeignKey(RGBColor)

class X11(models.Model):
    name  = models.CharField(max_length=24)
    rgb   = models.ForeignKey(RGBColor)

class NameThatColor(models.Model):
    name = models.CharField(max_length=24)
    rgb  = models.ForeignKey(RGBColor)

