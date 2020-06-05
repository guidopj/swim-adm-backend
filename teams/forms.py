from django import forms
from .models import Team
from .validators.validator import validate_team_name_abbr

class TeamForm(forms.ModelForm):
    team_name = forms.CharField()
    team_name_abbr = forms.CharField(validators = [validate_team_name_abbr])
    team_address = forms.CharField ()
    team_city = forms.CharField ()
    competition_name = forms.CharField ()

    class Meta:
        model = Team
        fields = ['team_name',
                  'team_name_abbr',
                  'team_address',
                  'team_city',
                  'competition_name',
                  ]