from django.test import TestCase
from athletes.models import Athlete
from django.utils import timezone
from teams.models import Team
from competitions.models import Competition
import datetime

class AthletesTest(TestCase):

    def setUp(self):
        self.competition = Competition.objects.create(
            competition_name="NEW COMP",
            club_name="CLUB",
            competition_end_date=datetime.date.today(),
            start_time=datetime.time(),
            inscription_start_date=timezone.now(),
            inscription_end_date=timezone.now(),
            competition_start_date=datetime.date.today(),
            number_of_lanes=6,
            pool_meters=25
        )
        self.team = Team.objects.create(
            team_name="Team1",
            team_name_abbr="T1",
            team_address="address",
            team_city="city",
        )

        self.team.competition_name.set([self.competition.competition_name])

    def athlete_creation(self):
        self.athlete = \
            Athlete.objects.create(dni=111,
                                   name="athlete name",
                                   surname="athlete surname",
                                   date_of_birth=timezone.now(),
                                   genre="Male",
                                   team=self.team)

    def test_athlete_creation(self):
        self.athlete_creation()
        self.assertTrue(isinstance(self.athlete, Athlete))
        self.assertEqual(self.athlete.name, "athlete name")