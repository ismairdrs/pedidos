import time
import pusher
from rest_framework.response import Response
from core.models import Pedido
from rest_framework import status
from rest_framework.exceptions import ValidationError


def websocket(request, id):
    STATUS = [
        'Preparando envio do pedido',
        'Pedido recebido pelo restaurante',
        'Sua pizza está sendo preparada...',
        'Pizza pronta! Saindo para a entrega...',
        'Seu pedido está chegando...',
        'Pedido Entregue!'
    ]

    def create_connection():
        pusher_client = pusher.Pusher(
            app_id='1193493',
            key='be00d08867dbcda17eb3',
            secret='693bb2a1cba35d01c782',
            cluster='mt1',
            ssl=True
        )
        return pusher_client

    def send_message(pusher_client):
        time.sleep(5)
        for status in STATUS:
            pusher_client.trigger('my-channel', 'my-event', {'message': status})
            time.sleep(1)

    def mudar_status_pedido(id):
        try:
            pedido = Pedido.objects.get(id=id)
            pedido.pedido_entregue = True
            pedido.save()
        except:
            content = {'Requisição inválida': 'ID do pedido inválido'}
            raise ValidationError(content)

    def main():
        pusher_client = create_connection()
        send_message(pusher_client)
        mudar_status_pedido(id)

    main()
    data= {"websocket": "success"}
    return Response(data, status=status.HTTP_200_OK)
