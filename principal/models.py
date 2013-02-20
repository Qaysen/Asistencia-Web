from django.db import models
from django.contrib.auth.models import User

GENERO = (
	('Masculino','Masculino'),
	('Femenino','Femenino')
)

TIPO_PUESTO = (
		('Operario','Operario'),
		('Supervisor','Supervisor'),
		('Vigilante','Vigilante')
)

User.add_to_class('telefono', models.IntegerField(null=True,blank=True, max_length=7))
User.add_to_class('dni', models.IntegerField(null=True,blank=True, max_length=8))
User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('genero', models.CharField(null=True,blank=True, choices=GENERO, max_length=30))
User.add_to_class('puesto', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('sueldo', models.FloatField(null=True,blank=True, choices=TIPO_PUESTO, max_length=100 ))

class Control(models.Model):
	fecha_ingreso = models.DateTimeField(auto_now=True)
	fecha_salida = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return unicode(self.usuario)

class Turno(models.Model):
	nombre = models.CharField(max_length=100)
	hora_turno = models.TimeField()

	def __unicode__(self):
		return self.nombre


class UsuarioTurno(models.Model):
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()
	usuario = models.ForeignKey(User)
	turno = models.ForeignKey(Turno)

	def __unicode__(self):
		return unicode(self.usuario)

class Descuento(models.Model):
	magnitud = models.CharField(max_length=100)
	porcentaje = models.FloatField()
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()

	def __unicode__(self):
		return '%s x %s' %(self.porcentaje, self.magnitud)