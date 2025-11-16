from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('lista/', views.lista, name='lista'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]