import random

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from amigos.models import Amigo
import random
# Create your views here.


def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['senha']
        senhaConfirmacao = request.POST['senhaConfirmacao']

        if not nome.strip():
            return redirect('cadastro')

        if not email.strip():
            return redirect('cadastro')

        if senha != senhaConfirmacao:
            return redirect('cadastro')

        if User.objects.filter(email=email).exists():  # Verificando se o usuarios ja existe
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        return redirect('login')

    return render(request, 'usuarios/cadastro.html')


def login(request):
    if request.method == 'POST':  # Olhe a pagina login.html  27:   <form action="{%  url 'login' %}" method="POST">
        email = request.POST['email']  # ['email'] == campo name=`email` da tag <input>
        senha = request.POST['senha']
        if campo_vazio(email) or campo_vazio(senha):
            # messages.error(request, 'O campo email e senha nao pode ser vazio')
            return redirect('login')

        if User.objects.filter(email=email).exists():  # Verificando se o email existe na base de dados
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()  # pegando o username

            user = auth.authenticate(request, username=nome, password=senha)  # autenticando o usuario

            if user is not None:
                auth.login(request, user)
                print('login Sucesso')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')


def dashboard(request):
    if request.user.is_authenticated:
        amigos = Amigo.objects.filter(usuario=request.user.id)

        dados = {
            'amigos': amigos
        }
        return render(request, 'usuarios/dashboard.html', dados)
    else:
        return redirect('index')


def cadastrar_amigo(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        telefone = request.POST['telefone']
        sujestao = request.POST['sujestao']

        randomico = random.randint(1, 12)
        local = 'http://127.0.0.1:8000/static/img/bg-img/nfts/' + str(randomico) + '.jpg'

        user = get_object_or_404(User, pk=request.user.id)
        amigo = Amigo.objects.create(usuario=user, nome=nome, telefone=telefone, email=email,
                                     sugestao_presente=sujestao, foto_amigo=local)
        amigo.save()
        return redirect('dashboard')

    return render(request, 'usuarios/cadastrar_amigo.html')

def campo_vazio(campo):
    return not campo.strip()
