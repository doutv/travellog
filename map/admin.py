from django.contrib import admin

# Register your models here.
from .models import Place
from mapbox_location_field.admin import MapAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)


class PlaceAdmin(MapAdmin):
    list_display = ('name',  'date')


admin.site.register(Place, PlaceAdmin)
