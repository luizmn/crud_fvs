from django.db import models

# Create your models here.
class Funcionario(models.Model):
    fnc_nome = models.CharField(max_length=100)
    fnc_matricula = models.CharField(max_length=10, blank=True)

    def __str__ (self):
        return self.fnc_nome
