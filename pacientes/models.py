from django.db import models

# Uma tabela simples para os planos de saúde (ex: Unimed, SUS)
class PlanoSaude(models.Model):
    nome = models.CharField(max_length=100)

    # Isso serve apenas para o nome do plano aparecer certinho no painel
    def __str__(self):
        return self.nome

# A tabela com os dados básicos do paciente
class Paciente(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    # Conecta o paciente a um plano de saúde
    plano = models.ForeignKey(PlanoSaude, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome
