from django.urls import path
from .views import MaterialMedicoListView

urlpatterns = [
    path('', MaterialMedicoListView.as_view(), name='material_medico_list'),
]