from django import forms
from .models import *

class FormularioCliente(forms.ModelForm):
    class Meta: 
        model = Cliente
        fields = '__all__'
        widgets = {}