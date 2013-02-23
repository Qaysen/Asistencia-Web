from principal.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms

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
        exclude = ("is_staff","is_superuser","last_login", "groups", "user_permissions", "date_joined", 'password', 'password1', 'password2')






class UsuarioTurnoForm(ModelForm):
    class Meta:
        model=UsuarioTurno

