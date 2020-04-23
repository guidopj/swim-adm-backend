from django.db import models
from athletes.models import Athlete
from events.models import Event

# Create your models here.

class EventExecution(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    heat = models.IntegerField()
    lane = models.IntegerField()
    inscription_time = models.DurationField()
    final_time = models.DurationField()
    heat_position = models.IntegerField()
    general_position = models.IntegerField()