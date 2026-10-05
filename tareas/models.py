from django.db import models
from django.contrib.auth.models import User
class Tarea(models.Model):
    titulo = models.CharField(
        max_length=100
    )
    descripcion = models.TextField(
        blank=True
    )
    completada = models.BooleanField(
        default=False
    )
    usuario = models.ForeignKey(
    User,
        on_delete=models.CASCADE,
        related_name='tareas'
    )
    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )
    def __str__(self):
        return self.titulo