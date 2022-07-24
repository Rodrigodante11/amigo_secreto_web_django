from django.contrib import admin

from .models import Usuario


class ListandoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'nome')  # aparecer o nome e o ID na tela de listagem
    list_display_links = ('nome',)  # Opcao de editar ao clicar no nome
    search_fields = ('nome',)  # colocando um filtro
    list_per_page = 10  # limitando q quantidade dos dados da pagina


admin.site.register(Usuario, ListandoUsuarios)
