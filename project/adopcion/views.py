from django.shortcuts import render, get_object_or_404
from .models import Mascota
from django.contrib.auth.decorators import login_required
from .forms import BusquedaMascotasForm

def lista_mascotas(request):
    if request.method == 'GET':
        form = BusquedaMascotasForm(request.GET)
        if form.is_valid():
            especie = form.cleaned_data.get('especie')
            nombre = form.cleaned_data.get('nombre')
            edad = form.cleaned_data.get('edad')
            tamaño = form.cleaned_data.get('tamaño')
            genero = form.cleaned_data.get('genero')
            mascotas = Mascota.objects.filter(especie=especie, nombre__icontains=nombre, edad=edad, tamaño=tamaño, genero=genero)
        else:
            mascotas = Mascota.objects.all()
    else:
        form = BusquedaMascotasForm()
        mascotas = Mascota.objects.all()
    return render (request, 'adopcion_mascotas/lista_mascotas.html', {'mascotas': mascotas, 'form': form})

@login_required
def adoptar_mascota(request, mascota_id):
    mascota = get_object_or_404(Mascota, pk=mascota_id)
    if request.method == 'POST':
        # Adoptar la mascota (y luego eliminarla de la base de datos)
        mascota.delete()
        return render(request, 'adopcion_mascotas/adoptar_mascota_exitosa.html', {'mascota': mascota})
    return render(request, 'adopcion_mascotas/adoptar_mascota_exitosa.html', {'mascota': mascota})

def adoptar_mascota_exitosa(request):
    return render(request, 'adopcion_mascotas/adoptar_mascota_exitosa.html')

