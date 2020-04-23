from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['competition_name',
                  'club_name',
                  'competition_start_date',
                  'competition_end_date',
                  'start_time',
                  'inscription_start_date',
                  'inscription_end_date',
                  'number_of_lanes',
                  'pool_meters',
                  'teams'
                  ]