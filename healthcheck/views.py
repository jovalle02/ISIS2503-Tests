from django.http import JsonResponse
from django.db import connections, OperationalError


def health_check(request):
    """
    Devuelve el estado de salud de la aplicación:
      - Conexión a la base de datos
    """
    status_checks = {
        'database': 'unknown',
    }

    # Verificar conexión a la base de datos
    try:
        connections['default'].cursor()
        status_checks['database'] = 'ok'
    except OperationalError:
        status_checks['database'] = 'error'

    # Estado general
    overall_status = 'ok' if all(v == 'ok' for v in status_checks.values()) else 'error'

    payload = {
        'status': overall_status,
        'checks': status_checks,
    }
    return JsonResponse(payload, status=200 if overall_status == 'ok' else 503)
