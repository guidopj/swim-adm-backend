from django import forms
from .models import Athlete

class AthleteForm(forms.ModelForm):
    class Meta:
        model = Athlete
        fields = ['dni',
                  'name',
                  'surname',
                  'date_of_birth',
                  'genre',
                  'team'
                  ]