from django.urls import path
from . import views

urlpatterns = [
    path('', views.exibir_usuarios, name='exibir_usuarios'),
    path('api/usuarios', views.usuario_busca, name='usuario_busca'),
]
