from principal.models import *
from django.contrib.auth.models import User 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import AturnoForm 
from django.utils import simplejson as json


def turno(request):
	turno = Turno.objects.all()
	return render_to_response('turno.html', {'turno':turno}, context_instance=RequestContext(request))

def agregar_turno(request):	
	if request.is_ajax():		
		if request.method=="POST":
			formulario = AturnoForm(request.POST)			
			if formulario.is_valid():
				formulario.save()
				turno=Turno.objects.latest("id")
				data=json.dumps({'nombre':str(turno.nombre),'hora_turno':str(turno.hora_turno)})
			else:
				data="formularo no valido"
		else:
			data="error"					
	else:
		data= 'Respuesta no es ajax'
	return HttpResponse(data, mimetype='aplication/json')

def eliminar_turno(request):
	if request.is_ajax():
		if request.method=="POST":
			pk=request.POST['pk']
			eliTurno = Turno.objects.get(pk=pk)
			eliTurno.delete()
			dato={'ojo':'true'}
			return HttpResponse(dato)

def edit_nombre(request):
	clave=request.POST["pk"]
	dato=request.POST["value"]
	Turno.objects.filter(pk=clave).update(nombre = dato)
	return HttpResponse(True)