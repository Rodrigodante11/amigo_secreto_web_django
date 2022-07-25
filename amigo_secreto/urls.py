

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('usuarios/', include('usuarios.urls')),
    path('', include('amigos.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # avisando q as rotas podem usar imagens e statics
# sem ele nao eh possivel adicionar fotos e exibir no front
