from django.contrib import admin

# Register your models here.
from .models import Place, Image
from mapbox_location_field.admin import MapAdmin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

admin.site.unregister(User)
admin.site.unregister(Group)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('preview', 'photo', 'place')
    readonly_fields = ('preview',)
    fieldsets = [
        (None, {'fields': ['photo', 'preview', 'layout', 'place']})
    ]


class ImageInline(admin.TabularInline):
    readonly_fields = ('preview',)
    model = Image


class PlaceAdmin(MapAdmin):
    list_display = ('name',  'date')
    inlines = [ImageInline]


admin.site.register(Place, PlaceAdmin)
admin.site.register(Image, ImageAdmin)
