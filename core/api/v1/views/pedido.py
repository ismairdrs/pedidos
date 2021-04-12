import django_filters.rest_framework
from rest_framework import viewsets, mixins
from rest_framework.exceptions import ValidationError

from core.api.v1.serializer import PedidoSerializer
from core.models import Pedido


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['usuario_id',]

    def get_queryset(self):
        user = self.request.query_params.get('usuario_id')
        if user:
            queryset = Pedido.objects.filter(usuario_id=user)
        else:
            content = {'Requisição inválida': 'ID do usuário é obrigatório no query params /?usuario=id'}
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