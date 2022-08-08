from http.client import PRECONDITION_FAILED
from re import M
from statistics import mode
from django.db import models

class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    codigo = models.CharField(max_length=4, unique=True)

    def __str__(self):
        return self.nome

class Ativo(models.Model):
    id = models.IntegerField(primary_key=True)
    codigo = models.CharField(max_length=10, unique=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    # Acrescentar método que diz o tipo de ação que o ativo é

    def __str__(self):
        return self.codigo

class AtivoMonitorado(models.Model):
    id = models.IntegerField(primary_key=True)
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    intervalo_consulta = models.IntegerField()

    # Salva os preços de compra e venda com apennas duas casas decimais
    def save(self, *args, **kwargs):
        self.preco_compra = round(self.preco_compra, 2)
        self.preco_venda = round(self.preco_venda, 2)
        super(AtivoMonitorado, self).save(*args, **kwargs)

# Consulta da cotação de um ativo
class Consulta(models.Model):
    id = models.IntegerField(primary_key=True)
    ativo = models.ForeignKey(Ativo, on_delete=models.CASCADE)
    preco = models.FloatField()
    data = models.DateField()