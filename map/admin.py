from django.contrib import admin

# Register your models here.
from .models import Place, Image
from mapbox_location_field.admin import MapAdmin


class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image_tag')


admin.site.register(Place, MapAdmin)
admin.site.register(Image, ImageAdmin)
