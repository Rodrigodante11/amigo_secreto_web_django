import random

from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Amigo


# 'teste': "{% static '/img/bg-img/nfts/1.jpg' %}",
# Create your views here.
def index(request):
    dados = {
        'amigos': Amigo.objects.all(),

    }
    return render(request, 'amigos/index.html', dados)


def detail(request, amigo_id):
    amigo = get_object_or_404(Amigo, pk=amigo_id)

    amigo_a_exibir = {
        'amigo': amigo
    }
    return render(request, 'amigos/detail.html', amigo_a_exibir)


def buscar(request):

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if buscar:
            amigos = Amigo.objects.filter(nome__icontains=nome_a_buscar)

    dados = {
        'amigos': amigos
    }
    return render(request, 'amigos/buscar.html', dados)

