"""refugio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from usuario.views import locked_out
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView,logout_then_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Adopcion/',include('adopcion.urls')),
    path('Mascota/',include('mascota.urls')),
    path('Usuario/',include('usuario.urls')),
    #path('',LoginView.as_view(template_name='index.html'),name='inicio'),
    path('',LoginView.as_view(template_name='index.html'),name='login'),
    path('accounts/login/',LoginView.as_view(template_name='index.html'),name='inicio'),
    path('Logout',logout_then_login,name='logout'),
    path('password-reset', PasswordResetView.as_view(template_name='passwordReset/passwordResetForm.html',email_template_name='passwordReset/PasswordResetEmail.html'), name='password_reset'),
    path('password-reset/done', PasswordResetDoneView.as_view(template_name='passwordReset/passwordResetDone.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name='passwordReset/passwordResetConfirm.html'), name='password_reset_confirm'),
    path('password-reset-reset', PasswordResetCompleteView.as_view(template_name='passwordReset/passwordResetComplete.html'), name='password_reset_complete'),
    path('locked/', locked_out, name='locked_out'),
    path('captcha/', include('captcha.urls')),
]
