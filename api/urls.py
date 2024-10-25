from django.urls import path
from . import views

urlpatterns = [
    path('', views.instrucoes,name='comprimentos'),
    path('dados', views.buscaDados,name='dados'),
    
]