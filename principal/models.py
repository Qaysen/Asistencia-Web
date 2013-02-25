from django.db import models
from django.contrib.auth.models import User

GENERO = (
	('Masculino','Masculino'),
	('Femenino','Femenino')
)

class Turno(models.Model):
	nombre = models.CharField(max_length=100)
	hora_turno = models.TimeField()
	
	def __unicode__(self):
		return self.nombre

User.add_to_class('telefono', models.IntegerField(null=True,blank=True, max_length=7))
User.add_to_class('direccion', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('genero', models.CharField(null=True,blank=True, choices=GENERO, max_length=30))
User.add_to_class('puesto', models.CharField(null=True,blank=True, max_length=500))
User.add_to_class('sueldo', models.FloatField(null=True,blank=True, max_length=100 ))
User.add_to_class('turno', models.ForeignKey(Turno, null=True, blank=True))

class Control(models.Model):
	fecha_ingreso = models.DateTimeField(auto_now=True)
	usuario = models.ForeignKey(User)

	def __unicode__(self):
		return unicode(self.usuario)

class Descuento(models.Model):
	magnitud = models.CharField(max_length=100)
	porcentaje = models.DecimalField(decimal_places=2, max_digits=12)
	fecha_inicio = models.DateField()
	fecha_termino = models.DateField()

	def __unicode__(self):
		return '%s x %s' %(self.porcentaje, self.magnitud)