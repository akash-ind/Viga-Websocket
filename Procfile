web: daphne Notify.asgi:application --port $PORT --bind 0.0.0.0 -v2
worker: python manage.py runworker --settings=Notify.settings -v2
