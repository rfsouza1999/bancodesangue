from django.db import models

class Endereco(models.Model): ## FEITO
    Endereco_Id = models.AutoField(auto_created=True,primary_key=True)
    Endereco_Cep = models.CharField(max_length=10,null=False)
    Endereco_Rua = models.CharField(max_length=150)
    Endereco_Numero = models.CharField(max_length=10, null=False)
    Endereco_Bairro = models.CharField(max_length=50)
    Endereco_Cidade = models.CharField(max_length=25)
    Endereco_Estado = models.CharField(max_length=20)
    Endereco_Pais = models.CharField(max_length=15)
    Endereco_Obs = models.CharField(max_length=100)
    
class Medico(models.Model):
    Medico_Id = models.AutoField(auto_created=True,primary_key=True)
    Medico_Nome = models.CharField(max_length=50,null=False)
    Medico_CRM = models.CharField(max_length=10)
    Medico_Especialidade = models.CharField(max_length=20)
    
class Local(models.Model):
    Local_Id = models.AutoField(auto_created=True,primary_key=True)
    Local_Nome = models.CharField(max_length=50,null=False)
    Local_Tipo = models.CharField(max_length=10,null=False)
    Local_HoraInicio = models.DateTimeField(null=False)
    Local_HoraFim = models.DateTimeField(null=False)
    Local_Endereco = models.ForeignKey(Endereco, null=False, on_delete=models.CASCADE)  
    
class Doacao(models.Model):
    Doacao_Id = models.AutoField(auto_created=True,primary_key=True)
    Doacao_Data = models.DateField(null=False) 
    Doacao_Local = models.ManyToManyField(Local)
    
class Checkup(models.Model):
    Checkup_Id = models.AutoField(auto_created=True,primary_key=True)
    Checkup_Cid = models.CharField(max_length=10)
    Checkup_Obs = models.CharField(max_length=100)
    Checkup_Data = models.DateField()
    Checkup_Medico = models.ManyToManyField(Medico)

class Pessoa(models.Model): ## FEITO
    Pessoa_Cpf = models.IntegerField(primary_key=True, unique=True)
    Pessoa_Nome = models.CharField(max_length=50, null=False)
    Pessoa_Telefone1 = models.CharField(max_length=15,null=False)
    Pessoa_Telefone2 = models.CharField(max_length=15, blank=True, null=True)
    Pessoa_Peso = models.FloatField()      
    Pessoa_Altura = models.CharField(max_length=5)
    Pessoa_TipoSanguineo = models.CharField(max_length=3, null=False)
    Pessoa_Sexo = models.CharField(max_length=1)
    Pessoa_DataNascimento = models.CharField(null=False, max_length=15)
    Pessoa_Endereco = models.ManyToManyField(Endereco, blank=False)
    Pessoa_Checkup = models.ManyToManyField(Checkup, blank=False)
    Pessoa_Doacoes = models.ManyToManyField(Doacao, blank=False)
    
class Compartilhamento(models.Model): ## FEITO
    Compartilhamento_Id = models.AutoField(auto_created=True,primary_key=True)
    Compartilhamento_Data = models.DateField(null=False)
    Compartilhamento_Link = models.URLField(null=False)
    Compartilhamento_Pessoa = models.ForeignKey(Pessoa,null=False,on_delete=models.CASCADE)
    Compartilhamento_Local = models.ForeignKey(Local, null=False, on_delete=models.CASCADE)
    Compartilhamento_Doacao = models.ForeignKey(Doacao, null=False, on_delete=models.CASCADE)
