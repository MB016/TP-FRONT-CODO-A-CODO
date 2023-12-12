from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Creador

# Create your views here.


class CreadorBaseView(View):
    template_name = 'Creador.html'
    model = Creador
    fields = '__all__'
    success_url = reverse_lazy('Creador:all')


class CreadorListView(CreadorBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LOS Creador
    """

class CreadorDetailView(CreadorBaseView,DetailView):
    template_name = "Creador_detail.html"

class CreadorCreateView(CreadorBaseView,CreateView):
    template_name = "Creador_create.html"
    extra_context = {
        "tipo": "Crear Creador"
    }


class CreadorUpdateView(CreadorBaseView,UpdateView):
    template_name = "Creador_create.html"
    extra_context = {
        "tipo": "Actualizar Creador"
    }

class CreadorDeleteView(CreadorBaseView,DeleteView):
    template_name = "Creador_delete.html"
    extra_context = {
        "tipo": "Borrar Creador"
    }
