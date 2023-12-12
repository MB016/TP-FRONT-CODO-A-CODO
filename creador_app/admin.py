from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Creador

# Register your models here.
@admin.register(Creador)
class ModoCreador(ModelAdmin):
    ...