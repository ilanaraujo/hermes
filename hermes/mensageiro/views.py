from re import I
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail

from django.conf import settings

from .models import Usuario
from .form import FormUsuario
def index(request):
    informacoes = { 'titulo_pagina' : 'Mensageiro'}
    return render(request, 'mensageiro/index.html')

# Cadastro de novos usuários
def cadastro(request):
    if request.method == 'POST':
        # Recupera informações do formulário
        form = FormUsuario(request.POST)
        if form.is_valid():
            print('é valido')
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']

            usuario = Usuario(nome=nome, email=email)
            usuario.save()
            return redirect('lista_usuarios')
    else:
        informacoes = { 'titulo_pagina' : 'Cadastro'}
        informacoes['form'] = FormUsuario()
        return render(request, 'mensageiro/cadastro.html', informacoes)

def lista(request):
    usuarios = Usuario.objects.all()
    informacoes = {
        'titulo_pagina' : 'Lista de Usuários',
        'usuarios' : usuarios
    }
    return render(request, 'mensageiro/lista.html', informacoes)

def altera_status(request, id_usuario):
    usuario = Usuario.objects.filter(id=id_usuario).first()
    if usuario:
        usuario.status = not(usuario.status)
        usuario.save()
    return redirect('lista_usuarios')

