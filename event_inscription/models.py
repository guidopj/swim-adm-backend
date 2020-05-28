from django.db import models
from athletes.models import Athlete
from events.models import Event

# Create your models here.

class EventInscription(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default="")
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, default="")
    inscription_time = models.TimeField(blank=True, null=True)