from django.contrib import admin
from .models import Terreno

# Register your models here.
@admin.register(Terreno)
class TerrenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'departamento', 'ciudad', 'barrio', 'tipo_calle', 'calle', 'numero1', 'numero2', 'area', 'nivelacion', 'tipo_suelo', 'caficultor_id')
    search_fields = ('nombre', 'departamento', 'ciudad', 'barrio')
    list_filter = ('departamento', 'ciudad', 'nivelacion', 'tipo_suelo')
    ordering = ('nombre',)