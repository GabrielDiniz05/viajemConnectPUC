from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.urls import reverse


class Viagem(models.Model):

    nome = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    destino = models.TextField();
    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='img-viagens', blank=True, null=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    integrantes = models.ManyToManyField(User, related_name='integrantes', default=None)
    dataCriacao = models.DateTimeField(verbose_name='Data de Criação',auto_now_add=True)
    dataSaida = models.DateTimeField(verbose_name='Data de Saída')

    def get_absolute_url(self):
        return reverse('viagem-detail', args=[self.slug])

    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'

    def __str__(self):
        return self.nome


