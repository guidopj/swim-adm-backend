from django.urls import path
from . import views

urlpatterns = [
    path('create', views.saveAthlete, name="saveAthlete"),
    path('', views.getAthletes, name="getAthletes"),
]