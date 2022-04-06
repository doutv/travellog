from django.db import models
from mapbox_location_field.models import LocationField
from django.conf import settings
import django.utils.timezone as timezone
from django.utils.safestring import mark_safe
# Create your models here.


class Place(models.Model):
    name = models.CharField(max_length=50)
    location = LocationField()
    notes = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)


class Image(models.Model):
    IMAGE_LAYOUTS = (
        ("1x1", "1x1"),
        ("1x2", "1x2"),
        ("1x3", "1x3"),
        ("2x1", "2x1"),
        ("2x2", "2x2"),
        ("2x3", "2x3"),
        ("3x1", "3x1"),
        ("3x2", "3x2"),
        ("3x3", "3x3"),
    )
    photo = models.ImageField()
    layout = models.CharField(
        max_length=10, choices=IMAGE_LAYOUTS, default="1x1")
    place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)

    @property
    def preview(self):
        if self.photo:
            return mark_safe(f'<img src="{self.photo.url}" style="max-width: auto; height: 200px;" />')
        else:
            return 'No Image Found'
