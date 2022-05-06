from django import forms
from mascota.models import Mascota,Vacuna

class MascotaFormulario(forms.ModelForm):
    class Meta:
        model = Mascota

        fields = [
                'nombre',
                'raza',
                'sexo',
                'edad_aproximada',
                'fecha_rescate',
                'alimentacion',
                'enfermedades',
                'persona',
                'vacuna',
        ]

        labels ={
                'nombre': 'Nombre',
                'raza': 'Raza',
                'sexo': 'Sexo',
                'edad_aproximada': 'Edad ',
                'fecha_rescate': 'Fecha de Rescate',
                'alimentacion': 'Alimentacion',
                'enfermedades': 'Enfermedades',
                'persona': 'Adoptante',
                'vacuna': 'Vacunas',
        }

        widgets = {
                'nombre': forms.TextInput(attrs={'class':'form-control'}),
                'raza': forms.TextInput(attrs={'class':'form-control'}),
                'sexo':forms.TextInput(attrs={'class':'form-control'}),
                'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
                'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
                'alimentacion': forms.TextInput(attrs={'class':'form-control'}),
                'enfermedades': forms.TextInput(attrs={'class':'form-control'}),
                'persona': forms.Select(attrs={'class':'form-control'}),
                'vacuna':forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),


        }


class VacunaFormulario(forms.ModelForm):
    class Meta:
        model = Vacuna

        fields = [
                'nombre',
                
        ]

        labels ={
                'nombre': 'Nombre',
                
        }

        widgets = {
                'nombre': forms.TextInput(attrs={'class':'form-control'}),


        }