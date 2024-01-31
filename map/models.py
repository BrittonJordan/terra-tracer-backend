from datetime import datetime

from django.db import models


# Create your models here.
class Location(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    time = models.DateTimeField('GPS collected time', default=datetime.now)

    longitude_precise = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    latitude_precise = models.DecimalField(max_digits=16, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=4)
    latitude = models.DecimalField(max_digits=8, decimal_places=4)
    create_time = models.DateTimeField('date created', default=datetime.now)
    delete = models.BooleanField(default=False)

# Moved to User.models
# class POIVisit(models.Model):
#     location = models.ForeignKey(Location, on_delete=models.CASCADE)
#     user = models.ForeignKey('user.User', on_delete=models.CASCADE)
#     POI_id_mapbox = models.CharField(max_length=128)
#     create_time = models.DateTimeField('date created', default=datetime.now)
#     delete = models.BooleanField(default=False)
