from django.core.exceptions import ValidationError

def validate_team_name_abbr(team_name_abbr):
    if len(team_name_abbr) > 10:
        raise ValidationError (
            '%d chars for abbr is too much. 10 Chars is the upper bound.' % len(team_name_abbr)
        )
    return team_name_abbr

