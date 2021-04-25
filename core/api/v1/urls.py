from django.conf.urls import url, include
from rest_framework import routers
from core.api.v1 import views
from core.api.v1.views.pedido import PedidoNaoEntregueViewSet
from core.api.v1.views.websocket import WebsocketAPIView

router = routers.DefaultRouter()
router.register('restaurante', PedidoNaoEntregueViewSet, basename='pedidos-restaurante')
router.register('pedido', views.PedidoViewSet, basename='pedido')

urlpatterns = [
    url(r'websocket/', WebsocketAPIView.as_view(), name='websocket'),
    url('', include(router.urls)),
]
