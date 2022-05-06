
from django.urls import path
from django.contrib.auth.decorators import login_required
from usuario.views import RegistroUsuario, UsuarioEditPerfil, UsuarioPerfil,UsuarioEditContraseña,locked_out,ListadeUsuario,ListadeUsuarioPDF

urlpatterns = [
    path('registrar/', RegistroUsuario.as_view(), name='usuario_registrar'),
    path('listado/', login_required(ListadeUsuario.as_view()), name='usuario_listado'),
    path('listadoPDF/', login_required(ListadeUsuarioPDF.as_view()), name='usuariopdf'),
    path('Perfil/', login_required(UsuarioPerfil.as_view()), name='usuario_perfil'),
    path('Editar/Perfil/<int:pk>/', login_required(UsuarioEditPerfil.as_view()), name='usuario_perfil_edit'),
    path('Editar/Contraseña/', login_required(UsuarioEditContraseña.as_view()), name = 'editar_password'),
    path('Bloqueo/', locked_out, name='Bloqueo'),
    #path('Rostro/', ValidarCara, name='validar_rostro'),
    #path('Registro rostro/', RegistroCaras, name='registrar_rostro'),
]