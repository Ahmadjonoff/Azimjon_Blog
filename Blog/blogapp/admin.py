from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(Maqola)
class MaqolaAdmin(ModelAdmin):
    search_fields = ['id', 'sarlavha']
    list_display = ['id', 'sarlavha', 'sana']