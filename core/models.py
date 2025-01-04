from symtable import Class

from django.db import models

# Trabalhando os Modelos
#Modelo de Dados Pessoa
class Pessoa(models.Model):
    cpf = models.CharField('CPF', max_length=11)
    nome = models.CharField('Nome', max_length=100)
    apelido = models.CharField('Apelido', max_length=20)
    cargo = models.IntegerField('Cargo')

    def __str__(self):
        return self.nome

#Modelo de Dados Cargos
class Cargo(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sigla = models.CharField('Sigla', max_length=3)

    def __str__(self):
        return self.nome

#Modelo de Dados de Unidade Escolar
class UnidadeEscolar(models.Model):
    INEP = models.IntegerField('INEP')
    UE = models.CharField('Unidade Escolar', max_length=150)

    def __str__(self):
        return self.UE

class Sexo(models.Model):
    sexo = models.CharField('Sexo', max_length=1)