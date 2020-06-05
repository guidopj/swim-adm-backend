from django.test import Client
from django.test import TestCase
import datetime
import logging
logger = logging.getLogger(__name__)


class AthleteValidatorTest(TestCase):

    def setUp(self):
        competition_data = {
            "competition_name": "NEW COMP",
            "club_name": "CLUB",
            "competition_end_date": "2020-10-10",
            "start_time": "09:00",
            "inscription_start_date": "2020-10-10",
            "inscription_end_date": "2020-10-10",
            "competition_start_date": "2020-10-10",
            "number_of_lanes": 6,
            "pool_meters": 25
        }

        self.client.post (
            '/competitions/create',
            data = competition_data,
            content_type = "application/json"
        )

        team_data = {
            "team_name": "Team1",
            "team_name_abbr": "T1",
            "team_address": "address",
            "team_city": "city",
            "competition_name": "NEW COMP"
        }

        self.client.post (
            '/teams/create',
            data = team_data,
            content_type = "application/json"
        )

        self.client = Client ()

    def test_get_athletes_success(self):
        response = self.client.get('/athletes/')
        self.assertEquals(200, response.status_code)

    def test_get_athletes_404_not_found(self):
        response = self.client.get('/athletess/')
        self.assertEquals(404, response.status_code)

    # def test_save_athletes_500_name_missing(self):
    #     athlete_data = {
    #         "name": "",
    #         "dni": 123,
    #         "surname": "Geeks",
    #         "date_of_birth": datetime.date(2000,12,31),
    #         "genre": "Male",
    #         "team": "T1"
    #     },
    #     response = self.client.post(
    #         '/athletes/create',
    #         data= athlete_data,
    #         content_type = "application/json"
    #     )
    #
    #     self.assertEquals(500, response.status_code)
    #
    # def test_save_athletes_200_success(self):
    #     athlete_data = {
    #         "name": "dsa",
    #         "dni": 123,
    #         "surname": "Geeks",
    #         "date_of_birth": datetime.date(2000,12,31),
    #         "genre": "Male",
    #         "team": "T1"
    #     },
    #     response = self.client.post(
    #         '/athletes/create',
    #         data= athlete_data,
    #         content_type = "application/json"
    #     )
    #
    #     self.assertEquals(500, response.status_code)
