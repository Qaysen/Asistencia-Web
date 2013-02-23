#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AturnoForm(ModelForm):
    hora_turno = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    class Meta:
    	model= Turno

