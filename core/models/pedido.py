import uuid

from django.db import models


class Pedido(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario_id = models.CharField(max_length=100)
    endereco_id = models.CharField(max_length=100)
    pizza_id = models.CharField(max_length=100)
    pedido_entregue = models.BooleanField(default=False)
