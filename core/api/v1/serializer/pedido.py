from rest_framework import serializers
from core.models import Pedido


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = [kwargs['context']['request'].query_params.get('fields')]

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields[0] is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class PedidoSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Pedido
        fields = ['id', 'usuario_id', 'endereco_id', 'pizza_id', 'pedido_entregue']
