from django import forms
from .models import Viagem, Formulario, Roteiro


class ViagemForm(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = ['nome', 'destino', 'roteiro', 'descricao', 'imagem', 'dataSaida', 'dataVolta', 'integrantes']

    def __init__(self, *args, **kwargs):
        super(ViagemForm, self).__init__(*args, **kwargs)
        self.fields['roteiro'] = forms.ModelChoiceField(queryset=Roteiro.objects.none(), required=False, label='Roteiro')

        if 'destino' in self.data:
            try:
                destino_id = int(self.data.get('destino'))
                self.fields['roteiro'].queryset = Roteiro.objects.filter(destino_id=destino_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['roteiro'].queryset = self.instance.destino.roteiros.all()



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
