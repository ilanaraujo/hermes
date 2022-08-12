from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from celery import Celery

from cotacao.models import AtivoMonitorado
from datetime import datetime, timedelta

from .configs_email import *

celery = Celery('tasks', broker='redis://127.0.0.1:6379')

@shared_task
def envia_emails():
    ativos_monitorados = AtivoMonitorado.objejcts.all()
    ativos_para_compra = list()
    ativos_para_venda = list()

    # 
    for ativo in ativos_monitorados:
        ultima_consulta_ativo = Consulta.objects.filter(ativo=ativo).last()
        if date.today() >= ultima_consulta_ativo.data + timedelta(days=ativo.intervalo_consulta):
            if compra_recomendada(ativo):
                ativos_para_compra.append(ativo)

            if venda_recomendada(ativo):
                ativos_para_venda.append(ativo)

    if ativos_para_compra:
        for ativo in ativos_para_compra:
            envia_email_compra(ativo, cotacao_ativo(ativo)) 

    if ativos_para_venda:
        for ativo in ativos_para_venda:
            envia_email_venda(ativo, cotacao_ativo(ativo))