from django.db import models


# Create your models here.
class Amigo(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=100, blank=False)
    sugestao_presente = models.TextField(blank=True)

