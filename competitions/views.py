from .models import Competition
from django.core import serializers
from django.http import JsonResponse
from .forms import CompetitionForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
logger = logging.getLogger(__name__)

# Create your views here.

def getCompetitions(request):
    qs = Competition.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)

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
