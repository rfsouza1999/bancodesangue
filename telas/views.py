from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Compartilhamento, Endereco, Pessoa
import datetime

def home(request):
    return render(request, 'inicio.html')

def inicio(request):
    if request.method == 'GET':
        return render(request, 'dados_pessoa.html')
    else:
        return render(request, 'dados_pessoa2.html')
    
    
def criar_conta(request):
    return render(request, 'criar_conta.html')

def dados_pessoa(request): ## FEITO
    if request.method == 'POST':
        Pessoa_Cpf = request.POST['Pessoa_Cpf']
        Pessoa_Nome = request.POST['Pessoa_Nome']
        Pessoa_Telefone1 = request.POST['Pessoa_Telefone1']
        Pessoa_Telefone2 = request.POST['Pessoa_Telefone2']
        Pessoa_Peso = request.POST['Pessoa_Peso']
        Pessoa_Altura = request.POST['Pessoa_Altura']
        Pessoa_TipoSanguineo = request.POST['Pessoa_TipoSanguineo']
        Pessoa_Sexo = request.POST['Pessoa_Sexo']
        Pessoa_DataNascimento = request.POST['Pessoa_DataNascimento']
        Pessoa_Endereco = request.POST['Pessoa_Endereco']
        print(Pessoa_Endereco, "alguma coisa")
        dados_pessoa = Pessoa.objects.create(Pessoa_Cpf=Pessoa_Cpf, Pessoa_Nome=Pessoa_Nome, Pessoa_Telefone1=Pessoa_Telefone1, Pessoa_Telefone2=Pessoa_Telefone2, Pessoa_Peso=Pessoa_Peso,  Pessoa_Altura=Pessoa_Altura, Pessoa_TipoSanguineo=Pessoa_TipoSanguineo, Pessoa_Sexo=Pessoa_Sexo, Pessoa_DataNascimento=Pessoa_DataNascimento)
        dados_pessoa.save()
        return render(request, 'link_compart.html')
    else:
        return render(request, 'link_compart.html')
      
 
def dados_pessoa2(request): ## FEITO
    if request.method == 'POST':
        Pessoa_Cpf = request.POST['Pessoa_Cpf']
        Pessoa_Nome = request.POST['Pessoa_Nome']
        Pessoa_Telefone1 = request.POST['Pessoa_Telefone1']
        Pessoa_Telefone2 = request.POST['Pessoa_Telefone2']
        Pessoa_Peso = request.POST['Pessoa_Peso']
        Pessoa_Altura = request.POST['Pessoa_Altura']
        Pessoa_TipoSanguineo = request.POST['Pessoa_TipoSanguineo']
        Pessoa_Sexo = request.POST['Pessoa_Sexo']
        Pessoa_DataNascimento = request.POST['Pessoa_DataNascimento']
        Pessoa_Endereco = request.POST['Pessoa_Endereco']
        dados_pessoa = Pessoa.objects.create(Pessoa_Cpf=Pessoa_Cpf, Pessoa_Nome=Pessoa_Nome, Pessoa_Telefone1=Pessoa_Telefone1, Pessoa_Telefone2=Pessoa_Telefone2, Pessoa_Peso=Pessoa_Peso,  Pessoa_Altura=Pessoa_Altura, Pessoa_TipoSanguineo=Pessoa_TipoSanguineo, Pessoa_Sexo=Pessoa_Sexo, Pessoa_DataNascimento=Pessoa_DataNascimento)
        dados_pessoa.save()
        return render(request, 'lista_doacao.html')
    else:
        return render(request, 'lista_doacao.html')      
       
def endereco(request): ## FEITO
    if request.method == 'POST':
        Endereco_Cep = request.POST['Endereco_Cep']
        Endereco_Rua = request.POST['Endereco_Rua']
        Endereco_Numero = request.POST['Endereco_Numero']
        Endereco_Bairro = request.POST['Endereco_Bairro']
        Endereco_Cidade = request.POST['Endereco_Cidade']
        Endereco_Estado = request.POST['Endereco_Estado']
        Endereco_Pais = request.POST['Endereco_Pais']
        Endereco_Obs = request.POST['Endereco_Obs']
        endereco = Endereco.objects.create(Endereco_Cep=Endereco_Cep, Endereco_Rua=Endereco_Rua, Endereco_Numero=Endereco_Numero, Endereco_Bairro=Endereco_Bairro, Endereco_Cidade=Endereco_Cidade, Endereco_Estado=Endereco_Estado, Endereco_Pais=Endereco_Pais, Endereco_Obs=Endereco_Obs)
        endereco.save()
        return render(request, 'endereco.html')
    return render(request, 'endereco.html')

def link_compart(request): ## FEITO
    if request.method == 'POST':
        Compartilhamento_Id = request.POST['Compartilhamento_Id']
        Compartilhamento_Data = request.POST['Compartilhamento_Data']
        Compartilhamento_Link = request.POST['Compartilhamento_Link']
        Compartilhamento_Pessoa = request.POST['Compartilhamento_Pessoa']
        Compartilhamento_Local = request.POST['Compartilhamento_Local']
        Compartilhamento_Doacao = request.POST['Compartilhamento_Doacao']
        link_compart = Compartilhamento.objects.create(Compartilhamento_Id=Compartilhamento_Id, Compartilhamento_Data=Compartilhamento_Data, Compartilhamento_Link=Compartilhamento_Link, Compartilhamento_Pessoa=Compartilhamento_Pessoa, Compartilhamento_Local=Compartilhamento_Local, Compartilhamento_Doacao=Compartilhamento_Doacao)
        link_compart.save()
        return redirect('compartilhamento')
    return render(request, 'compartilhamento.html')    
    
def lista_doacao(request):
    return render(request, 'lista_doacao.html')

def esqueceu(request):
    return render(request, 'esqueceu.html')
    