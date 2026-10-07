from django.urls import path

from estudantes import views

urlpatterns = [
    path ('', views.listarEstudantes, name= 'listagem'),
    path ('editar/<id>', views.editarEstudantes, name='editar'),
    path ('adicionar/', views.adicionarEstudante, name= 'adicionar'),
    path ('deletar/<id>', views.deletarEstudante, name= 'deletar')
  ]