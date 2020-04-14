from django.db import models

# Create your models here.

class Competition(models.Model):
    club_name = models.CharField(max_length=200)
    start_time = models.TimeField()
    inscription_start_date = models.DateField()
    inscription_end_date= models.DateField()
