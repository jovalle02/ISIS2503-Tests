from django.db import models

class Cama(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('ocupada', 'Ocupada'),
        ('mantenimiento', 'Mantenimiento'),
    ]

    numero = models.CharField(max_length=10, unique=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='disponible')

    def __str__(self):
        return f"Cama {self.numero} - {self.estado}"
