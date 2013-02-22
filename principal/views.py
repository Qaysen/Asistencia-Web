from principal.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import UsuarioTurnoForm
from django.utils import simplejson as json 


def usuarioTurno(request):
	usuarioTurno = UsuarioTurno.objects.all()
	usuarios=User.objects.all()
	turnos=Turno.objects.all()
	return render_to_response('usuarioTurno.html', {'usuarioTurno':usuarioTurno,'usuarios':usuarios,'turnos':turnos}, context_instance=RequestContext(request))

def edit_fechas(request):
	clave=request.POST["pk"]
	dato=request.POST["value"]
	campo=request.POST["name"]
	filtrar={campo:dato}
	UsuarioTurno.objects.filter(pk=clave).update(**filtrar)
	return HttpResponse(True)


def edit_usuario(request):
	clave=request.POST["pk"]
	dato=request.POST["value"]
	UsuarioTurno.objects.filter(pk=clave).update(usuario = dato)
	return HttpResponse(True)

def eliminarUT(request):	
	if request.is_ajax():
		if request.method=="POST":	
			pk=request.POST['pk']			
			elim_usuarioTurno=UsuarioTurno.objects.get(pk=pk)
			dato={'sdf':'sdfsdf'}
			elim_usuarioTurno.delete()
		else:			
			dato="Error"
	else:
		dato="No es ajax"
	return HttpResponse(dato)


def agregarUT(request):	
	data="valor inicial"
	if request.is_ajax():
		if request.method=="POST":
			formulario=UsuarioTurnoForm(request.POST)
			if formulario.is_valid():
				formulario.save()
				ut=UsuarioTurno.objects.latest("id")
				data=json.dumps({'usuario':ut.usuario_id,'turno':ut.turno_id,'fecha_inicio':str(ut.fecha_inicio),'fecha_termino':str(ut.fecha_termino)})
	else:
		data="Respuesta no es ajax"
	return HttpResponse(data,mimetype='application/json')

def ver_usuarios(request):	
    usuarios = User.objects.filter(**qdct_as_kwargs(request.POST)).order_by('id') 
    #return JSONResponse with id and name
    return JSONResponse(usuarios.values('id','username'))




 
   