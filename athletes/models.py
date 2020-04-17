from django.db import models

# Create your models here.

class Athlete(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    genre = models.CharField(max_length=10)
