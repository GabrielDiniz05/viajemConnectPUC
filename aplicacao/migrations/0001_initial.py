# Generated by Django 5.0.4 on 2024-04-30 20:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Viagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250)),
                ('destino', models.TextField()),
                ('descricao', models.TextField()),
                ('dataCriacao', models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')),
                ('dataSaida', models.DateTimeField(verbose_name='Data de Saída')),
                ('criador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('integrantes', models.ManyToManyField(default=None, related_name='integrantes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
