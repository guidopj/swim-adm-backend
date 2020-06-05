from django.test import TestCase
from django.core.exceptions import ValidationError
from teams.validators.validator import validate_team_name_abbr

class AthleteValidatorTest(TestCase):

    def test_team_name_abbr_validation_success(self):
        validate_team_name_abbr("asdfghjklñ")

    def test_team_name_abbr_validation_failure(self):
        with self.assertRaises(ValidationError):
            validate_team_name_abbr("asdfghjklñq")