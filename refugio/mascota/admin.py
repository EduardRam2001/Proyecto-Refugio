from django.contrib import admin
from mascota.models import Mascota, Vacuna
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(Mascota)
class MascotaAdmin(ImportExportModelAdmin):
    search_fields =('id','nombre',)
    list_display = ('nombre','sexo','edad_aproximada','fecha_rescate','persona',)


@admin.register(Vacuna)
class VacunaAdmin(ImportExportModelAdmin):
    search_fields =('nombre',)
    list_display = ('nombre',)
