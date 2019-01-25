from django.forms import ModelForm, TextInput
from .models import Funcionario, Setor


class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['fnc_nome', 'fnc_matricula', 'fnc_estado']
        widgets = {
            'fnc_nome': TextInput(attrs={'class': 'form-control'}),
            'fnc_matricula': TextInput(attrs={'class': 'form-control'}),
            'fnc_estado': TextInput(attrs={'class': 'form-control'}),
            'setor' : ChoiceField(queryset=Setor.objects.all()),
        }

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['setor_nome', 'setor_unidade']
        widgets = {
            'setor_nome': TextInput(attrs={'class': 'form-control'}),
            'setor_unidade': TextInput(attrs={'class': 'form-control'}),
        }