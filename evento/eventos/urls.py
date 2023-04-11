
from django.urls import path
from . import views

urlpatterns = [
    
    path('novo_evento/', views.novo_cadastro, name='novo_evento'),
    
]