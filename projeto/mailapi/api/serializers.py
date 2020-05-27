from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from mailapi.models import Emailapi
from sistema.models import SistemaCliente

class EmailSerializer(ModelSerializer):
   
    class Meta:
        model = Emailapi
        fields = ('id', 'EmailOrigem', 'EmailDestino', 'Assunto','Conteudo', 'Cliente')