from django.shortcuts import render, get_object_or_404
from .models import Mascota
from django.contrib.auth.decorators import login_required

def lista_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'adopcion/lista_mascotas.html', {'mascotas': mascotas})

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
