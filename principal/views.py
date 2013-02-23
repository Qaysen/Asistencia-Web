from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import DescuentoForm, ControlForm
from django.utils import simplejson as json
from django.core import serializers
import random

def descuentos(request):
	descuentos = Descuento.objects.all()
	return render_to_response('descuentos.html', {'descuentos':descuentos}, context_instance=RequestContext(request))

def graficos_descuentos(request):
	descuentos = Descuento.objects.all()
	return render_to_response('graficos-descuentos.html', {'descuentos':descuentos}, context_instance=RequestContext(request))

def agregar_descuento(request):
	dato = "hola"
	if request.is_ajax():
		dato = "si es ajax"
		if request.method == 'POST':
			formulario = DescuentoForm(request.POST)
			dato = "si es post "
			if formulario.is_valid():
				formulario.save()
				descuento = Descuento.objects.latest("id")
				dato = json.dumps({'pk':descuento.id, 'magnitud':descuento.magnitud,'porcentaje':descuento.porcentaje, 'fecha_inicio': str(descuento.fecha_inicio), 'fecha_termino':str(descuento.fecha_termino)})
			else:
				dato = "El formulario no es valido"
		else:
			dato = "hubo un error"
	else:
		dato = "No es ajax"
	return HttpResponse(dato, mimetype="application/json")

def editar_descuento(request):
	clave = request.POST['pk']
	dato = request.POST['value']
	campo = request.POST['name']
	editar = { campo: dato } 
	descuento = Descuento.objects.filter(pk = clave).update(**editar)
	#descuento = Descuento.objects.get(pk = clave)
	#descuento.request.POST['name'] = dato
	#descuento.save()
	return HttpResponse(True)

def eliminar_descuento(request):
	dato = "hola"
	pk = request.POST['id']
	if request.is_ajax():
		dato = "si es ajax"
		if request.method == 'POST':
			descuento = Descuento.objects.get(pk=pk)
			dato = json.dumps(descuento)
			descuento.delete()
		else:
			dato = "hubo un error"
	else:
		dato = "No es ajax"
	return HttpResponse(dato, mimetype='application/json')

def ajax_usuarios(request):
	usuarios = User.objects.all()
	dato = serializers.serialize('json', usuarios)
	return HttpResponse(dato, mimetype="application/json")

def controles(request):
	controles = Control.objects.all()
	return render_to_response('controles.html', {'controles':controles}, context_instance=RequestContext(request))

def agregar_control(request):
	dato = "hola"
	if request.is_ajax():
		dato = "si es ajax"
		if request.method == 'POST':
			formulario = ControlForm(request.POST)
			dato = "si es post "
			if formulario.is_valid():
				formulario.save()
				control = Control.objects.latest("id")
				dato = json.dumps({'pk':control.id, 'usuario':str(control.usuario),'fecha_ingreso': str(control.fecha_ingreso), 'fecha_salida':str(control.fecha_salida)})
		else:
			dato = "hubo un error"
	else:
		dato = "No es ajax"
	return HttpResponse(dato, mimetype="application/json")

def registrar_controles(request):
	if request.method == 'POST':
		formulario = ControlForm(request.POST)
		if formulario.is_valid:
			formulario.save()
			usuarios = User.objects.all()
			cantidad_de_usuarios = len(usuarios)
			n = random.randint(1,cantidad_de_usuarios)
			control = Control.objects.latest("id")
			Control.objects.filter(pk=control.id).update(usuario=n)
			return HttpResponseRedirect('/registrar-controles/')
	else:
		formulario = ControlForm()
	return render_to_response('registrar-control.html', {'formulario':formulario}, context_instance=RequestContext(request))

def registrar_usuario(request):
	if request.method == 'POST':
		formulario = RegistrarUsuarioForm(request.POST)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios/')
	else:
		formulario = RegistrarUsuarioForm()
	return render_to_response('nuevo-usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))
