
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm 
from django.contrib.auth.forms import PasswordChangeForm
from captcha.fields import CaptchaField




class RegistroForm(UserCreationForm):

	class Meta:
		model = User
		fields = [
				'username',
				'first_name',
				'last_name',
				'email',
			]
		labels = {
				'username': 'Nombre de usuario',
				'first_name': 'Nombre',
				'last_name': 'Apellido',
				'email': 'Correo',
		}



class UserPerfil(ModelForm):

	class Meta:
		model = User
		fields = ['username',
				'first_name',
				'last_name',
				'email',]

		widgets = {
                'username': forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
				'email':forms.TextInput(attrs={'class':'form-control'}),
				
        	}
		exclude =['password','user_permissions','last_login','date_joined','is_superuser','is_active','is_staff','groups']


class PasswordEdit (PasswordChangeForm):
	old_password = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	new_password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','type':'password'}))
	new_password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class':'form-control','type':'password'}))


	class Meta:
		model = User
		fields = ('old_password','new_password1','new_password2')


class AxesCaptchaForm(forms.Form):
    captcha = CaptchaField()
