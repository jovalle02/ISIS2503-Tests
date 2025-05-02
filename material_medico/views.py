from django.views.generic import ListView
from .models import MaterialMedico

class MaterialMedicoListView(ListView):
    model = MaterialMedico
    template_name = 'material_medico/list.html'