from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    club_name = forms.CharField()
    competition_start_date = forms.DateField()
    competition_end_date = forms.DateField()
    start_time = forms.TimeField()
    inscription_start_date = forms.DateTimeField()
    inscription_end_date = forms.DateTimeField()
    number_of_lanes = forms.IntegerField()
    pool_meters = forms.IntegerField()