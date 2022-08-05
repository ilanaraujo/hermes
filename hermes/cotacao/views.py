from django.shortcuts import render
from django.http import HttpResponse

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
