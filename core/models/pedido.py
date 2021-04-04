import uuid

from django.db import models


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario_id = models.UUIDField(default=uuid.uuid4, editable=True)
    endereco_id = models.UUIDField(default=uuid.uuid4, editable=True)
    pizza_id = models.IntegerField()
    pedido_entregue = models.BooleanField(default=False)
