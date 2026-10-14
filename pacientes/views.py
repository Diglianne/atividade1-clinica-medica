from django.shortcuts import render, redirect
from pacientes.models import Paciente
from pacientes.forms import PacienteForm # Importa o forms que limpamos!

# 1. Listar Pacientes
def listarPacientes(request):
    lista = Paciente.objects.all()
    return render(request, 'pacientes/listagem.html', {'pacientes': lista})

# 2. Criar Paciente (Ajustado para mandar o form automático)
def adicionarPaciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('paciente_listar')
    else:
        form = PacienteForm() # Cria as caixas automáticas em branco
        
    # Enviamos a variável 'form' para o adicionar.html desenhar as caixas!
    return render(request, 'pacientes/adicionar.html', {'form': form})

# 3. Editar Paciente
def editarPaciente(request, pk):
    paciente_existente = Paciente.objects.get(pk=pk)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=paciente_existente)
        if form.is_valid():
            form.save()
            return redirect('paciente_listar')
    else:
        form = PacienteForm(instance=paciente_existente)
    return render(request, 'pacientes/adicionar.html', {'form': form})

# 4. Deletar Paciente
def deletarPaciente(request, pk):
    paciente_existente = Paciente.objects.get(pk=pk)
    if request.method == "POST":
        paciente_existente.delete()
        return redirect('paciente_listar')
    return render(request, 'pacientes/paciente_deletar.html', {'paciente': paciente_existente})



