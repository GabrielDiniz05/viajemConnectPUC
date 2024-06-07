from django.contrib import admin
from .models import Viagem, Destino


@admin.register(Destino)
class Destino(admin.ModelAdmin):
    list_display = ('nome', 'criador', )
    search_fields = ('nome',)


@admin.register(Viagem)
class ViagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'destino', 'criador', 'dataSaida')
    search_fields = ('nome', 'destino')
    prepopulated_fields = {'slug':['nome']}


