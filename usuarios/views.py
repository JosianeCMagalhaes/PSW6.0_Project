from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth
def cadastro(request):
    if request.method == "GET":
        return render(request,'cadastro.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        print(username, email, senha, confirmar_senha)
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'as senhas não coincidem')
            return redirect(reverse('cadastro'))
        user=User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR,'Usuario já existe')
            return redirect(reverse('cadastro'))
        user = User.objects.create_user(username=username,email=email,password=senha)
        messages.add_message(request,constants.SUCCESS,'Usuário salvo com sucesso')
        return redirect(reverse('login'))
def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        user = auth.authenticate(username=username,password= senha)
        if not user:
            #TODO:validar força da senha
            messages.add_message(request,constants.ERROR,'Username ou senha invalidos')
            return redirect(reverse('login'))
        
        auth.login(request,user)
        return redirect('/eventos/novo_evento/')

