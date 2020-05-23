from django.urls import path
from . import views

urlpatterns = [
    path('create', views.saveEvent, name="saveTeam"),
    path('', views.getEvents, name="getTeams"),
]