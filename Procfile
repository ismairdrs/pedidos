web: gunicorn pedidos.wsgi
release: python manage.py migrate
web: daphne pedidos.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker channels --settings=pedidos.settings -v2