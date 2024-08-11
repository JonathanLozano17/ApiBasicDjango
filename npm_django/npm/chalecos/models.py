from django.db import models

class Chalecos(models.Model):
    serial = models.IntegerField(primary_key=True)
    beneficiario_cedula = models.ForeignKey(
        'beneficiarios.Beneficiarios',  # nombre_app.nombre_modelo
        on_delete=models.CASCADE,
        related_name='chalecos'
    )
