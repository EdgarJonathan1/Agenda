from django.db import models

# Create your models here.
class Medico(models.Model):
	nombre = models.CharField(max_length=30)
	Direccion = models.CharField(max_length=100)
	Correo = models.CharField(max_length=100)

	def __str__(self):
		return "{0}".format(self.nombre)


class Paciente(models.Model):
	dni =models.CharField(max_length=8, primary_key=True)
	apellidoPaterno = models.CharField(max_length=35)
	apellidoMaterno = models.CharField(max_length=35)
	nombres = models.CharField(max_length=35)
	sexos = [
		('F','Femenino'),
		('M', 'Masculino')
	]
	sexo = models.CharField(max_length=1,choices=sexos,default='F')
	fechaNacimiento = models.DateField()

	Direccion = models.CharField(max_length=100)
	Correo = models.CharField(max_length=100)

	def nombreCompleto(self):
		txt = "{0},{1},{2}"
		return txt.format(self.apellidoPaterno,self.apellidoPaterno,self.nombres)

	def __str__(self):
		return  self.nombreCompleto()

class Cita(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	paciente =  models.ForeignKey(Paciente,null=False,blank=False,on_delete=models.CASCADE)
	medico =  models.ForeignKey(Medico,null=False,blank=False,on_delete=models.CASCADE)




