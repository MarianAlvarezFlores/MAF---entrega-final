from django.db import models

class Mascota(models.Model):
    ESPECIES_CHOICES = [
        ('Perro', 'Perro'),
        ('Gato', 'Gato'),
    ]
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    especie = models.CharField(max_length=10, choices=ESPECIES_CHOICES)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='mascotas/')

