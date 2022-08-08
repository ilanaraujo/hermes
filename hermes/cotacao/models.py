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
