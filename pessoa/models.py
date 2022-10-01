from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_completo
