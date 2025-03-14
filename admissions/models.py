from django.db import models

from camas.models import Cama

class Admission(models.Model):
    cama = models.ForeignKey(Cama, on_delete=models.CASCADE, null=True, blank=True)  # Relación con la cama
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_type = models.CharField(max_length=3, choices=[
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ])
    
    admission_date = models.DateTimeField(auto_now_add=True)
    admission_age = models.IntegerField(default=0)
    reason = models.TextField()
    status = models.CharField(max_length=50, choices=[
        ('Pendiente', 'Pendiente'),
        ('Autorizado', 'Autorizado'),
        ('Rechazado', 'Rechazado')
    ])
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.status}"
