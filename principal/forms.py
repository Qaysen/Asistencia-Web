#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *

class UsuarioTurnoForm(ModelForm):
    class Meta:
        model=UsuarioTurno