from django.shortcuts import render, redirect
from .models import Medico, Especialidade, Procedimento, AgendaConsultas, Atendimento

# Dashboard simples
def dashboard(request):
    return render(request, 'dashboard.html')

# ==================== MÉDICOS ====================
def listarMedicos(request):
    medicos = Medico.objects.all()
    return render(request, 'medico_listar.html', {'medicos': medicos})

def criarMedico(request):
    if request.method == "POST":
        crm = request.POST.get('crm')
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        novo = Medico(crm=crm, nome=nome, email=email, cpf=cpf)
        novo.save()
        return redirect('medico_listar')
    return render(request, 'medico_criar.html')

def atualizarMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    if request.method == "POST":
        medico.crm = request.POST.get('crm')
        medico.nome = request.POST.get('nome')
        medico.email = request.POST.get('email')
        medico.cpf = request.POST.get('cpf')
        medico.save()
        return redirect('medico_listar')
    return render(request, 'medico_atualizar.html', {'medico': medico})

def deletarMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    if request.method == "POST":
        medico.delete()
        return redirect('medico_listar')
    return render(request, 'medico_deletar.html', {'medico': medico})


# ==================== AGENDAS ====================
def listarAgendas(request):
    agendas = AgendaConsultas.objects.all()
    return render(request, 'agenda_listar.html', {'agendas': agendas})

def criarAgenda(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        ano = request.POST.get('ano')
        periodo = request.POST.get('periodo')
        procedimento_id = request.POST.get('procedimento')
        
        proc = Procedimento.objects.get(codigo=procedimento_id)
        
        nova_agenda = AgendaConsultas(codigo=codigo, ano=ano, periodo=periodo, procedimento=proc)
        nova_agenda.save()
        return redirect('agenda_listar')
    procedimentos = Procedimento.objects.all()
    return render(request, 'agenda_criar.html', {'procedimentos': procedimentos})

def atualizarAgenda(request, pk):
    agenda = AgendaConsultas.objects.get(id=pk)
    if request.method == "POST":
        agenda.codigo = request.POST.get('codigo')
        agenda.ano = request.POST.get('ano')
        agenda.periodo = request.POST.get('periodo')
        procedimento_id = request.POST.get('procedimento')
        
        agenda.procedimento = Procedimento.objects.get(codigo=procedimento_id)
        agenda.save()
        return redirect('agenda_listar')
    procedimentos = Procedimento.objects.all()
    return render(request, 'agenda_atualizar.html', {'agenda': agenda, 'procedimentos': procedimentos})

def deletarAgenda(request, pk):
    agenda = AgendaConsultas.objects.get(id=pk)
    if request.method == "POST":
        agenda.delete()
        return redirect('agenda_listar')
    return render(request, 'agenda_deletar.html', {'agenda': agenda})


# ==================== ATENDIMENTOS ====================
def listarAtendimentos(request):
    atendimentos = Atendimento.objects.all()
    return render(request, 'atendimento_listar.html', {'atendimentos': atendimentos})

def criarAtendimento(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        nome_paciente = request.POST.get('nome_paciente')
        duracao_minutos = request.POST.get('duracao_minutos')
        sala = request.POST.get('sala')
        agenda_id = request.POST.get('agenda')
        
        age = AgendaConsultas.objects.get(id=agenda_id)
        
        novo_atend = Atendimento(codigo=codigo, nome_paciente=nome_paciente, duracao_minutos=duracao_minutos, sala=sala, agenda=age)
        novo_atend.save()
        return redirect('atendimento_listar')
    agendas = AgendaConsultas.objects.all()
    return render(request, 'atendimento_criar.html', {'agendas': agendas})

def atualizarAtendimento(request, pk):
    atendimento = Atendimento.objects.get(codigo=pk)
    if request.method == "POST":
        atendimento.nome_paciente = request.POST.get('nome_paciente')
        atendimento.duracao_minutos = request.POST.get('duracao_minutos')
        atendimento.sala = request.POST.get('sala')
        agenda_id = request.POST.get('agenda')
        
        atendimento.agenda = AgendaConsultas.objects.get(id=agenda_id)
        atendimento.save()
        return redirect('atendimento_listar')
    agendas = AgendaConsultas.objects.all()
    return render(request, 'atendimento_atualizar.html', {'atendimento': atendimento, 'agendas': agendas})

def deletarAtendimento(request, pk):
    atendimento = Atendimento.objects.get(codigo=pk)
    if request.method == "POST":
        atendimento.delete()
        return redirect('atendimento_listar')
    return render(request, 'atendimento_deletar.html', {'atendimento': atendimento})


# ==================== PROCEDIMENTOS ====================
def listarProcedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimento_listar.html', {'procedimentos': procedimentos})

def criarProcedimento(request):
    if request.method == "POST":
        codigo = request.POST.get('codigo')
        nome = request.POST.get('nome')
        foto = request.FILES.get('foto')
        duracao_estimada = request.POST.get('duracao_estimada')
        data_criacao = request.POST.get('data_criacao')
        custo_operacional = request.POST.get('custo_operacional')
        especialidade_id = request.POST.get('especialidade')
        
        esp = Especialidade.objects.get(id=especialidade_id)
        
        novo_proc = Procedimento(
            codigo=codigo, nome=nome, foto=foto, 
            duracao_estimada=duracao_estimada, data_criacao=data_criacao, 
            custo_operacional=custo_operacional, especialidade=esp
        )
        novo_proc.save()
        return redirect('procedimento_listar')
    especialidades = Especialidade.objects.all()
    return render(request, 'procedimento_criar.html', {'especialidades': especialidades})

def atualizarProcedimento(request, pk):
    procedimento = Procedimento.objects.get(codigo=pk)
    if request.method == "POST":
        procedimento.nome = request.POST.get('nome')
        if request.FILES.get('foto'):
            procedimento.foto = request.FILES.get('foto')
        procedimento.duracao_estimada = request.POST.get('duracao_estimada')
        procedimento.data_criacao = request.POST.get('data_criacao')
        procedimento.custo_operacional = request.POST.get('custo_operacional')
        especialidade_id = request.POST.get('especialidade')
        
        procedimento.especialidade = Especialidade.objects.get(id=especialidade_id)
        procedimento.save()
        return redirect('procedimento_listar')
    especialidades = Especialidade.objects.all()
    return render(request, 'procedimento_atualizar.html', {'procedimento': procedimento, 'especialidades': especialidades})

def deletarProcedimento(request, pk):
    procedimento = Procedimento.objects.get(codigo=pk)
    if request.method == "POST":
        procedimento.delete()
        return redirect('procedimento_listar')
    return render(request, 'procedimento_deletar.html', {'procedimento': procedimento})


