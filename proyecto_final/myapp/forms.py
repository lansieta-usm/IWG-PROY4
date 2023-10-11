from django import forms
from .models import Condicion

class RegistroUsuarioForm(forms.Form):
    name = forms.CharField(max_length=20, label='Nombre')
    alergias = forms.CharField(widget=forms.Textarea, label='Alergias')
    contact = forms.CharField(max_length=20, label='Contacto')
    num_contact = forms.IntegerField(label='Número de Contacto')
    condicion = forms.ModelChoiceField(
        queryset=Condicion.objects.values_list('condicion', flat=True),
        empty_label="Selecciona una condición",
        label='Condición Médica'
    )