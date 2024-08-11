from django.contrib import admin
from .models import Chalecos

@admin.register(Chalecos)
class ChalecosAdmin(admin.ModelAdmin):
    list_display = ('serial', 'beneficiario_cedula')
    search_fields = ('serial', 'beneficiario_cedula__cedula', 'beneficiario_cedula__nombre')
