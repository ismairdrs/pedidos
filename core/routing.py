from django.urls import path

from .consumers import WSConsumer

ws_urlpatterns = [
    path('ws/pedido/', WSConsumer.as_asgi())
]