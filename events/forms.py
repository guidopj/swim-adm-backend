from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            'meters',
            'style',
            'category_from_age',
            'category_to_age',
            'genre',
            'competition_name',
        ]