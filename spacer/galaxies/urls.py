from django.urls import path
from galaxies import views

app_name = 'galaxies'

url_patterns = [
    path('', views.ListGalaxies.as_view(), name='all'),
    path('new/', views.CreateGalaxy.as_view(), name='create'),
    path('posts/in/<slug>/', views.SingleGalaxy.as_view(), name='single',)
]
