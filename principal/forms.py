#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DescuentoForm(ModelForm):
    class Meta:
        model=Descuento

class ControlForm(ModelForm):
    class Meta:
        model=Control

class AturnoForm(ModelForm):
    hora_turno = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
    	model= Turno

'''class UsuarioTurnoForm(ModelForm):
    class Meta:
        model=UsuarioTurno'''

class RegistrarUsuarioForm(ModelForm):
    username=forms.CharField(label="DNI" , max_length=8)
    class Meta:
        model = User
        exclude = ("is_staff", "is_superuser", "last_login", "groups", "user_permissions", "date_joined")

class EditarUserFormAdm(ModelForm):
    first_name = forms.CharField(label='Nombres')
    email= forms.EmailField(label="Email")
    is_active= forms.BooleanField(label="Usuario activo", required=False)
    username= forms.CharField(label="Nombre de usuario")
    class Meta:
        model = User
        exclude = ("is_staff","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2','puesto','sueldo','turno')