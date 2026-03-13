from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('perfil/', views.perfil_view, name='perfil'),
    path('editar/', views.editar_view, name='editar'),
]