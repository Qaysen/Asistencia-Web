from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from principal.forms import RegistrarUsuarioForm,EditarUserFormAdm
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import simplejson as json

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
