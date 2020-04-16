from .models import Competition
from django.contrib import messages
from .forms import CompetitionForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def getCompetitions(request):
    return Competition.objects.all()

@csrf_exempt
def saveCompetition(request):
    messages.success(request, request.POST)
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            competition = form.save(commit=False)
            value = competition.save()
            messages.success(request, value)
            return HttpResponse(status=200)
        else:
            messages.error(request, form.errors)
            return HttpResponse(status=500, content=form.errors)
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
            return HttpResponse('ERROR', status_code=500)
    else:
        return HttpResponse(status_code=405)
