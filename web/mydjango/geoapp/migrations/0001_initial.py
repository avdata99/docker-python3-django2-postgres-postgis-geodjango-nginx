# Generated by Django 2.0.3 on 2018-03-25 19:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GeoAlgo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=90)),
                ('poligono', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]
