from django.contrib import admin
from consultas.models import Medico, Especialidade, Procedimento, AgendaConsultas

# 1. Painel de Médicos (Estilo idêntico ao do professor)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('crm', 'nome', 'email', 'especialidade')

admin.site.register(Medico, MedicoAdmin)

# 2. Painel de Especialidades
class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome') # Usamos o id padrão do Django no lugar do código manual

admin.site.register(Especialidade, EspecialidadeAdmin)

# 3. Painel de Procedimentos
class ProcedimentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'custo_operacional')

admin.site.register(Procedimento, ProcedimentoAdmin)

# 4. Painel de Agenda de Consultas
class AgendaConsultasAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'procedimento', 'data', 'horario')

admin.site.register(AgendaConsultas, AgendaConsultasAdmin)

