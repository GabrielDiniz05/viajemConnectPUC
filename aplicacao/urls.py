from django.urls import path

from . import views

urlpatterns = [
    path('', views.AplicacaoListView.as_view(), name='home'),
    path('search/', views.AplicacaoListViewSearch.as_view(), name='search'),
    path('viagem/<slug:slug>/', views.AplicacaoDetailView.as_view(), name='viagem-detail'),
    path('login/', views.AplicacaoLoginView.as_view(), name='login'),
    path('cadastro/', views.AplicacaoCadastroView.as_view(), name='cadastro'),

]