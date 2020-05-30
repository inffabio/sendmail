
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from sistema.models import SistemaCliente
from .serializers import  SistemaSerializer



class SistemaviewSet(ModelViewSet):
    serializer_class = SistemaSerializer

    def get_queryset(self):
        sistema = self.request.query_params.get('sistema', None)
        queryset = SistemaCliente.objects.filter(Sistema=sistema)
        return queryset

    def list (self, request, *args, **kwargs):
        queryset = SistemaCliente.objects.all()
        serializer = SistemaSerializer(queryset, many=True)
        return Response(serializer.data)

  