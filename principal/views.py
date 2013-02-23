from principal.models import *
from django.contrib.auth.models import User 
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import AturnoForm 
from django.utils import simplejson as json
from principal.forms import RegistrarUsuarioForm,EditarUserFormAdm
from principal.forms import UsuarioTurnoForm

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

def usuarios(request):
	usuarios = User.objects.all()
	return render_to_response('usuarios.html', {'usuarios':usuarios}, context_instance=RequestContext(request))


def registrar_usuario(request):
	if request.method=='POST':
		usuario = request.POST.copy()
		usuario['password']=usuario['username']
		formulario=RegistrarUsuarioForm(usuario)
		#Hay diferencia entre is_valid() y is_valid, mientras que el primero valida mostrando los errores el ultimo no muestra los errores.
		if formulario.is_valid():
			formulario.save()
			usur2=User.objects.get(username=usuario['username'])
			usur2.set_password(usuario['username'])
			usur2.save()
			return HttpResponseRedirect('/usuarios/')
	else:
		formulario = RegistrarUsuarioForm()
	return render_to_response('nuevo-usuario.html', {'formulario':formulario}, context_instance=RequestContext(request))

def ajax_ver_usuario(request):	
	if request.is_ajax():
		clave=request.GET['id_usuario']
		usuario = User.objects.get(pk=clave) 
		data=json.dumps({'nombre':usuario.first_name,'apellido':usuario.last_name, 'email':usuario.email,'user':usuario.username,'direccion':usuario.direccion,'telefono':usuario.telefono})
		
		return HttpResponse(data, mimetype="application/json")
	else:
		raise Http404

def ajax_username(request):
	if request.is_ajax():
		username = request.GET['username']
		try:
			usuario = User.objects.get(username = username)
			data = usuario.username
		except:
			data = False
		return HttpResponse(data)
	else:
		raise Http404

def resetear_clave(request):
	if request.is_ajax():
		id_usuario = request.POST["id"]
		try:
			usuario= User.objects.get(pk=id_usuario)
			usuario.set_password(usuario.username)
			usuario.save()
			dato=usuario.username
		except:
			dato=False
		return HttpResponse(dato)
	else:
		raise Http404

def editar_usuario(request, id_usuario):
	usuario = User.objects.get(pk = id_usuario)
	if request.method=='POST':
		formulario = EditarUserFormAdm(request.POST, instance=usuario)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuarios')
	else:
		formulario = EditarUserFormAdm(instance = usuario)
	return render_to_response('editar-usuario.html', {'formulario':formulario, 'usuario':usuario}, context_instance=RequestContext(request))

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



