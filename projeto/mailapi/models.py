from django.db import models
from sistema.models import SistemaCliente


class Emailapi(models.Model):
   EmailOrigem = models.CharField(max_length=100)
   EmailDestino =  models.CharField(max_length=100)
   Assunto = models.CharField(max_length=100, null=True )
   Conteudo = models.TextField()
   Cliente = models.ForeignKey(SistemaCliente, on_delete=models.CASCADE, null=True, blank=True)
   Data = models.DateTimeField(auto_now=True)
	
   def __str__(self):
       return self.Nome     

