from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from adopcion.models import Persona, Solicitud
from adopcion.forms import PersonaFormulario, SolicitudFormulario
from django.contrib.auth.mixins import PermissionRequiredMixin



# Create your views here.
class SolicitudList(PermissionRequiredMixin,ListView):
    model = Solicitud
    template_name='adopcion/solicitud_lista.html'
    ordering = ['pk']
    permission_required = 'adopcion.view_solicitud'



class SolicitudCreate(CreateView):
	model = Solicitud
	template_name = 'adopcion/solicitud_formulario.html'
	form_class = SolicitudFormulario
	second_form_class = PersonaFormulario
	success_url = reverse_lazy('home')

	def get_context_data(self, **kwargs):
		context = super(SolicitudCreate, self).get_context_data(**kwargs)
		if 'form' not in context:
			context['form'] = self.form_class(self.request.GET)
		if 'form2' not in context:
			context['form2'] = self.second_form_class(self.request.GET)
		return context

	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		form = self.form_class(request.POST)
		form2 = self.second_form_class(request.POST)
		if form.is_valid() and form2.is_valid():
			solicitud = form.save(commit=False)
			solicitud.persona = form2.save()
			solicitud.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form, form2=form2))

class SolicitudUpdate(PermissionRequiredMixin,UpdateView):
	model = Solicitud
	second_model = Persona
	template_name = 'adopcion/solicitud_formulario.html'
	form_class = SolicitudFormulario
	second_form_class = PersonaFormulario
	success_url = reverse_lazy('solicitud_listado')
	permission_required = 'adopcion.change_solicitud'


	def get_context_data(self, **kwargs):
			context = super(SolicitudUpdate, self).get_context_data(**kwargs)
			pk = self.kwargs.get('pk', 0)
			solicitud = self.model.objects.get(id=pk)
			persona = self.second_model.objects.get(id=solicitud.persona_id)
			if 'form' not in context:
				context['form'] = self.form_class()
			if 'form2' not in context:
				context['form2'] = self.second_form_class(instance=persona)
			context['id'] = pk
			return context
	
	def post(self, request, *args, **kwargs):
		self.object = self.get_object
		id_solicitud = kwargs['pk']
		solicitud = self.model.objects.get(id=id_solicitud)
		persona = self.second_model.objects.get(id=solicitud.persona_id)
		form = self.form_class(request.POST, instance=solicitud)
		form2 = self.second_form_class(request.POST, instance=persona)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
			return HttpResponseRedirect(self.get_success_url())
		else:
			return HttpResponseRedirect(self.get_success_url())

class SolicitudDelete(DeleteView):
	model = Solicitud
	template_name = 'adopcion/solicitudDelete.html'
	success_url = reverse_lazy('solicitud_listado')
	permission_required = 'adopcion.delete_solicitud'



