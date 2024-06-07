from django import forms
from .models import Viagem


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['slug', 'destino', 'descricao', 'imagem', 'dataSaida', 'dataVolta', 'integrantes']


class SearchForm(forms.Form):
    query = forms.CharField(label='Pesquisar Destinos', max_length=100)
