from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .forms import EventForm
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)
from .models import Event

@csrf_exempt
def saveEvent(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        logger.error(received_json_data.values())
        form = EventForm(received_json_data)
        if form.is_valid():
            event = form.save(commit=True)
            event.save()
            return HttpResponse(status=200)
        else:
            context = {'errors': form.errors}
            return HttpResponse("ERROR: " + str(context), status=500)
    else:
        return HttpResponse(status=405)

def getEvents(request):
    qs = Event.objects.all()
    data = list(qs.values())
    return JsonResponse(data, safe=False)
