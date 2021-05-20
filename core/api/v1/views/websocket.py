import time
import pusher
from core.models import Pedido
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response


class WebsocketConnection():
    _STATUS = [
        'Preparando envio do pedido',
        'Pedido recebido pelo restaurante',
        'Sua pizza está sendo preparada...',
        'Pizza pronta! Saindo para a entrega...',
        'Seu pedido está chegando...',
        'Pedido Entregue!'
    ]

    def criar_conecao(self):
        self.pusher_client = pusher.Pusher(
            app_id='1193493',
            key='be00d08867dbcda17eb3',
            secret='693bb2a1cba35d01c782',
            cluster='mt1',
            ssl=True
        )
        return self.pusher_client

    def enviar_status(self):
        time.sleep(1)
        for status in self._STATUS:
            self.pusher_client.trigger('my-channel', 'my-event', {'message': status})
            time.sleep(5)


class WebsocketAPIView(APIView):
    def get(self, request, form=None):
        id = self.request.query_params.get('id')
        pedido = self.encontrar_pedido(id)

        if not pedido:
            content = {'Requisição inválida': 'ID do pedido inválido'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if pedido.pedido_entregue:
            content = {'Status pedido': 'Pedido Entregue'}
            return Response(content, status=status.HTTP_200_OK)

        self.enviar_status_websocket()
        self.alterar_status_pedido(pedido)

        data = {"websocket": "success"}
        return Response(data, status=status.HTTP_200_OK)

    def encontrar_pedido(self, id):
        try:
            return Pedido.objects.get(id=id)
        except:
            return False

    def enviar_status_websocket(self):
        websocket = WebsocketConnection()
        websocket.criar_conecao()
        websocket.enviar_status()

    def alterar_status_pedido(self, pedido):
        pedido.pedido_entregue = True
        pedido.save()