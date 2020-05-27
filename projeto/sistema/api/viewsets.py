
from rest_framework.viewsets import ModelViewSet
from sistema.models import SistemaCliente
from .serializers import  SistemaSerializer



class SistemaviewSet(ModelViewSet):
    serializer_class = SistemaSerializer

    def get_queryset(self):
        sistema = self.request.query_params.get('sistema', None)
        queryset = SistemaCliente.objects.filter(Sistema=sistema)
        return queryset

    def List (self, request, *args, **kwargs):
        return SistemaCliente.objects.all()

  