from django.db import models
from django.contrib.auth.models import User

class Reporte(models.Model):
    CATEGORIA_OPCIONES = [
        ('B', 'Basura'),
        ('A', 'Alumbrado'),
        ('V', 'Baches'),
        ('S', 'Seguridad'),
        ('O', 'Otros'),
    ]
    
    ESTADO_OPCIONES = [
        ('P', 'Pendiente'),
        ('E', 'En Progreso'),
        ('R', 'Resuelto'),
    ]
    
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=1, choices=CATEGORIA_OPCIONES)
    ubicacion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to='reportes/', blank=True, null=True)
    estado = models.CharField(max_length=1, choices=ESTADO_OPCIONES, default='P')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo