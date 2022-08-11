from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from django.conf import settings

def index(request):
    return HttpResponse('Início dos emails')

def configuracao(request):
    return HttpResponse('Configuração do email')

def teste_envio(request):
    send_mail(
        subject='Teste',
        message='Queria decorar o Lorem Ipsum',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=['ilanrochaaraujo@gmail.com'],
        fail_silently=False,
    )

    return HttpResponse('')
