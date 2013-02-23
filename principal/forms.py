#encoding:utf-8
from django.forms import ModelForm
from django import forms
from principal.models import *

class DescuentoForm(ModelForm):
    class Meta:
        model=Descuento

class ControlForm(ModelForm):
    class Meta:
        model=Control