from .models import Competition
from django.core import serializers
from django.http import JsonResponse
from .forms import CompetitionForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
logger = logging.getLogger(__name__)
from events.models import Event
from django.core.serializers import serialize
from teams.models import Team
from athletes.models import Athlete
from django.http import HttpResponse

# Create your views here.

def getCompetitions(request):
    qs = Competition.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)

def getCompetitionDetails(request, competition_name):
    events = Event.objects.filter(competition_name=competition_name).values()
    teams = Team.objects.filter(competition_name=competition_name)
    athletesList = []
    for team in teams:
        athletes = Athlete.objects.filter(team=team)
        athletesList = athletesList + list(athletes.values())
    eventsSerialized = serializers.serialize("json", events)
    teamsSerialized = serializers.serialize("json", teams)
    return JsonResponse({'events': eventsSerialized, 'teams': teamsSerialized, 'athletes': athletesList}, safe=False)

@csrf_exempt
def saveCompetition(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        logger.error(received_json_data)
        form = CompetitionForm(received_json_data)
        if form.is_valid():
            competition = form.save(commit=False)
            competition.save()
            return HttpResponse(status=200)
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context), status=500)
    else:
        return HttpResponse(status=405)

def deleteCompetition(request, competitionId):
   comp = Competition.objects.get(id = competitionId)
   comp.delete()
   return HttpResponse(status=200)

def editCompetition(request):
    if request.method == "PUT":
        form = CompetitionForm(request.PUT)
        if form.is_valid():
            competitionId= form.cleaned_data['id']
            comp = Competition.objects.get(id=competitionId)
            comp.club_name = request.PUT.get('club_name')
            comp.competition_start_date = request.PUT.get('competition_start_date')
            comp.competition_end_date = request.PUT.get('competition_end_date')
            comp.start_time = request.PUT.get('start_time')
            comp.inscription_start_date = request.PUT.get('inscription_start_date')
            comp.inscription_end_date = request.PUT.get('inscription_end_date')
            comp.number_of_lanes = request.PUT.get('number_of_lanes')
            comp.pool_meters = request.PUT.get('pool_meters')
            comp.save()
            return HttpResponse('updated', status=200)
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context))
    else:
        return HttpResponse(status_code=405)
