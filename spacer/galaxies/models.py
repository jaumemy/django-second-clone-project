from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.conf import settings

import misaka

from django.contrib.auth import get_user_model
User = get_user_model()

from django import template
register = template.Library()

# Create your models here.


class Galaxy(models.Model):
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(blank=True, default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through="GalaxyMember")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("galaxies:single", kwargs={"slug":self.slug})

    class Meta:
        ordering = ["name"]




class GalaxyMember(models.Model):
    galaxy = models.ForeignKey(Galaxy,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_galaxies',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('galaxy','user')
