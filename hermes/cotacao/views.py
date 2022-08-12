from os import stat
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Ativo, AtivoMonitorado, Consulta, Empresa
from datetime import date

import urllib, json

from .forms import FormMonitoramento

def index(request):
    informações = { 'titulo_pagina' : 'Index Cotacão'}
    return render(request, 'cotacao/index.html', informações)

def configuracao(request, id_ativo):
    ativo = Ativo.objects.get(id=id_ativo)
    # Caso alterações tenham sido feitas
    if request.method == 'POST':
        # Recupera informações do formulário
        form = FormMonitoramento(request.POST)
        if form.is_valid():
            print('é valido')
            preco_venda = form.cleaned_data['preco_venda']
            preco_compra = form.cleaned_data['preco_compra']
            intervalo_consulta = form.cleaned_data['intervalo_consulta']
            monitoramento = form.cleaned_data['monitoramento']  

            # Se o ativo já estiver sendo monitorado previamente
            if ativo.e_monitorado():
                ativo_monitorado = AtivoMonitorado.objects.get(ativo=ativo) 
            
                # Alterações nas informações do ativo monitorado
                if monitoramento:
                    ativo_monitorado.preco_compra = preco_compra
                    ativo_monitorado.preco_venda = preco_venda
                    ativo_monitorado.intervalo_consulta = intervalo_consulta
                    ativo_monitorado.save()
            
                # Ativo deixou de ser monitorado
                else:
                    ativo_monitorado.delete()
        
            # Ativo não está sendo monitorado
            else:
                # Salva o ativo monitorado
                if monitoramento:
                    ativo_monitorado = AtivoMonitorado(
                        ativo=ativo,
                        preco_compra=preco_compra,
                        preco_venda=preco_venda, 
                        intervalo_consulta = intervalo_consulta
                    )
                    ativo_monitorado.save()
                
                # Não faz nada
                else:
                    pass
        
        return redirect('lista') # Retorna para a lista de ativos
    
    # Carrega a página
    else:
        informacoes = dict()
        informacoes['titulo_pagina'] = 'config'
        informacoes['form'] = FormMonitoramento()
        informacoes['ativo'] = Ativo.objects.get(id=id_ativo)
        return render(request, 'cotacao/configuracao.html', informacoes)

def armazena_dados_csv(request):
    # Utilizada previamente para inserir ativos e empresas no banco de dados
    # Mantida para caso seja necessário incluir novamente os objetos
    return redirect('index')

    # Código utilizado para inserir as empresas e ativos no banco de dados
    from .lista_empresas_ativos import lista_ativos, lista_empresas

    # Inserindo as empresas no banco
    for string_completa in lista_empresas:
        string_separada = string_completa.split(',')
        nome_empresa = string_separada[1]
        cod_empresa = string_separada[2]
        nova_empresa = Empresa(nome=nome_empresa, codigo=cod_empresa) 
        nova_empresa.save()
    
    # Inserindo os ativos
    for string_completa in lista_ativos:
        string_separada = string_completa.split(',')
        codigo_ativo = string_separada[1]
        empresa = Empresa.objects.filter(codigo=codigo_ativo[:4]).first()
        novo_ativo = Ativo(codigo=codigo_ativo, empresa=empresa)
        novo_ativo.save()

    return redirect('index')

# Lista de todos os ativos
def lista(request):
    ativos = Ativo.objects.all()
    status_ativos = list()
    status_ativos.append(False)
    for ativo in ativos:
        status_ativos.append(ativo.e_monitorado())
    print(status_ativos)
    informacoes = {
        'ativos' : ativos,
        'ativo_e_monitorado' : status_ativos,
        'titulo_pagina' : "Ativos"
    }
    return render(request, 'cotacao/lista.html', informacoes)

def lista_monitorados(request):
    ativos_monitorados = AtivoMonitorado.objects.all()
    informacoes = { 'ativos' : ativos_monitorados}
    informacoes['titulo_pagina'] = 'Ativos Monitorados'

    for i in ativos_monitorados:
        print(i.ativo)
    return render(request, 'cotacao/lista_monitorados.html', informacoes)

# Obtem a cotação atual de um ativo
def consulta(request, id_ativo):
    ativo = Ativo.objects.get(id=id_ativo)

    # Busca na API
    url = f'https://www.okanebox.com.br/api/acoes/ultima/{ativo}/' # API
    r = urllib.request.urlopen(url)
    dados = json.loads(r.read())
    informacoes = dict(dados) # Dicionário com informações obtidas na API
    informacoes['ativo'] = ativo
    informacoes['titulo_pagina'] = 'Cotação do Ativo'
    data = date.today()
    preco = float(informacoes['PREULT'])

    # Armazena a nova consulta
    nova_consulta = Consulta(ativo=ativo, preco=preco, data=data)
    nova_consulta.save()

    # Exibe as informações da cosulta na página
    return render(request, 'cotacao/consulta.html', informacoes)

# Exibe todas as consultas realizadas
def lista_consultas(request):
    consultas = Consulta.objects.all()
    informacoes = dict()
    informacoes['consultas'] = consultas
    informacoes['titulo_pagina'] = 'Lista de Consultas'
    return render(request, 'cotacao/lista_consultas.html', informacoes)