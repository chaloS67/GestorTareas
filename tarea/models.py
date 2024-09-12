from django.db import models

class Tarea(models.Model):
    titulo = models.CharField(max_length=150)
    descripcion = models.TextField(max_length=500)
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    ##limite = models.DateTimeField(null=True ,blank=True) ## campo no obligatorio
    completado=models.BooleanField(default=False)

    def __str__(self):
        return self.titulo




