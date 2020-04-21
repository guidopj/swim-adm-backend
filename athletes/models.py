from django.db import models
from teams.models import Team

# Create your models here.

class Athlete(models.Model):
    dni = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    genre = models.CharField(max_length=11)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
