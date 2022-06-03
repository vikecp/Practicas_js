from django.db import models
from django.contrib.auth.models import User

# Cada clase sera una tabla, y sus atributos sus columnas


class Tarea(models.Model):
    usuario = models.ForeignKey(User,
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(null=True,
                                blank=True)
    completo = models.BooleanField(default=False)


    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['completo']

