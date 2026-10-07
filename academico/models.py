from django.db import models

# 1. MEDICO
class Medico(models.Model):
    crm = models.CharField(max_length=12)
    nome = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    cpf = models.CharField(max_length=14)

    def __str__(self):
        return self.nome

# 2. ESPECIALIDADE
class Especialidade(models.Model):
    codigo = models.CharField(max_length=10)
    nome = models.CharField(max_length=150)
    imagem = models.ImageField(upload_to='fotos/especialidades')

    def __str__(self):
        return self.nome

# 3. PROCEDIMENTO
class Procedimento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos/procedimentos')
    duracao_estimada = models.DecimalField(max_digits=3, decimal_places=2)
    data_criacao = models.DateField(blank=True, null=True)
    custo_operacional = models.IntegerField()
    medico = models.ManyToManyField(Medico, blank=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

# 4. AGENDACONSULTAS
class AgendaConsultas(models.Model):
    codigo = models.CharField(max_length=15)
    ano = models.IntegerField()
    periodo = models.CharField(max_length=5)
    procedimento = models.ForeignKey(Procedimento, on_delete=models.PROTECT)

    def __str__(self):
        return self.codigo

# 5. ATENDIMENTO
class Atendimento(models.Model):
    codigo = models.IntegerField(primary_key=True)
    nome_paciente = models.CharField(max_length=150)
    duracao_minutos = models.IntegerField()
    sala = models.CharField(max_length=5)
    agenda = models.ForeignKey(AgendaConsultas, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_paciente

