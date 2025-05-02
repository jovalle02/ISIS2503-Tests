from django.db import models

class MaterialMedico(models.Model):
    TIPO_CHOICES = [
        ('cama', 'Cama'),
        ('instrumento', 'Instrumento médico'),
        # ...otros tipos
    ]

    tipo = models.CharField(
        max_length=20,
        choices=TIPO_CHOICES,
        default='cama',
        help_text='Selecciona el tipo de material médico'
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Material Médico'
        verbose_name_plural = 'Materiales Médicos'

    def __str__(self):
        return f"{self.get_tipo_display()}: {self.nombre}"
