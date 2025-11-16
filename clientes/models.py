from django.db import models



# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255, null=False)
    telefone = models.CharField(max_length=15255, null=False, default="Indefinido")



    def __str__(self):
        return f'Nome: {self.nome} - Telefone: {self.telefone} </br>'