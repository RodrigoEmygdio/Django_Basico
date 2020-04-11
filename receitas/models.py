import datetime as dt

from django.db import models


class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    igrendientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=dt.datetime.now(), blank=True)
