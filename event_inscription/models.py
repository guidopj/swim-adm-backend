from django.db import models
from athletes.models import Athlete
from events.models import Event
from competitions.models import Competition

# Create your models here.

class EventInscription(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE)
    competition_name = models.ForeignKey(Competition, on_delete=models.CASCADE, db_column='competition_name', default=None)
    inscription_time = models.TimeField(blank=True, null=True)