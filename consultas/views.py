from django.shortcuts import render, redirect
from .models import Medico, Especialidade, Procedimento, AgendaConsultas
from pacientes.models import Paciente 

# ==================== PÁGINA INICIAL ====================
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
        
        novo = Medico(crm=crm, nome=nome, email=email)
        novo.save()
        return redirect('medico_listar')
    return render(request, 'medico_criar.html')

def atualizarMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    if request.method == "POST":
        medico.crm = request.POST.get('crm')
        medico.nome = request.POST.get('nome')
        medico.email = request.POST.get('email')
        medico.save()
        return redirect('medico_listar')
    return render(request, 'medico_atualizar.html', {'medico': medico})

def deletarMedico(request, pk):
    medico = Medico.objects.get(id=pk)
    if request.method == "POST":
        medico.delete()
        return redirect('medico_listar')
    return render(request, 'medico_deletar.html', {'medico': medico})

# ==================== AGENDAS (CONSULTAS) ====================
def listarAgendas(request):
    agendas = AgendaConsultas.objects.all()
    return render(request, 'agenda_listar.html', {'agendas': agendas})

def criarAgenda(request):
    if request.method == "POST":
        paciente_id = request.POST.get('paciente')
        medico_id = request.POST.get('medico')
        procedimento_id = request.POST.get('procedimento')
        data = request.POST.get('data')
        horario = request.POST.get('horario')
        
        # Cria a agenda direto com os dados da clínica
        AgendaConsultas.objects.create(
            paciente_id=paciente_id,
            medico_id=medico_id,
            procedimento_id=procedimento_id,
            data=data,
            horario=horario
        )
        return redirect('agenda_listar')
        
    contexto = {
        'pacientes': Paciente.objects.all(),
        'medicos': Medico.objects.all(),
        'procedimentos': Procedimento.objects.all()
    }
    return render(request, 'agenda_criar.html', contexto)

def atualizarAgenda(request, pk):
    agenda = AgendaConsultas.objects.get(id=pk)
    if request.method == "POST":
        agenda.data = request.POST.get('data')
        agenda.horario = request.POST.get('horario')
        agenda.save()
        return redirect('agenda_listar')
    return render(request, 'agenda_atualizar.html', {'agenda': agenda})

def deletarAgenda(request, pk):
    agenda = AgendaConsultas.objects.get(id=pk)
    if request.method == "POST":
        agenda.delete()
        return redirect('agenda_listar')
    return render(request, 'agenda_deletar.html', {'agenda': agenda})

# ==================== PROCEDIMENTOS ====================
def listarProcedimentos(request):
    procedimentos = Procedimento.objects.all()
    return render(request, 'procedimento_listar.html', {'procedimentos': procedimentos})

def criarProcedimento(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        custo = request.POST.get('custo_operacional')
        
        novo = Procedimento(nome=nome, custo_operacional=custo)
        novo.save()
        return redirect('procedimento_listar')
    return render(request, 'procedimento_criar.html')

def atualizarProcedimento(request, pk):
    procedimento = Procedimento.objects.get(id=pk)
    if request.method == "POST":
        procedimento.nome = request.POST.get('nome')
        procedimento.custo_operacional = request.POST.get('custo_operacional')
        procedimento.save()
        return redirect('procedimento_listar')
    return render(request, 'procedimento_atualizar.html', {'procedimento': procedimento})

def deletarProcedimento(request, pk):
    procedimento = Procedimento.objects.get(id=pk)
    if request.method == "POST":
        procedimento.delete()
        return redirect('procedimento_listar')
    return render(request, 'procedimento_deletar.html', {'procedimento': procedimento})



