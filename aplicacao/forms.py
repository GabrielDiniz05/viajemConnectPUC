from django import forms
from .models import Viagem, Formulario


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['slug', 'destino', 'descricao', 'imagem', 'dataSaida', 'dataVolta', 'integrantes']


class SearchForm(forms.Form):
    query = forms.CharField(label='Pesquisar Destinos', max_length=100)


class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = ['faixaEtaria', 'regiao', 'rendaSalarial', 'frequencia', 'destinoIdeal', 'perfil', 'costume', 'organizacao']
        widgets = {
            'faixaEtaria': forms.Select(attrs={'class': 'form-control'}),
            'regiao': forms.Select(attrs={'class': 'form-control'}),
            'rendaSalarial': forms.Select(attrs={'class': 'form-control'}),
            'frequencia': forms.Select(attrs={'class': 'form-control'}),
            'destinoIdeal': forms.Select(attrs={'class': 'form-control'}),
            'perfil': forms.Select(attrs={'class': 'form-control'}),
            'costume': forms.Select(attrs={'class': 'form-control'}),
            'organizacao': forms.Select(attrs={'class': 'form-control'}),
        }
