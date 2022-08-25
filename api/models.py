import uuid

from django.contrib.auth.models import User
from django.db import models
from pyexpat import model


class Categoria(models.Model):
    ESCOLHAS_CATEGORIA= (
    ('M', 'Masculino'),
    ('F', 'Feminino'),    
    )
    
    
    tipo = models.CharField(max_length=1, choices=  ESCOLHAS_CATEGORIA,blank=False, null=False)
     
    class Meta:
        ordering= ['id']
    
    def __str__(self) -> str:
        return self.tipo

class Sub_Categoria(models.Model):
    ESCOLHAS_SUB_CATEGORIA= (
    ('A', 'Adulto'),
    ('I', 'Infantil'),    
    ('P','Plus_Size'),
    )
    
    
    tipo = models.CharField(max_length=1, choices=  ESCOLHAS_SUB_CATEGORIA, blank=False, null=False)
     
    class Meta:
        ordering= ['id']
    
    def __str__(self) -> str:
        return self.tipo
    
class Tipos(models.Model):    
    ESCOLHAS_TIPO= (
    ('cam','Camisetas'),
    ('blu','Blusas'),
    ('sho','Shorts'),
    ('cal','Calça'),
    ('int','Roupa_Intima'),
    
    )
    
    nome = models.CharField(max_length=3, choices=  ESCOLHAS_TIPO,blank=False, null=False)
       
     
    class Meta:
        ordering= ['id']
        verbose_name_plural = 'Tipos'
    
    def __str__(self) -> str:
        return self.nome

class Produto(models.Model):
      
      nome =models.CharField(max_length=100,blank=False, null=False)
      categoria=models.ForeignKey('Categoria', on_delete=models.CASCADE,blank=False, null=False)
      tipo=models.ForeignKey('Tipos',on_delete=models.CASCADE,blank=False, null=False)
      s_categoria=models.ForeignKey('Sub_Categoria',on_delete=models.CASCADE,blank=False, null=False)
      qtd_em_estoque =models.PositiveIntegerField( blank=False, null=False)
      preco =models.DecimalField(max_digits = 10, decimal_places= 2,blank=False, null=False )
      cor =models.CharField(max_length=50, blank=False, null=False)
      tamanho=models.PositiveIntegerField(blank=False, null=False)
      imagem = models.ImageField()
      class Meta:
          ordering=['id'] 
      def __str__(self) -> str:
          return f'{self.tipo} - {self.categoria} - {self.nome } - {self.s_categoria} - {self.cor}'
      
class Venda(models.Model):
    class StatusVenda(models.IntegerChoices):
        CARRINHO = 1,'Carrinho'
        REALIZADO = 2,'Realizado'
        PAGO =3,'Pago'
        ENTREGUE =4,'Entregue'
        
    usuario = models.ForeignKey(User, on_delete=models.PROTECT,related_name='venda', default=1)
    status = models.IntegerField(choices= StatusVenda.choices, default= StatusVenda.CARRINHO)
    
    
class VendaItens(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.PositiveIntegerField()
