from django import forms
from .models import Mascota

class BusquedaMascotasForm(forms.Form):
    ESPECIES_CHOICES = [('perro', 'Perro'), ('gato', 'Gato')]
    
    especie = forms.ChoiceField(label='Especie', choices=ESPECIES_CHOICES, required=False)
    nombre = forms.CharField(label='Nombre', max_length=100, required=False)
    edad = forms.IntegerField(label='Edad (meses o años)', min_value=0, required=False)
    tamaño = forms.ChoiceField(label='Tamaño', choices=[('chico', 'Chico'), ('mediano', 'Mediano'), ('grande', 'Grande')], required=False)
    genero = forms.ChoiceField(label='Género', choices=[('macho', 'Macho'), ('hembra', 'Hembra')], required=False)

class CargarMascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'edad', 'tamaño', 'genero', 'descripcion', 'imagen1', 'imagen2', 'imagen3']