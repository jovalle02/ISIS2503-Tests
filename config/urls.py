from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from admissions.views import AdmissionViewSet
from admissions.views import admitir_paciente
from camas.views import obtener_camas_disponibles
from healthcheck.views import health_check

router = DefaultRouter()
router.register(r'admissions', AdmissionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('admitir/', admitir_paciente, name='admitir_paciente'),
    path('disponibles/', obtener_camas_disponibles, name='camas_disponibles'),
    path('health/', health_check, name='health_check'),
    path('material-medico/', include('material_medico.urls')),
]
