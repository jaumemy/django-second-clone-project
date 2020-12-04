from django.urls import path
from . import views

app_name = 'galaxies'

urlpatterns = [
    path('', views.ListGalaxies.as_view(), name='all'),
    path('new/', views.CreateGalaxy.as_view(), name='create'),
    path('posts/in/<slug>/', views.SingleGalaxy.as_view(), name='single'),
    path('join/<slug>/', views.JoinGalaxy.as_view(), name='join'),
    path('leave/<slug>/', views.LeaveGalaxy.as_view(), name='leave'),
]
