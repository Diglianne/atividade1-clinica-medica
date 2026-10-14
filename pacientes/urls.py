from django.urls import path
from pacientes import views

urlpatterns = [
    path('', views.listarPacientes, name='listagem_pacientes'),
    path('adicionar/', views.adicionarPaciente, name='adicionar_paciente'),
    path('editar/<int:id>/', views.editarPaciente, name='editar_paciente'),
    path('deletar/<int:id>/', views.deletarPaciente, name='deletar_paciente'),
]
