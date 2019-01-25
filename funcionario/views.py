from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario, Setor
from .forms import FuncionarioForm, SetorForm


# Create your views here.
def func_gerenciar(request):
    """Gerenciar cadastro dos funcionarios."""
    model = Funcionario.objects.all()
    return render(request, 'func_gerenciar.html', {'funcionarios': model})


# Criar funcionario
def func_create(request):
    """Cadastrar novo funcionario."""
    form = FuncionarioForm(request.POST or None, request.FILES or None)
    setorList = Setor.objects.all()

    if form.is_valid():
        form.save()
        return redirect('func_gerenciar')
    return render(request, 'func_create.html', { 'form': form , 'setorList': setorList })


# Deletar funcionario
def func_delete(request, id):
    """Excluir funcionario."""
    model = get_object_or_404(Funcionario, pk=id)

    if request.POST:
        model.delete()
        return redirect('func_gerenciar')

    return render(request, 'func_delete.html', {'model': model})


# Atualizar funcionario
def func_update(request, id):
    """Atualizar cadastro do funcionario."""
    model = get_object_or_404(Funcionario, pk=id)
    form = FuncionarioForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('func_gerenciar')

    return render(request, 'func_update.html', {'form': form})


# Visualizar funcionario
def func_view(request, id):
    """Visualizar cadastro do funcionario."""
    model = get_object_or_404(Funcionario, pk=id)

    return render(request, 'func_view.html', {'model': model})


# Gerenciar Setor
def setor_gerenciar(request):
    """Gerenciar cadastro dos setores."""
    model = Setor.objects.all()
    return render(request, 'setor_gerenciar.html', {'setores': model})


# Criar setor
def setor_create(request):
    """Cadastrar novo setor."""
    form = SetorForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('setor_gerenciar')
    return render(request, 'setor_create.html', { 'form': form })


# Deletar setor
def setor_delete(request, id):
    """Excluir setor."""
    model = get_object_or_404(Setor, pk=id)

    if request.POST:
        model.delete()
        return redirect('setor_gerenciar')

    return render(request, 'setor_delete.html', {'model': model})


# Atualizar setor
def setor_update(request, id):
    """Atualizar cadastro do funcionario."""
    model = get_object_or_404(Setor, pk=id)
    form = SetorForm(request.POST or None, request.FILES or None, instance=model)

    if form.is_valid():
        form.save()
        return redirect('setor_gerenciar')

    return render(request, 'setor_update.html', {'form': form})


# Visualizar setor
def setor_view(request, id):
    """Visualizar cadastro do setor."""
    model = get_object_or_404(Setor, pk=id)

    return render(request, 'setor_view.html', {'model': model})

