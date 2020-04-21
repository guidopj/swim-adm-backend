from django.urls import path
from . import views

urlpatterns = [
    path('create', views.saveTeam, name="saveTeam"),
    path('', views.getTeams, name="getTeams"),
]