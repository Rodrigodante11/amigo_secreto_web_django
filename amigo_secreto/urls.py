from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('usuarios', include('usuarios.urls')),
    path('', include('amigos.urls')),
    path('admin/', admin.site.urls),
]
