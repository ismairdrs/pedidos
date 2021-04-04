from django.conf.urls import url, include
from rest_framework import routers

from core.api.v1 import views


router = routers.DefaultRouter()
router.register('', views.PedidoViewSet, basename='pedido')

urlpatterns = [
    url('', include(router.urls)),
]
