from django.shortcuts import render, get_object_or_404, get_list_or_404
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
    amigo = get_object_or_404(Amigo, pk=amigo_id)

    amigo_a_exibir = {
        'amigo': amigo
    }
    return render(request, 'amigos/detail.html', amigo_a_exibir)
