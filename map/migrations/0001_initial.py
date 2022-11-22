# Generated by Django 3.2.12 on 2022-04-05 12:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('location', mapbox_location_field.models.LocationField(map_attrs={})),
                ('notes', models.TextField(blank=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('layout', models.CharField(choices=[('1x1', '1x1'), ('1x2', '1x2'), ('1x3', '1x3'), ('2x1', '2x1'), ('2x2', '2x2'), ('2x3', '2x3'), ('3x1', '3x1'), ('3x2', '3x2'), ('3x3', '3x3')], default='1x1', max_length=10)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.place')),
            ],
        ),
    ]