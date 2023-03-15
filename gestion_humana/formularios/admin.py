from django.contrib import admin
from .models import Barrio

admin.site.register(Barrio)

class Formulario(admin.ModelAdmin):
    list_display=['id','barrio']



