from django.contrib import admin
from galaxies import models

# Register your models here.

class GalaxyMemberInline(admin.TabularInline):
    model = models.GalaxyMember

admin.site.register(models.Galaxy)
