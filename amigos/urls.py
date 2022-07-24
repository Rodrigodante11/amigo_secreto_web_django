from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrar_amigo', views.cadastrar_amigo, name='cadastrar_amigo'),
    path('detail/<int:amigo_id>', views.detail, name='detail'),

]
