import time
import pusher
from core.models import Pedido
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.views import APIView
from rest_framework.response import Response


class WebsocketAPIView(APIView):
    def get(self, request, format=None):
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
            time.sleep(1)
            for status in STATUS:
                pusher_client.trigger('my-channel', 'my-event', {'message': status})
                time.sleep(1)

        def mudar_status_pedido(id):
            pedido = Pedido.objects.get(id=id)
            if pedido.pedido_entregue:
                return False
            else:
                pedido.pedido_entregue = True
                pedido.save()

        id = self.request.query_params.get('id')
        try:
            mudar_status_pedido(id)
        except:
            content = {'Requisição inválida': 'ID do pedido inválido'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        pusher_client = create_connection()
        send_message(pusher_client)

        data = {"websocket": "success"}
        return Response(data, status=status.HTTP_200_OK)




@api_view(['GET'])
def websocket(request):
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
            time.sleep(5)

    def mudar_status_pedido(id):
        try:
            pedido = Pedido.objects.get(id=id)
        except:
            content = {'Requisição inválida': 'ID do pedido inválido'}
            #raise ValidationError(content, status=status.HTTP_400_BAD_REQUEST)
            pass
        else:
            pedido.pedido_entregue = True
            pedido.save()

    def main():
        mudar_status_pedido(id)
        pusher_client = create_connection()
        send_message(pusher_client)

    main()
    data= {"websocket": "success"}
    return Response(data, status=status.HTTP_200_OK)

@api_view(['GET'])
def websocket(request):
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
            time.sleep(5)

    def mudar_status_pedido(id):
        try:
            pedido = Pedido.objects.get(id=id)
        except:
            content = {'Requisição inválida': 'ID do pedido inválido'}
            #raise ValidationError(content, status=status.HTTP_400_BAD_REQUEST)
            pass
        else:
            pedido.pedido_entregue = True
            pedido.save()

    def main():
        mudar_status_pedido(id)
        pusher_client = create_connection()
        send_message(pusher_client)

    main()
    data= {"websocket": "success"}
    return Response(data, status=status.HTTP_200_OK)
