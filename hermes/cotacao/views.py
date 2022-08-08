from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Ativo, AtivoMonitorado, Consulta, Empresa
from datetime import date

import urllib, json

def index(request):
    return HttpResponse("Pagina de cotacoes.")

def testejson(request):
    # Exemplo pra testar api
    url = 'https://www.okanebox.com.br/api/acoes/hist/PETR4/20220803/20220804/'
    r = urllib.request.urlopen(url)
    data = json.loads(r.read())
    aurelio = dict(data) # Usando dicionnário para melhor extração dos dados
    return HttpResponse(aurelio)

def connfiguracao(request):
    # ativos = Ativo.objects.all()    
    return HttpResponse("Página de connfigurações")

def armazena_dados_csv(request):
    return redirect('index')

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
    ativos = Ativo.objects.all()
    lista_ativos_empresas = list()
    for ativo in ativos:
        empresa_correspondente = ativo.empresa
        lista_ativos_empresas.append([ativo, empresa_correspondente])

    informacoes = {
        'ativos' : ativos
    }
    return render(request, 'cotacao/lista.html', informacoes)

def obter_cotacao(request, id_ativo):
    ativo = Ativo.objects.get(id=id_ativo)
    url = f'https://www.okanebox.com.br/api/acoes/ultima/{ativo}/'
    r = urllib.request.urlopen(url)
    dados = json.loads(r.read())
    informacoes = dict(dados)
    informacoes['ativo'] = ativo
    data = date.today()
    preco = float(informacoes['PREULT'])
    nova_consulta = Consulta(ativo=ativo, preco=preco, data=data)
    nova_consulta.save()
    return render(request, 'cotacao/obter_cotacao.html', informacoes)