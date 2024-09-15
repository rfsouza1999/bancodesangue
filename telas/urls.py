from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from telas import views
from bancodesangue.telas import views

app_name = 'telas'

urlpatterns =[
    path('', views.home.as_view(), name='home' ),
    path('/inicio/', views.inicio.as_view(), name='inicio' ),
    path('/criar_conta/', views.inicio.as_view(), name='criar_conta' ),
    path('/dados_pessoa/', views.inicio.as_view(), name='dados_pessoa' ),
    path('/endereco/', views.inicio.as_view(), name='endereco' ),
    path('/esqueceu/', views.inicio.as_view(), name='esqueceu' ),
    path('/link_compart/', views.inicio.as_view(), name='link_compart' ),
    path('/lista_doacao/', views.inicio.as_view(), name='lista_doacao' ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)