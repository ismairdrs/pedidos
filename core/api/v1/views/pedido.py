from rest_framework import viewsets

from core.api.v1.serializer import PedidoSerializer
from core.models import Pedido


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
