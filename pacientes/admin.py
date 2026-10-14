from django.contrib import admin
from pacientes.models import PlanoSaude, Paciente

class PlanoSaudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

admin.site.register(PlanoSaude, PlanoSaudeAdmin)

class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'cpf', 'telefone', 'plano')

admin.site.register(Paciente, PacienteAdmin)
