from django.shortcuts import render, get_object_or_404, redirect
from .models import Mascota
from django.contrib.auth.decorators import login_required
from .forms import BusquedaMascotasForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import CargarMascotaForm

def home(request):
    return render(request, 'home.html')

def lista_mascotas(request):
    if request.method == 'GET':
        form = BusquedaMascotasForm(request.GET)
        if form.is_valid():
            especie = form.cleaned_data.get('especie')
            nombre = form.cleaned_data.get('nombre')
            edad = form.cleaned_data.get('edad')
            tamaño = form.cleaned_data.get('tamaño')
            genero = form.cleaned_data.get('genero')
            mascotas = Mascota.objects.filter(especie=especie, nombre__icontains=nombre, edad=edad)
            if tamaño:
                mascotas = mascotas.filter(tamaño=tamaño)
            if genero:
                mascotas = mascotas.filter(genero=genero)
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

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lista_mascotas')  # Redirigir al usuario a la página principal después del registro
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})

def inicio_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirigir al usuario/a a la página principal después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'inicio_sesion.html', {'form': form})

@login_required
def cargar_mascota(request):
    if request.method == 'POST':
        form = CargarMascotaForm(request.POST, request.FILES)
        if form.is_valid():
            mascota = form.save(commit=False)
            mascota.usuario = request.user  # Usuario/a actual como adoptante de la mascota
            mascota.save()
            return redirect('lista_mascotas')  # Redirigir al usuario/a a la página principal después de cargar la mascota
    else:
        form = CargarMascotaForm()
    return render(request, 'adopcion_mascotas/cargar_mascota.html', {'form': form})