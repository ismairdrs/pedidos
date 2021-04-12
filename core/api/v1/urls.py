from django.conf.urls import url, include
from rest_framework import routers

from core.api.v1 import views
from core.api.v1.views.pedido import PedidoNaoEntregueViewSet

router = routers.DefaultRouter()
router.register('restaurante', PedidoNaoEntregueViewSet, basename='pedidos-restaurante')
router.register('', views.PedidoViewSet, basename='pedido')


urlpatterns = [
    url('', include(router.urls)),
]
