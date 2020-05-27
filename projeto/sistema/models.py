from django.db import models

class SistemaCliente(models.Model):
    Sistema = models.CharField(max_length=100)
    ServidorEmail = models.CharField(max_length=100)
    LoginServidor = models.CharField(max_length=100)
    SenhaServidor = models.CharField(max_length=50)
    Porta = models.IntegerField()
    SSL =  models.BooleanField(default=False)

	
    def __str__(self):
       return self.Sistema 
