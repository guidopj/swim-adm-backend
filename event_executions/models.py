from django.db import models
from athletes.models import Athlete
from event_inscription.models import EventInscription

# Create your models here.

class EventExecution(models.Model):
    event_inscription = models.ForeignKey(EventInscription, on_delete=models.CASCADE, default="")
    heat = models.IntegerField()
    lane = models.IntegerField()
    final_time = models.TimeField()
    heat_position = models.IntegerField()
    general_position = models.IntegerField()