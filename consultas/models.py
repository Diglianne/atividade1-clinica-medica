from django.db import models
# Importamos o Paciente lá da outra pasta para vincular as consultas a ele
from pacientes.models import Paciente 

# 1. ESPECIALIDADE
class Especialidade(models.Model):
    nome = models.CharField(max_length=150)
    imagen = models.ImageField(upload_to='fotos/especialidades', blank=True, null=True)

    def __str__(self):
        return self.nome

# 2. MEDICO
class Medico(models.Model):
    crm = models.CharField(max_length=12)
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.nome

# 3. PROCEDIMENTO
class Procedimento(models.Model):
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/procedimentos', blank=True, null=True)
    custo_operacional = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

# 4. AGENDA DE CONSULTAS
class AgendaConsultas(models.Model):
    # Vincula diretamente ao Paciente cadastrado no outro app
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.PROTECT)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"Consulta: {self.paciente.nome} com {self.medico.nome}"

