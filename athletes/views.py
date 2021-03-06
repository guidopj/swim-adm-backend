# Create your views here.

from athletes.models import Athlete
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import logging
from .forms import AthleteForm
from django.http import HttpResponse

logger = logging.getLogger(__name__)
# Create your views here.

def getAthletes(request):
    qs = Athlete.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)

@csrf_exempt
def saveAthlete(request):
    if request.method == "POST":
        logger.error (request.body)
        received_json_data = json.loads(request.body)
        logger.error (received_json_data)
        form = AthleteForm(received_json_data[0])
        if form.is_valid():
            athlete = form.save(commit=False)
            athlete.save()
            return HttpResponse(status=200)
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context), status=500)
    else:
        return HttpResponse(status=405)
