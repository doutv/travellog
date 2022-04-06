from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Place
# Create your views here.


def _render_index():
    template = get_template('index.html')
    context = {
        "place_list": Place.objects.all(),
        "location_dict": {},
        "mapbox_token": settings.MAPBOX_KEY
    }
    for place in Place.objects.all():
        context["location_dict"][place.name] = {
            "center": place.location,
            "zoom": 15,
            "duration": 8000,
        }
    return template.render(context)


def index(request):
    return HttpResponse(_render_index())
