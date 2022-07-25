from django.db import models
from usuarios.models import Usuario
from django.contrib.auth.models import User


# Create your models here.
class Amigo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    sugestao_presente = models.TextField(blank=True)
    foto_amigo = models.CharField(max_length=200, blank=True)

    def getTelefone(self):
        return "("+self.telefone[0:2]+") "+self.telefone[2:7]+"-"+self.telefone[7:11]

    def getNome(self):
        return self.nome.title()