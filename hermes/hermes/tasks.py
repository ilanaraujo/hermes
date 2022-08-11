from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from celery import Celery

from cotacao.models import AtivoMonitorado
from datetime import datetime

celery = Celery('tasks', broker='redis://127.0.0.1:6379')

@shared_task
def envia_email():
    subject = 'Teste do envio agendado'
    hoje = datetime.today().time()
    message = f'Boa noite Marcelo, são {hoje}'
    email_from = "Hermes Automatico"
    recipient_list = ['ilanrochaaraujo@gmail.com']
    send_mail( subject, message, email_from, recipient_list )
    print('Email enviado')