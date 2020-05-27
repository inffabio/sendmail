from rest_framework.serializers import ModelSerializer
from sistema.models import SistemaCliente

class SistemaSerializer(ModelSerializer):
    class Meta:
        model = SistemaCliente
        fields = ('id', 'Sistema', 'ServidorEmail', 'LoginServidor', 'Porta')