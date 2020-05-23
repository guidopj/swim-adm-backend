from django.db import models
from events.models import Event

class Record(models.Model):
    event = models.OneToOneField(
        Event,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    time = models.TimeField()

# Create your models here.
