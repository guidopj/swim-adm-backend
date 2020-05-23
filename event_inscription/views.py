from django.http import HttpResponse
from .forms import EventInscriptionForm
import logging
logger = logging.getLogger(__name__)

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import json

def removeIfSaved(array):
    del array[0]

@csrf_exempt
def saveInscriptions(request):
    if request.method == "POST":
        data = request.body.decode('utf-8')
        received_json_data = json.loads(data)
        inscriptionList = received_json_data["inscriptions"]
        inscriptionListCopy = inscriptionList
        for inscription in inscriptionList:
            inscription["competition_name"] = received_json_data["competition_name"]
            form = EventInscriptionForm(inscription)
            if form.is_valid():
                inscription = form.save(commit=True)
                inscription.save()
                logger.error(inscription)
                removeIfSaved(inscriptionListCopy)
            else:
                context = {'errors': form.errors, 'not_saved': inscriptionListCopy}
                return HttpResponse("ERROR: " + str(context), status=500)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=405)