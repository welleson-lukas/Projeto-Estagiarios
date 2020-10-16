from django.urls import path
from administracao import views
from administracao.views import *

urlpatterns = [
    path('', views.painel, name='painel')
]