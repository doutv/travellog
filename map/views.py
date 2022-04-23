from django.conf import settings
from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
from .models import Place
import os
import glob


def _get_all_photos_url_in_directory(directory_name):
    '''
    Get relative paths of all photos in a given directory
    '''
    base_url = os.path.join("photos", directory_name)
    dir = os.path.join(settings.MEDIA_ROOT, directory_name)
    photo_exts = ("*.png", "*.JPG", "*.jpeg", "*.jpg")
    photos = []
    for photo_exts in photo_exts:
        photos.extend(glob.glob(photo_exts, root_dir=dir))
    photos = [os.path.join(base_url, filename) for filename in photos]
    return photos


def _render_index():
    template = get_template('index.html')
    context = {
        "place_list": Place.objects.all(),
        "location_dict": {},
        "mapbox_token": settings.MAPBOX_KEY
    }
    for place in context["place_list"]:
        context["location_dict"][place.name] = {
            "center": place.location,
            "zoom": 15,
            "duration": 8000,
        }
        place.photos = _get_all_photos_url_in_directory(place.name)
    return template.render(context)


def index(request):
    return HttpResponse(_render_index())
