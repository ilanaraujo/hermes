from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from django.conf import settings

def index(request):
    return HttpResponse('Início dos emails')

def configuracao(request):
    return HttpResponse('Configuração do email')

def teste_envio(request):

    aux_var = 23
    send_mail(
        subject='Teste',
        message=f'Queria decorar o Lorem Ipsum.\nLorem Ipsum {aux_var}',
        from_email="Hermes B3 Django",
        recipient_list=['ilanrochaaraujo@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('')
