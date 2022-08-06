import pandas as pd
from .models import Ativo, Empresa

PATH_ATIVOS = 'ativos.csv'
PATH_EMPRESAS = 'empresas_codigo.csv'

df_empresas = pd.read_csv(PATH_EMPRESAS)
df_ativos = pd.read_csv(PATH_ATIVOS)

def armazena_empresas(df_empresas):
    if not Ativo.objects.get(id=0):
        for i in df_empresas.index:
            nome = df_empresas.iloc[i,0]
            cod_bolsa = df_empresas.iloc[i,1]
            nova_empresa = Empresa(nome=nome, codigo=cod_bolsa)
            nova_empresa.save()

def armazena_ativos(df_ativos):
    if not Ativo.objects.get(id=0):
        for i in df_ativos.index:
            codigo = df_ativos.iloc[i,0]
            empresa = Empresa.objects.get(codigo=codigo[:4])
            ativo = Ativo(codigo=codigo, empresa=empresa.id)
            ativo.save()