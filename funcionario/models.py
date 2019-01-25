from django.db import models

# Create your models here.

class Setor(models.Model):
    setor_nome = models.CharField(max_length=100)
    setor_unidade = models.CharField(max_length=50)

    def __str__(self):
        return self.setor_nome

class Funcionario(models.Model):
    fnc_nome = models.CharField(max_length=100)
    fnc_matricula = models.CharField(max_length=10, blank=True)
    fnc_estado = models.CharField(max_length=30, blank=True)
    setor = models.ForeignKey(Setor, models.PROTECT, default='1')

    def __str__ (self):
        return self.fnc_nome