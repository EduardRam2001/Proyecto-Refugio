from django.db import models
from adopcion.models import Persona

# Create your models here.
class Vacuna(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
       	 return '{}'.format(self.nombre)

class Mascota(models.Model):
	nombre = models.CharField(max_length=50)
	raza = models.CharField(max_length=50)
	sexo = models.CharField(max_length=10)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
	alimentacion = models.CharField(max_length=100)
	enfermedades = models.CharField(max_length=100)
	persona = models.ForeignKey(Persona, null=True,blank=True,on_delete=models.CASCADE)
	vacuna=models.ManyToManyField(Vacuna,blank=True)

	def __str__(self):
       	 return '{}'.format(self.nombre)