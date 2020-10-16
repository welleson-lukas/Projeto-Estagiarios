from django.urls import path
from estagiario import views
from estagiario.views import *

urlpatterns = [
    path('', views.EstagiarioIndex.as_view(), name='index'),
    path('inativos/', views.EstagiarioInativos.as_view(), name='inativos'),
    path('cadastrar_estagiario/', cadastrar_estagiario, name='cadastrar_estagiario'),
    path('editar_estagiario/<int:id>', editar_estagiario, name='editar_estagiario'),
    path('<int:estagiario_id>', exibir_estagiario, name='exibir_estagiario'),
]