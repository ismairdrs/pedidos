import requests as requests
from django.core.exceptions import PermissionDenied


class ProxyMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        proxy = Proxy()
        if proxy.validar_token(request):
            return self.get_response(request)
        else:
            raise PermissionDenied(f'Operação não permitida: {request.headers["Authorization"]}')



class Proxy():
    def validar_token(self, request):
        headers = {
            "Authorization": None
        }
        url = 'http://pizzaria-fasam.herokuapp.com/validar-token/'
        headers['Authorization'] = f"{request.headers['Authorization']}"
        result = requests.get(url, headers=headers)

        if result.status_code == 200:
            return True
        else:
            return False
