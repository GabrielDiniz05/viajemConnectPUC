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



class Formulario(models.Model):
    FAIXA_ETARIA_CHOICES = [
        ('1', '15 - 20'),
        ('2', '21 - 29'),
        ('3', '30 - 40'),
        ('4', 'Acima de 40')
    ]

    REGIAO_CHOICES = [
        ('1', 'Norte'),
        ('2', 'Nordeste'),
        ('3', 'Sul'),
        ('4', 'Sudeste'),
        ('5', 'Centro-Oeste')
    ]

    RENDA_SALARIAL_CHOICES = [
        ('1', '1 Salario Minimo'),
        ('2', '2 Salario Minimo'),
        ('3', 'Acima de 3 Salario Minimo'),
        ('4', 'Nao possuo renda')
    ]

    FREQUENCIA_CHOICES = [
        ('1', '1 vez ao ano'),
        ('2', '2 vezes ao ano'),
        ('3', '3 ou mais vezes')
    ]

    DESTINO_IDEAL_CHOICES = [
        ('1', 'Dentro do seu estado'),
        ('2', 'Outros estados do pais'),
        ('3', 'Viagens internacionas')
    ]

    PERFIL_CHOICES = [
        ('1', 'Aproveitar até o último segundo'),
        ('2', 'Ficar no hotel e sair raramente'),
        ('3', 'Mantenho o equilibrio')
    ]

    COSTUME_CHOICES = [
        ('1', 'Sozinho'),
        ('2', 'Em familia'),
        ('3', 'Grupos de amigos'),
        ('4', 'Grupo de pessoas desconhecidas')
    ]

    ORGANIZACAO_CHOICES = [
        ('1', 'Pacotes prontos'),
        ('2', 'Excursões'),
        ('3', 'Conta própria')
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    faixaEtaria = models.CharField(max_length=1, choices=FAIXA_ETARIA_CHOICES)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)




    def __str__(self):
        return f'Formulário de {self.usuario.name}'
