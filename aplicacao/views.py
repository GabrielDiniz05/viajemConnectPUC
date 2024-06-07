from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from . models import Viagem, Destino
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password


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