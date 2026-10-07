from django.db import models

class Paciente(models.Model):
    # Campos bem simples e tradicionais de iniciante
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=15)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
