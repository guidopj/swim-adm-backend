from django.db import models
from django.utils import timezone

# Create your models here.

class Competition(models.Model):
    competition_name = models.CharField(max_length=200, default='New Competition')
    club_name = models.CharField(max_length=200)
    competition_start_date = models.DateField(default=timezone.localdate)
    competition_end_date = models.DateField(default=timezone.localdate)
    start_time = models.TimeField(default=timezone.localtime)
    inscription_start_date = models.DateTimeField(default=timezone.now)
    inscription_end_date= models.DateTimeField(default=timezone.now)
    number_of_lanes = models.IntegerField()
    pool_meters = models.IntegerField()
