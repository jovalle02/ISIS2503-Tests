from django.contrib import admin
from .models import MaterialMedico

@admin.register(MaterialMedico)
class MaterialMedicoAdmin(admin.ModelAdmin):
    list_display = ('tipo', 'nombre')
    list_filter = ('tipo',)
    search_fields = ('nombre',)
