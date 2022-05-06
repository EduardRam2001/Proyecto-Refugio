from django.contrib import admin
from .models import Persona, Solicitud
from import_export.admin import ImportExportModelAdmin

# Register your models here.

@admin.register(Persona)
class PersonaAdmin(ImportExportModelAdmin):
    search_fields =('id','nombre','apellidos',)
    list_display = ('id','nombre','apellidos','edad','telefono','email','direccion',)
    
    

@admin.register(Solicitud)
class SolcitudAdmin(ImportExportModelAdmin):
    search_fields =('id',)
    list_display = ('persona','numero_mascotas','razones',)



