from django.shortcuts import render, redirect
from django.contrib.auth.models import User
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
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
    return render(request, 'usuarios/login.html')


def logout(request):
    return render(request, 'usuarios/login.html')


def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
