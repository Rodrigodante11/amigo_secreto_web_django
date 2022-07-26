from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:amigo_id>', views.detail, name='detail'),
    path('busca', views.buscar, name='buscar'),
    path('detail/excluir_amigo', views.excluir_amigo, name='excluir_amigo'),
]
