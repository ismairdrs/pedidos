from django.conf.urls import url, include
from rest_framework import routers
from django.urls import path
from core.api.v1 import views
from core.api.v1.views.pedido import PedidoNaoEntregueViewSet
from core.api.v1.views.websocket import websocket

router = routers.DefaultRouter()
router.register('restaurante', PedidoNaoEntregueViewSet, basename='pedidos-restaurante')
router.register('pedidos', views.PedidoViewSet, basename='pedido')


urlpatterns = [
    url('', include(router.urls)),
    path('pedido/<int:id>/websocket/', websocket),
]
