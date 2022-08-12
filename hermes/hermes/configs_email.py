from datetime import date
from ..cotacao.models import Consulta
from ..mensageiro.models import Usuario
from django.core.mail import send_mass_mail

import urllib, json

def cotacao_ativo(ativo):
    url = f'https://www.okanebox.com.br/api/acoes/ultima/{ativo}/'
    r = urllib.request.urlopen(url)
    dados = json.loads(r.read())
    preco_atual = float(dict(dados)['PREULT'])
    nova_consulta = Consulta(ativo=ativo, preco=preco_atual, data=date.today())
    nova_consulta.save()
    return float(preco_atual)

def envia_email_compra(ativo_monitorado, valor_ativo):
    mensagem = f'Compra recomentada: {ativo_monitorado} \nValor atual: R$ {valor_ativo}\nValor de compra definido: R$ {ativo_monitorado.preco_venda}'
    assunto = "Compra de ativo"
    lista_emails = list()
    for usuario in Usuario.objects.all():
        if usuario.status:
            lista_emails.append(usuario.email)
    tupla_dados = tuple(assunto, mensagem, 'Sistema Hermes', lista_emails)
    send_mass_mail(tupla_dados)

def envia_email_venda(ativo_monitorado, valor_ativo):
    mensagem = f'venda recomentada: {ativo_monitorado} \nValor atual: R$ {valor_ativo}\nValor de venda definido: R$ {ativo_monitorado.preco_venda}'
    assunto = "Venda de ativo"
    lista_emails = list()
    for usuario in Usuario.objects.all():
        lista_emails.append(usuario.email)
    tupla_dados = tuple(assunto, mensagem, 'Sistema Hermes', lista_emails)
    send_mass_mail(tupla_dados)

def compra_recomendada(ativo_monitorado):
    preco_atual = cotacao_ativo(ativo_monitorado)
    if ativo_monitorado.preco_compra >= preco_atual:
        return True
    else:
        return False

def venda_recomendada(ativo_monitorado):
    preco_atual = cotacao_ativo(ativo_monitorado)
    if ativo_monitorado.preco_venda <= preco_atual:
        return True
    else:
        return False
