from django.shortcuts import render
from django.http import HttpResponse
from mascota.forms import MascotaFormulario, VacunaFormulario
from mascota.models import Mascota,Vacuna
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin

from mascota.utils import render_to_pdf_Mascota


# Create your views here.

class ListadeMascotaPDF(ListView):
	
    def get(self, request, *args, **kwargs):
        mascotas = Mascota.objects.all()
        data = {
            'mascotas': mascotas
        }
        pdf = render_to_pdf_Mascota('mascota/mascotaListapdf.html',data)
        return HttpResponse(pdf, content_type='application/pdf')

def home (request):
    return render(request,'base/home.html')

class MascotaList(ListView):
    model = Mascota
    template_name = 'mascota/mascotaLista.html'
    paginate_by = 5    
    ordering = ['id']

class MascotaListInvitado(ListView):
    model = Mascota
    template_name = 'mascota/mascotaListainvitado.html'
    paginate_by = 5    
    ordering = ['id']

class MascotaCreate(PermissionRequiredMixin,CreateView):
    model = Mascota
    form_class = MascotaFormulario
    template_name = 'mascota/mascota_formulario.html'
    success_url = reverse_lazy('mascota_lista')
    permission_required = 'mascota.add_mascota'

class MascotaUpdate(PermissionRequiredMixin, UpdateView):
    model = Mascota
    form_class = MascotaFormulario
    template_name = 'mascota/mascota_formulario.html'
    success_url = reverse_lazy('mascota_lista')
    permission_required = 'mascota.change_mascota'

class MascotaDelete(PermissionRequiredMixin,DeleteView):
    model = Mascota
    template_name = 'mascota/mascotaDelete.html'
    success_url = reverse_lazy('mascota_lista')
    permission_required = 'mascota.delete_mascota'

class VacunaCreate(CreateView):
    model = Vacuna
    form_class = VacunaFormulario
    template_name = 'mascota/vacuna_formulario.html'
    success_url = reverse_lazy('mascota_lista')