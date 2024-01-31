from datetime import datetime

from django.db import models


class User(models.Model):
    phone_id = models.CharField(max_length=128)
    last_login = models.DateTimeField('last login date', blank=True, null=True)
    create_time = models.DateTimeField('date created', default=datetime.now)
    delete = models.BooleanField(default=False)

    def __str__(self):
        return self.phone_id


class POIVisit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poi_id = models.BigIntegerField()

    latitude = models.CharField(max_length=32, blank=False, null=False)
    longitude = models.CharField(max_length=32, blank=False, null=False)

    visit_count = models.IntegerField(blank=False)

    class Meta:
        unique_together = [['user', 'poi_id']]
        index_together = [['user', 'poi_id']]
