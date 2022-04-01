from django.contrib import admin

# Register your models here.
from .models import Place, Image


class ImageAdmin(admin.ModelAdmin):
    list_display = ('place', 'image_tag')


admin.site.register(Place)
admin.site.register(Image, ImageAdmin)
