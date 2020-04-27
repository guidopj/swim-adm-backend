from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name',
                  'team_name_abbr',
                  'team_address',
                  'team_city',
                  'competition_name',
                  ]