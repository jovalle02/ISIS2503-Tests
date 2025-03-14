import requests
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import generics
from django.http import JsonResponse

from camas.models import Cama
from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionViewSet(viewsets.ModelViewSet):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

class AdmissionDetailView(generics.RetrieveUpdateAPIView):
    queryset = Admission.objects.all()
    serializer_class = AdmissionSerializer

@csrf_exempt
def admitir_paciente(request):
    if request.method != "POST":
        return JsonResponse({"error": "Método no permitido"}, status=405)

    try:
        data = json.loads(request.body)  # Si usas API con JSON
    except json.JSONDecodeError:
        return JsonResponse({"error": "Formato JSON inválido"}, status=400)

    # Buscar una cama disponible
    cama_disponible = Cama.objects.filter(estado='disponible').first()

    if not cama_disponible:
        return JsonResponse({"error": "No hay camas disponibles"}, status=400)

    # Extraer datos de la request
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    age = data.get("age")
    blood_type = data.get("blood_type")
    reason = data.get("reason")
    status = data.get("status", "Autorizado")  # Si no se envía, por defecto "Autorizado"

    # Validación básica
    if not all([first_name, last_name, age, blood_type, reason]):
        return JsonResponse({"error": "Faltan datos obligatorios"}, status=400)

    # Crear la admisión con los datos recibidos
    nueva_admision = Admission.objects.create(
        cama=cama_disponible,
        first_name=first_name,
        last_name=last_name,
        age=age,
        blood_type=blood_type,
        reason=reason,
        status=status
    )

    # Marcar la cama como ocupada
    cama_disponible.estado = 'ocupada'
    cama_disponible.save()

    return JsonResponse({
        "message": "Paciente admitido correctamente",
        "id": nueva_admision.id
    })
