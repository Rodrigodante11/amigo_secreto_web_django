from django.db import models
from usuarios.models import Usuario


# Create your models here.
class Amigo(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    sugestao_presente = models.TextField(blank=True)
    # sala = models.CharField(max_length=50)

