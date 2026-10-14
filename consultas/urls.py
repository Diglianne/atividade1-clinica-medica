from django.urls import path
from consultas import views
# Trocamos 'estudantes' por 'pacientes' para o Django achar o caminho certo!
from pacientes import views as pacViews

urlpatterns = [
    # Dashboard Principal
    path('', views.dashboard, name='dashboard'),
    
    # Médicos
    path('medicos/', views.listarMedicos, name='medico_listar'),
    path('medicos/novo/', views.criarMedico, name='medico_criar'),
    path('medicos/<int:pk>/editar/', views.atualizarMedico, name='medico_atualizar'),
    path('medicos/<int:pk>/deletar/', views.deletarMedico, name='medico_deletar'),
    
    # Pacientes (Buscando do app pacientes)
    path('pacientes/', pacViews.listarPacientes, name='paciente_listar'),
    path('pacientes/novo/', pacViews.adicionarPaciente, name='paciente_criar'),
    path('pacientes/<int:pk>/editar/', pacViews.editarPaciente, name='paciente_atualizar'),
    path('pacientes/<int:pk>/deletar/', pacViews.deletarPaciente, name='paciente_deletar'),
    
    # Agendas
    path('agendas/', views.listarAgendas, name='agenda_listar'),
    path('agendas/novo/', views.criarAgenda, name='agenda_criar'),
    path('agendas/<int:pk>/editar/', views.atualizarAgenda, name='agenda_atualizar'),
    path('agendas/<int:pk>/deletar/', views.deletarAgenda, name='agenda_deletar'),
    
    # Procedimentos
    path('procedimentos/', views.listarProcedimentos, name='procedimento_listar'),
    path('procedimentos/novo/', views.criarProcedimento, name='procedimento_criar'),
    path('procedimentos/<int:pk>/editar/', views.atualizarProcedimento, name='procedimento_atualizar'),
    path('procedimentos/<int:pk>/deletar/', views.deletarProcedimento, name='procedimento_deletar'),
]

