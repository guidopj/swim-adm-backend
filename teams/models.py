from django.db import models
from competitions.models import Competition

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=201)
    team_name_abbr = models.CharField(max_length=11, primary_key=True)
    team_address = models.CharField(max_length=200)
    team_city = models.CharField(max_length=200)
    competition_name = models.ManyToManyField(Competition)