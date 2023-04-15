from django.urls import path
from .import views

urlpatterns = [
    
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.login, name='login'),
    path('logout/', views.lougout_user, name='lougout_user'),
]