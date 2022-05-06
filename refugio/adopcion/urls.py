from django.urls import path
from adopcion import views
from django.contrib.auth.decorators import login_required
from adopcion.views import SolicitudList, SolicitudCreate,SolicitudUpdate,SolicitudDelete

urlpatterns = [
    path('solicitud/lista', login_required(SolicitudList.as_view()), name='solicitud_listado'),
    path('solicitud/nueva', login_required(SolicitudCreate.as_view()), name='solicitud_crear'),
    path('solicitud/editar/<int:pk>/', login_required(SolicitudUpdate.as_view()), name='solicitud_editar'),
    path('solicitud/eliminar/<int:pk>/',login_required( SolicitudDelete.as_view()), name='solicitud_eliminar'),
]