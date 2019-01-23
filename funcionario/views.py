from django.shortcuts import render, redirect, get_object_or_404
from .models import Funcionario
from .forms import FuncionarioForm


# Create your views here.
def func_gerenciar(request):
    """Gerenciar cadastro dos funcionarios."""
    model = Funcionario.objects.all()
    return render(request, 'func_gerenciar.html', {'funcionarios': model})


# Criar funcionario
def func_create(request):
    """Cadastrar novo funcionario."""
    form = FuncionarioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('func_gerenciar')
    return render(request, 'func_create.html', { 'form': form })


# Deletar funcionario
def func_delete(request):
    """Excluir funcionario."""
    return render(request, 'func_delete.html')


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

