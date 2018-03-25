from django.contrib import admin
from .models import GeoAlgo


@admin.register(GeoAlgo)
class GeoAlgoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    search_fields = ['nombre']