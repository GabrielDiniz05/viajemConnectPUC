from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Viagem, Destino, Formulario, Roteiro
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .forms import FormularioForm, ViagemForm
from django.http import JsonResponse
from django.urls import reverse_lazy


def HomeView(request):
    return render(request, 'aplicacao/home.html')

class AplicacaoListViewSearch(ListView):
    model = Viagem
    template_name = 'aplicacao/search.html'

class AplicacaoDetailView(DetailView):
    model = Viagem
    template_name = 'aplicacao/viagem-detail.html'

class AplicacaoCadastroView(ListView):
    model = Viagem
    template_name = 'aplicacao/cadastro.html'

def CadastroView(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
           return render(request, 'registration/cadastro.html', {'error': 'As senhas não correspondem'})

        user = User.objects.create(
            username=username,
            email=email,
            password=make_password(password1)
        )
        return redirect('login')

    return render(request, 'registration/cadastro.html')


def LoginView(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,  username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                formulario = Formulario.objects.get(user=user)
                if not formulario.is_completed:
                    return redirect('formulario')
            except Formulario.DoesNotExist:
                return redirect('formulario')
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Login inválido'})
    else:
        return render(request, 'login.html')

@login_required
def LogoutView(request):
    logout(request)
    return redirect('start-page')


def search_destinos(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        destinos = Destino.objects.filter(nome__icontains=query)
        return render(request, 'aplicacao/search_destinos.html', {'destinos': destinos, 'query':query})


@login_required
def join_viagem(request, slug):
    viagem = get_object_or_404(Viagem, slug=slug)
    if request.user not in viagem.integrantes.all():
        viagem.integrantes.add(request.user)
        viagem.save()
    return HttpResponseRedirect(reverse('viagem-detail', args=[slug]))


@login_required
def leave_viagem(request, slug):
    viagem = get_object_or_404(Viagem, slug=slug)
    if request.user in viagem.integrantes.all():
        viagem.integrantes.remove(request.user)
        viagem.save()
    return HttpResponseRedirect(reverse('viagem-detail', args=[slug]))


@login_required
def FormularioView(request):
    try:
        formulario = Formulario.objects.get(user=request.user)
    except Formulario.DoesNotExist:
        formulario = None

    if formulario:
        if formulario.is_completed:
            return redirect('home')

    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            if formulario:
                formulario.is_completed = True
                formulario.faixaEtaria = form.cleaned_data['faixaEtaria']
                formulario.regiao = form.cleaned_data['regiao']
                formulario.rendaSalarial = form.cleaned_data['rendaSalarial']
                formulario.frequencia = form.cleaned_data['frequencia']
                formulario.destinoIdeal = form.cleaned_data['destinoIdeal']
                formulario.perfil = form.cleaned_data['perfil']
                formulario.costume = form.cleaned_data['costume']
                formulario.organizacao = form.cleaned_data['organizacao']
            else:
                formulario = Formulario.objects.create(user=request.user)
                formulario.is_completed = True;
                formulario.faixaEtaria = form.cleaned_data['faixaEtaria']
                formulario.regiao = form.cleaned_data['regiao']
                formulario.rendaSalarial = form.cleaned_data['rendaSalarial']
                formulario.frequencia = form.cleaned_data['frequencia']
                formulario.destinoIdeal = form.cleaned_data['destinoIdeal']
                formulario.perfil = form.cleaned_data['perfil']
                formulario.costume = form.cleaned_data['costume']
                formulario.organizacao = form.cleaned_data['organizacao']
            formulario.save()
            return redirect('home')
    else:
        form = FormularioForm()
    return render(request, 'aplicacao/formulario.html', {'form': form})


class CriarViagemView(LoginRequiredMixin, CreateView):
    model = Viagem
    form_class = ViagemForm
    template_name = 'aplicacao/criar_viagem.html'
    success_url = reverse_lazy('home')  # Substitua 'home' pela URL que você deseja redirecionar após a criação

    def form_valid(self, form):
        form.instance.criador = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ViagemForm(self.request.POST or None)
        return context

@login_required
def get_roteiros(request, destino_id):
    roteiros = Roteiro.objects.filter(destino_id=destino_id).values('id', 'sobre')
    return JsonResponse(list(roteiros), safe=False)