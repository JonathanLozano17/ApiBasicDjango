from django.contrib import admin
from .models import Beneficiarios

@admin.register(Beneficiarios)
class BeneficiariosAdmin(admin.ModelAdmin):
    list_display = ('cedula', 'nombre', 'direccion', 'poblacion')
    search_fields = ('cedula', 'nombre')
