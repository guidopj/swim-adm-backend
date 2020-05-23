from django.urls import path
from . import views

urlpatterns = [
    path('create', views.saveInscriptions, name="saveInscriptions"),
]