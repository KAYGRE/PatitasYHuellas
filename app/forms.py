from django import forms
from django.forms import ModelForm 
from django.forms import widgets 
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Tipocli, Cliente, Tipomascota, Mascotas

class ClienteForm(forms.ModelForm):
    
    class Meta: 
        model = Cliente 
        fields = ['rutcliente', 'nombrecliente','contacto', 'tipocli']
        labels = {
            'rutcliente': 'Rutcliente',
            'nombrecliente': 'Nombrecliente',
            'contacto':'Contacto',
            'tipocli': 'Tipocli',
        }
        widgets={
            'rutcliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite su Rut',
                    'id': 'rutcliente'
                }
            ),
            'nombrecliente': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite su Nombre',
                    'id': 'nombrecliente'
                }
            ),
            'contacto': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite su numero de telefono',
                    'id': 'contacto'
                }
            ),
            'tipocli':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'tipocli'
                }
            ),
        }


class MascotaForm(forms.ModelForm):
    
    class Meta: 
        model = Mascotas 
        fields = ['codmascota', 'nombremascota', 'tipomascota', 'imagen']
        labels = {
            'codmascota': 'Codmascota',
            'nombremascota': 'Nombremascota',
            'tipomascota': 'Tipomascota',
            'imagen': 'Imagen'
        }
        widgets={
            'codmascota': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Digite el Codigo de la Mascota',
                    'id': 'codmascota'
                }
            ),
            'nombremascota': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder':'Digite el Nombre de la Mascota',
                    'id': 'nombremascota'
                }
            ),
            'tipomascota':forms.Select(
                attrs = {
                    'class': 'form-control',
                    'id': 'tipomascota'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            )
        }
