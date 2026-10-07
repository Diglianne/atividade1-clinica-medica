from django.shortcuts import render, redirect
from .models import Paciente

# Listar Pacientes
def listarPacientes(request):
    lista = Paciente.objects.all()
    return render(request, 'paciente_listar.html', {'pacientes': lista})

# Criar Paciente
def criarPaciente(request):
    if request.method == "POST":
        nome_dig = request.POST.get('nome')
        cpf_dig = request.POST.get('cpf')
        tel_dig = request.POST.get('telefone')
        data_dig = request.POST.get('data_nascimento')
        
        novo_paciente = Paciente(nome=nome_dig, cpf=cpf_dig, telefone=tel_dig, data_nascimento=data_dig)
        novo_paciente.save()
        return redirect('paciente_listar')
        
    return render(request, 'paciente_criar.html')

# Atualizar Paciente
def atualizarPaciente(request, pk):
    paciente_existente = Paciente.objects.get(id=pk)
    if request.method == "POST":
        paciente_existente.nome = request.POST.get('nome')
        paciente_existente.cpf = request.POST.get('cpf')
        paciente_existente.telefone = request.POST.get('telefone')
        paciente_existente.data_nascimento = request.POST.get('data_nascimento')
        paciente_existente.save()
        return redirect('paciente_listar')
    return render(request, 'paciente_atualizar.html', {'paciente': paciente_existente})

# Deletar Paciente
def deletarPaciente(request, pk):
    paciente_existente = Paciente.objects.get(id=pk)
    if request.method == "POST":
        paciente_existente.delete()
        return redirect('paciente_listar')
    return render(request, 'paciente_deletar.html', {'paciente': paciente_existente})

