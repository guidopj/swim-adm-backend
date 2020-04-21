from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .forms import TeamForm
from django.http import HttpResponse
from .models import Team
from django.http import JsonResponse

logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
def saveTeam(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        logger.error(received_json_data)
        form = TeamForm(received_json_data)
        if form.is_valid():
            team = form.save(commit=False)
            team.save()
            return HttpResponse(status=200)
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context), status=500)
    else:
        return HttpResponse(status=405)

def getTeams(request):
    qs = Team.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)