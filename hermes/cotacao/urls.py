from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('testejson', views.testejson, name='testejson'),
    path('armazena_dados_csv', views.armazena_dados_csv)
]