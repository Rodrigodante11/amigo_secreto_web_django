from django.contrib import admin

# Register your models here.
from .models import Amigo


class ListandoAmigos(admin.ModelAdmin):
    list_display = ('id', 'nome')  # aparecer o nome e o ID na tela de listagem
    list_display_links = ('nome',)  # Opcao de editar ao clicar no nome
    search_fields = ('nome',)  # colocando um filtro
    list_per_page = 10  # limitando q quantidade dos dados da pagina


admin.site.register(Amigo, ListandoAmigos)

# Username (leave blank to use 'rodrigo'):
# Email address: rodrigo@gmail.com
# Password: 12345678
