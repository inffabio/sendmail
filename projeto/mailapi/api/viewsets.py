
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from mailapi.models import Emailapi
from sistema.models import SistemaCliente
from mailapi.models import SistemaCliente
from .serializers import  EmailSerializer
from django.core.mail import get_connection, send_mail
from django.core.mail.message import EmailMessage
import smtplib



class EmailviewSet(ModelViewSet):
    serializer_class = EmailSerializer

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        queryset = SistemaCliente.objects.filter(id=id)
        return queryset

    def List (self, request, *args, **kwargs):
        return Emailapi.objects.all()

    def create (self, request, *args, **kwargs):
    
        cliente_Id = request.data['Cliente']
        sistema_cliente =  SistemaCliente.objects.get(id=cliente_Id)

        cliente_Host = sistema_cliente.ServidorEmail
        cliente_Port =  sistema_cliente.Porta 
        cliente_mailUsername = sistema_cliente.LoginServidor
        cliente_mailPassword = sistema_cliente.SenhaServidor
        cliente_mailSSL = sistema_cliente.SSL
        
        mail_EmailOrigem = request.data['EmailOrigem']
        mail_EmailDestino =  request.data['EmailDestino']
        mail_Assunto = request.data['Assunto']
        mail_Conteudo = request.data['Conteudo']

        connection = get_connection (
          host=cliente_Host, 
          port=cliente_Port, 
          username = cliente_mailUsername,
          password = cliente_mailPassword,  
          use_ssl = cliente_mailSSL,
          use_tls = False )

        try:

            EmailMessage( mail_Assunto, 
                          mail_Conteudo, 
                          mail_EmailOrigem, 
                          [mail_EmailDestino], connection = connection).send(fail_silently=False)

        except  smtplib.SMTPException as e:
                return Response({'Erro ao enviar email': str(e)})
        else:
                return Response({'Sucesso': 'Email enviado'})
        