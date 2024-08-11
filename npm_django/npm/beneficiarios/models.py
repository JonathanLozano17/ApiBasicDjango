from django.db import models

class Beneficiarios(models.Model):
    cedula = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    poblacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
