from django.db import models
from django.utils import timezone

class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    categoria = models.CharField(max_length=255)
    creado = models.DateTimeField(default=timezone.now)