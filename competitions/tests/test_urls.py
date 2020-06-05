from django.test import Client
from django.test import TestCase
import json


class CompetitionUrlsTest (TestCase):

    def setUp(self):
        self.client = Client ()

    def test_save_athletes_200_success(self):
        data = {
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

        response = self.client.post (
            '/competitions/create',
            data = data,
            content_type="application/json"
        )

        self.assertEquals (200, response.status_code)

    def test_save_athletes_500_name_missing(self):
        data = {
            "competition_name": "",
            "club_name": "CLUB",
            "competition_end_date": "2020-10-10",
            "start_time": "09:00",
            "inscription_start_date": "2020-10-10",
            "inscription_end_date": "2020-10-10",
            "competition_start_date": "2020-10-10",
            "number_of_lanes": 6,
            "pool_meters": 25
        }

        response = self.client.post (
            '/competitions/create',
            data = data,
            content_type="application/json"
        )

        self.assertEquals (500, response.status_code)
