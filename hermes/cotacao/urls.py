from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('armazena_dados_csv', views.armazena_dados_csv),
    path('lista', views.lista, name='lista'),
    path('listamonitorados', views.lista_monitorados, name="lista_monitorados"),
    path('obter_cotacao/<int:id_ativo>', views.consulta, name='obter_cotacao'),
    path('configuracao/<int:id_ativo>', views.configuracao, name='configuracao'),
    path('lista_consultas', views.lista_consultas, name="lista_consultas"),
    path('lista_monitorados', views.lista_monitorados, name="lista_monitorados")
]