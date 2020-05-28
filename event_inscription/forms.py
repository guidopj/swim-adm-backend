from django import forms
from .models import EventInscription

class EventInscriptionForm(forms.ModelForm):
    class Meta:
        model = EventInscription
        fields = [
            'event',
            'athlete',
            'inscription_time',
        ]