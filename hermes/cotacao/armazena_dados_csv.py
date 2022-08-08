from .models import Ativo, Empresa

def armazena_empresas(lista):
    for string_completa in lista:
        string_separada = string_completa.split(',')
        nome_empresa = string_separada[1]
        cod_empresa = string_separada[2]
        nova_empresa = Empresa(nome=nome_empresa, codigo=cod_empresa) 
        nova_empresa.save()

def armazena_ativos(lista):
    for string_completa in lista:
        string_separada = string_completa.split(',')
        codigo_ativo = string_separada[1]
        empresa = Empresa.objects.filter(codigo=codigo_ativo[:4]).first
        novo_ativo = Ativo(codigo=codigo_ativo, empresa=empresa)
