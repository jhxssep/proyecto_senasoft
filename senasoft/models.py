from django.db import models

class Competidor(models.Model):
    nombre = models.CharField(max_length=120)
    centro = models.CharField(max_length=150)
    categoria = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.centro} ({self.categoria})"
