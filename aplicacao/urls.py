from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomeView, name='start-page'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('home/', views.AplicacaoListViewSearch.as_view(), name='home'),
    path('search/', views.search_destinos, name='search'),
    path('viagem/<slug:slug>/', views.AplicacaoDetailView.as_view(), name='viagem-detail'),
    path('cadastro/', views.CadastroView, name='cadastro'),

]