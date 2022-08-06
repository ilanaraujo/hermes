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
    from .armazena_dados_csv import df_ativos, df_empresas, armazena_ativos, armazena_empresas
    armazena_ativos(df_ativos)
    armazena_empresas(df_empresas)
    return redirect('index')

def lista(request):
    return 0