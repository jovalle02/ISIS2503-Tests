from django.db import models

class MaterialMedicoReservable(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('mantenimiento', 'Mantenimiento'),
    ]

    nombre = models.CharField(max_length=100, unique=True)
    estado = models.CharField(max_length=15, choices=ESTADOS, default='disponible')

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"
