from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Viagem


class AplicacaoListView(ListView):
    model = Viagem
    template_name = 'aplicacao/home.html'

class AplicacaoListViewSearch(ListView):
    model = Viagem
    template_name = 'aplicacao/search.html'

class AplicacaoDetailView(DetailView):
    model = Viagem
    template_name = 'aplicacao/viagem-detail.html'

class AplicacaoLoginView(ListView):
    model = Viagem
    template_name = 'aplicacao/login.html'

class AplicacaoCadastroView(ListView):
    model = Viagem
    template_name = 'aplicacao/cadastro.html'
