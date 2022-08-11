from django.db import models

class Usuario(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    status = models.BooleanField(default=True)
