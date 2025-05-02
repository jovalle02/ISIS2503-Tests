from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from materiales.models import MaterialMedicoReservable

@csrf_exempt
def reservar_material(request):
    material = MaterialMedicoReservable.objects.filter(estado='disponible').first()

    if material:
        material.estado = 'reservado'
        material.save()
        return JsonResponse({'mensaje': f'{material.nombre} ha sido reservado con éxito.'})
    else:
        return JsonResponse({'mensaje': 'No hay material médico disponible.'}, status=404)
