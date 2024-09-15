from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from telas import views

app_name = 'telas'

urlpatterns =[
    path('', views.home, name='home' ),
    path('inicio/', views.inicio, name='inicio' ),
    path('criar_conta/', views.criar_conta, name='criar_conta' ),
    path('dados_pessoa/', views.dados_pessoa, name='dados_pessoa' ),
    path('dados_pessoa2/', views.dados_pessoa2, name='dados_pessoa2' ),
    path('endereco/', views.endereco, name='endereco' ),
    path('esqueceu/', views.esqueceu, name='esqueceu' ),
    path('link_compart/', views.link_compart, name='link_compart' ),
    path('lista_doacao/', views.lista_doacao, name='lista_doacao' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)