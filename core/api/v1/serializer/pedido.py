from rest_framework import serializers

from core.models import Pedido


class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pedido
        fields = ('id', 'usuario_id', 'endereco_id', 'pizza_id', 'pedido_entregue')
