from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Ativo, Empresa

import urllib, json

def index(request):
    return HttpResponse("Pagina de cotacoes.")

def testejson(request):
    # Exemplo pra testar api
    url = 'https://www.okanebox.com.br/api/acoes/hist/PETR4/20220803/20220804/'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read())
    aurelio = dict(data)
    return HttpResponse(aurelio)

def armazena_dados_csv(request):
    #return redirect('index')

    # Código utilizado para inserir as empresas e ativos no banco de dados
    from .lista_empresas_ativos import lista_ativos, lista_empresas

    for string_completa in lista_empresas:
        string_separada = string_completa.split(',')
        nome_empresa = string_separada[1]
        cod_empresa = string_separada[2]
        nova_empresa = Empresa(nome=nome_empresa, codigo=cod_empresa) 
        nova_empresa.save()
    
    for string_completa in lista_ativos:
        string_separada = string_completa.split(',')
        codigo_ativo = string_separada[1]
        empresa = Empresa.objects.filter(codigo=codigo_ativo[:4]).first()
        novo_ativo = Ativo(codigo=codigo_ativo, empresa=empresa)
        novo_ativo.save()

    return redirect('index')

def lista(request):
    return 0