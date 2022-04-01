from django.conf import settings
from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Place
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    context = {
        "place_list": Place.objects.all(),
        "location_dict": {},
        "mapbox_token": settings.MAPBOX_TOKEN
    }
    for place in Place.objects.all():
        context["location_dict"][place.name] = {
            "center": [place.longitude, place.latitude],
            "zoom": 15,
            "bearing": 35,
            "pitch": 40,
            "duration": 8000,
        }
    return HttpResponse(template.render(context, request))
