
import django_filters.rest_framework
from rest_framework import viewsets, mixins
from rest_framework.exceptions import ValidationError

from core.api.v1.serializer import PedidoSerializer

from core.models import Pedido


class PedidoViewSet(viewsets.ModelViewSet):
    serializer_class = PedidoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

    def get_queryset(self):
        usuario = self.request.query_params.get('usuario')
        if usuario:
            queryset = self.buscar_pedido(usuario)
        else:
            content = {'Requisição inválida': 'ID do usuário é obrigatório no query params /?usuario=id'}
            raise ValidationError(content)
        return queryset

    def buscar_pedido(self, usuario):
        try:
            queryset = Pedido.objects.filter(usuario_id=usuario)
        except:
            content = {'error': 'ID inválido'}
            raise ValidationError(content)
        return queryset


class PedidoNaoEntregueViewSet(mixins.ListModelMixin,
                               mixins.RetrieveModelMixin,
                               mixins.UpdateModelMixin,
                               viewsets.GenericViewSet):

    serializer_class = PedidoSerializer

    def get_queryset(self):
        pedidos = Pedido.objects.filter(pedido_entregue=False)
        return pedidos