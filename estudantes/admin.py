from django.contrib import admin
from estudantes.models import Paciente

class PacienteAdmin(admin.ModelAdmin):
    # Mostra os novos campos simples na lista do painel do professor
    list_display = ('id', 'nome', 'cpf', 'telefone', 'data_nascimento')

admin.site.register(Paciente, PacienteAdmin)
