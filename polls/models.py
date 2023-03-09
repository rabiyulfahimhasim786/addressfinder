from django.db import models

# Create your models here.
class Mappin(models.Model):
    mapurl = models.TextField(blank=False, null=False)

class Mapsdata(models.Model):
    maplink = models.TextField(blank=False, null=False)
    mapaddress = models.TextField(blank=False, null=False)
    mapcity = models.TextField(blank=False, null=False)
    mapstate = models.TextField(blank=False, null=False)
    mapcountry = models.TextField(blank=False, null=False)
    mapzip = models.TextField(blank=False, null=False)
    


class Locationadress(models.Model):
    locationdata = models.TextField(blank=False, null=False)

class Locationdata(models.Model):
    locationlink = models.TextField(blank=False, null=False)
    addressdata = models.TextField(blank=False, null=False)

    

