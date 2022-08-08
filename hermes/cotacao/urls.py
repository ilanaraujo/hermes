from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testejson', views.testejson, name='testejson'),
    path('armazena_dados_csv', views.armazena_dados_csv),
    path('lista', views.lista, name='lista'),
    path('obter_cotacao/<int:id_ativo>', views.obter_cotacao, name='obter_cotacao')
]