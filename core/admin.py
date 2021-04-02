from django.contrib import admin

from core.models.pedido import Pedido


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_id', 'endereco_id', 'pizza_id', 'pedido_entregue',)
