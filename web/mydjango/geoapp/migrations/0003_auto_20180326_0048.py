# Generated by Django 2.0.3 on 2018-03-26 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geoapp', '0002_geoalgo_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='geoalgo',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
    ]