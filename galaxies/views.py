from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from galaxies.models import Galaxy, GalaxyMember
from django.contrib import messages
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.

class CreateGalaxy(LoginRequiredMixin, generic.CreateView):
    fields = ('name','description')
    model = Galaxy


class SingleGalaxy(generic.DetailView):
    model = Galaxy


class ListGalaxies(generic.ListView):
    model = Galaxy


class JoinGalaxy(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self,*args,**kwargs):
        return reverse("galaxies:single", kwargs={"slug":self.kwargs.get("slug")})

    def get(self,request,*args,**kwargs):
        galaxy = get_object_or_404(Galaxy, slug=self.kwargs.get("slug"))

        try:
            GalaxyMember.objects.create(user=self.request.user,galaxy=galaxy)

        except IntegrityError:
            messages.warning(self.request,f"You are already a member of {galaxy.name} galaxy")

        else:
            messages.success(self.request,f"You are now a member of {galaxy.name} galaxy")

        return super().get(request,*args,**kwargs)


class LeaveGalaxy(LoginRequiredMixin,generic.RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse("galaxies:single",kwargs={"slug": self.kwargs.get("slug")})

    def get(self, request, *args, **kwargs):
        try:
            membership = models.GalaxyMember.objects.filter(
                user=self.request.user,
                galaxy__slug=self.kwargs.get("slug")
            ).get()

        except models.GalaxyMember.DoesNotExist:
            messages.warning(
                self.request,
                "You can't leave this group because you aren't in it."
            )

        else:
            membership.delete()
            messages.success(
                self.request,
                "You have successfully left this galaxy."
            )
        return super().get(request, *args, **kwargs)
