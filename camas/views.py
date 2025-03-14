from django.http import JsonResponse
from .models import Cama

def obtener_camas_disponibles(request):
    camas_disponibles = Cama.objects.filter(estado='disponible').count()
    return JsonResponse({'camas_disponibles': camas_disponibles})
