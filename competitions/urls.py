from django.urls import path
from . import views

urlpatterns = [
    path('', views.getCompetitions, name="getCompetitions"),
    path('saveCompetition', views.saveCompetition, name="saveCompetition"),
    path('editCompetition', views.editCompetition, name="editCompetition"),
    path('deleteCompetition/<id>/', views.deleteCompetition, name="deleteCompetition"),
]