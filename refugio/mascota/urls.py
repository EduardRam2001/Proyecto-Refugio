from django.urls import path
from mascota.views import MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete,home, ListadeMascotaPDF 
from django.contrib.auth.decorators import login_required
from mascota.views import MascotaListInvitado, VacunaCreate



urlpatterns = [
    path('Nueva', login_required(MascotaCreate.as_view()) , name= "mascota_crear"),
    path('Lista', MascotaList.as_view() , name= "mascota_lista"),
    path('Listapdf', ListadeMascotaPDF.as_view() , name= "mascotapdf"),
    path('ListaInvitado', MascotaListInvitado.as_view() , name= "mascota_lista_invitado"),
    path('Editar/<int:pk>/', login_required(MascotaUpdate.as_view()) , name= "mascota_editar"),
    path('Eliminar/<int:pk>/', login_required(MascotaDelete.as_view()) , name= "mascota_delete"),
    path('', home , name='home'),
    path('Vacuna/', VacunaCreate.as_view() , name= "vacuna_nueva"),
]