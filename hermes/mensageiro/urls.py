from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teste', views.teste_envio, name='teste_envio')
]