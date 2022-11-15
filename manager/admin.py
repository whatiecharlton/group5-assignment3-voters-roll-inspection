from django.contrib import admin
from manager.models import *


# Register your models here.
@admin.register(VotersRoll)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('name','surname','constituency','is_registered','id_number')
    search_fields = ('name','id_number')


