from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista_usuarios', views.lista, name='lista_usuarios'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('altera_status/<int:id_usuario>', views.altera_status, name='altera_status')
]