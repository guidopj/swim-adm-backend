from django.db import models
from competitions.models import Competition
#from records.modals import Record

# Create your models here.

class Event(models.Model):
    meters = models.IntegerField()
    style = models.CharField(max_length=50)
    category_from_age = models.IntegerField()
    category_to_age = models.IntegerField()
    genre = models.CharField(max_length=10)
    competition_name = models.ForeignKey(Competition, on_delete=models.CASCADE, db_column='competition_name')