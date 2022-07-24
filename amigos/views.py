from django.shortcuts import render
from .models import Amigo


# Create your views here.
def index(request):
    dados = {
        'amigos': Amigo.objects.all()
    }
    return render(request, 'amigos/index.html', dados)


def cadastrar_amigo(request):
    return render(request, 'amigos/cadastrar_amigo.html')


def detail(request, amigo_id):
    return render(request, 'amigos/detail.html')
