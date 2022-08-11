from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('armazena_dados_csv', views.armazena_dados_csv),
    path('lista', views.lista, name='lista'),
    path('listamonitorados', views.lista_monitorados, name="lista_monitorados"),
    path('obter_cotacao/<int:id_ativo>', views.obter_cotacao, name='obter_cotacao')
]