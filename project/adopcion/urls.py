from django.urls import path
from . import views
from .views import adoptar_mascota_exitosa


urlpatterns = [
    path('', views.lista_mascotas, name='lista_mascotas'),
    path('adoptar/<int:mascota_id>/', views.adoptar_mascota, name='adoptar_mascota'),
    path('adoptar-exitosa/', views.adoptar_mascota_exitosa, name='adoptar_mascota_exitosa'),
    path('registro/', views.registro, name='registro'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio_sesion'),
]