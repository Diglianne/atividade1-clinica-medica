from django.contrib import admin
from .models import Medico, Especialidade, Procedimento, AgendaConsultas, Atendimento

# 1. Painel de Médicos
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'email', 'cpf')

admin.site.register(Medico, MedicoAdmin)


# 2. Painel de Especialidades
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'imagem')

admin.site.register(Especialidade, EspecialidadeAdmin)


# 3. Painel de Procedimentos
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome', 'foto', 'duracao_estimada', 'data_criacao', 'custo_operacional', 'especialidade')

admin.site.register(Procedimento, ProcedimentoAdmin)


# 4. Painel de Agenda de Consultas
class AgendaConsultasAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'ano', 'periodo', 'procedimento')

admin.site.register(AgendaConsultas, AgendaConsultasAdmin)


# 5. Painel de Atendimentos
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nome_paciente', 'duracao_minutos', 'sala', 'agenda')

admin.site.register(Atendimento, AtendimentoAdmin)
