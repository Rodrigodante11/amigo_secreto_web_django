from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'amigos/index.html')


def cadastrar_amigo(request):
    return render(request, 'amigos/cadastrar_amigo.html')


def detail(request):
    return render(request, 'amigos/detail.html')
