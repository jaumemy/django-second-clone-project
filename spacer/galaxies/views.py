from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from galaxies.models import Galaxy, GalaxyMember

# Create your views here.

class CreateGalaxy(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description')
    model = Galaxy

class SingleGalaxy(generic.DetailView):
    model = Galaxy

class ListGalaxies(generic.ListView):
    model = Galaxy
