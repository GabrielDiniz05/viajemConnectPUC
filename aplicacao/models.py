from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from django.urls import reverse


class Destino(models.Model):
    nome = models.CharField(max_length=100, default="")
    criador = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.nome



class Viagem(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='viagens')
    destino_nome = models.CharField(max_length=100, editable=False)

    descricao = models.TextField(verbose_name='Descrição')
    imagem = models.ImageField(upload_to='img-viagens', blank=True, null=True)
    criador = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    integrantes = models.ManyToManyField(User, related_name='integrantes', default=User)
    dataCriacao = models.DateTimeField(verbose_name='Data de Criação', auto_now_add=True)
    dataSaida = models.DateTimeField(verbose_name='Data de Saída')
    dataVolta = models.DateTimeField(verbose_name='Data da Volta', default=timezone.now())

    def get_absolute_url(self):
        return reverse('viagem-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.destino_nome = self.destino.nome

        if not self.pk:
            contador = Viagem.objects.filter(destino=self.destino).count() + 1
            self.nome = f'Grupo {contador} - {self.destino_nome}';

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Viagem'
        verbose_name_plural = 'Viagens'

    def __str__(self):
        return f'{self.nome} - {self.destino_nome}'
