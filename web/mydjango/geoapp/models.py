from django.db import models
from django.contrib.gis.db import models as models_geo


class GeoAlgo(models.Model):
    nombre = models.CharField(max_length=90)
    poligono = models_geo.PolygonField()
    
    def __str__(self):
        return self.nombre