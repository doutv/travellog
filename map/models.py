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
