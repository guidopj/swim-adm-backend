from django import forms
from .models import Athlete
from .validators.validator import validate_date_of_birth

class AthleteForm(forms.ModelForm):
    date_of_birth = forms.CharField(validators=[validate_date_of_birth])
    dni = forms.IntegerField()
    name = forms.CharField()
    surname = forms.CharField()
    genre = forms.CharField()
    team = forms.CharField()

    class Meta:
        model = Athlete
        fields = [
            'date_of_birth',
            'dni',
            'name',
            'surname',
            'genre',
            'team',
        ]
