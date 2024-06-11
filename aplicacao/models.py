from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse


class Destino(models.Model):
    nome = models.CharField(max_length=100, default="")
    criador = models.ForeignKey(User, on_delete=models.CASCADE, default=User)

    class Meta:
        verbose_name = 'Destino'
        verbose_name_plural = 'Destinos'

    def __str__(self):
        return self.nome


class Roteiro(models.Model):
    sobre = RichTextField(verbose_name='Sobre')
    como_chegar = RichTextField(verbose_name='Como chegar?')
    hospedagem = RichTextField(verbose_name='Hospedagem')
    transporte = RichTextField(verbose_name='Transporte')
    o_que_levar = RichTextField(verbose_name='O que levar?')
    quando_ir = RichTextField(verbose_name='Quando ir?')
    passeios = RichTextField(verbose_name='Passeios')

    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='roteiros', default=None)

    def __str__(self):
        return f'Roteiro para o destino de {self.destino}'


class Viagem(models.Model):
    nome = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)

    destino = models.ForeignKey(Destino, on_delete=models.CASCADE, related_name='viagens')
    destino_nome = models.CharField(max_length=100, editable=False)

    roteiro = models.ForeignKey(Roteiro, on_delete=models.SET_NULL, null=True, blank=True)

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=User)
    is_completed = models.BooleanField(default=False)

    faixaEtaria = models.CharField(max_length=1, choices=FAIXA_ETARIA_CHOICES)
    regiao = models.CharField(max_length=1, choices=REGIAO_CHOICES)
    rendaSalarial = models.CharField(max_length=1, choices=RENDA_SALARIAL_CHOICES)
    frequencia = models.CharField(max_length=1, choices=FREQUENCIA_CHOICES)
    destinoIdeal = models.CharField(max_length=1, choices=DESTINO_IDEAL_CHOICES)
    perfil = models.CharField(max_length=1, choices=PERFIL_CHOICES)
    costume = models.CharField(max_length=1, choices=COSTUME_CHOICES)
    organizacao = models.CharField(max_length=1, choices=ORGANIZACAO_CHOICES)


    def __str__(self):
        return f'Formulário de {self.user}'