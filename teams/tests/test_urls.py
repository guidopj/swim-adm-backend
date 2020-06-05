from django.test import Client
from django.test import TestCase
from teams.models import Team
from competitions.models import Competition
import logging
logger = logging.getLogger(__name__)
import json
from django.forms.models import model_to_dict


class TeamUrlsTest(TestCase):

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

        response = self.client.post (
            '/competitions/create',
            data = competition_data,
            content_type = "application/json"
        )

        logger.error(response.status_code)

        self.client = Client ()

    def test_get_teams_success(self):
        response = self.client.get('/teams/')
        self.assertEquals(200, response.status_code)

    def test_get_teams_404_not_found(self):
        response = self.client.get('/teamss/')
        self.assertEquals(404, response.status_code)

    def test_save_team_500_name_abbr_missing(self):
        team_data = {
            "team_name": "Team1",
            "team_name_abbr": "",
            "team_address": "address",
            "team_city": "city",
            "competition_name": "NEW COMP"
        }

        response = self.client.post (
            '/teams/create',
            data = team_data,
            content_type = "application/json"
        )

        self.assertEquals(500, response.status_code)

    def test_save_team_200_success(self):
        team_data = {
            "team_name": "Team1",
            "team_name_abbr": "T1",
            "team_address": "address",
            "team_city": "city",
            "competition_name": "NEW COMP"
        }

        response = self.client.post (
            '/teams/create',
            data = json.dumps(team_data),
            content_type = "application/json"
        )

        self.assertEquals(200, response.status_code)
