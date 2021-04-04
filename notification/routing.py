from . import consumers
from django.urls import re_path


websocket_urlpatterns = [
    re_path(r'notify/$', consumers.NotificationWebConsumer.as_asgi()),
]