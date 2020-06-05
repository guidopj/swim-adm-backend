from django.test import TestCase
from django.core.exceptions import ValidationError
from athletes.validators.validator import validate_date_of_birth
from datetime import datetime


class AthleteValidatorTest(TestCase):

    def setUp(self):
        self.date2 = datetime(2013, 12, 31)
        self.date3 = datetime(2014, 12, 31)


    def test_date_of_birth_validation_success(self):
        validate_date_of_birth(self.date2)

    def test_date_of_birth_validation_failure(self):
        with self.assertRaises(ValidationError):
            validate_date_of_birth(self.date3)