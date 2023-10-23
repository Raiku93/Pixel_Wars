import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.layers import get_channel_layer
from django.urls import re_path
from . import consumers 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PixelWars.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        re_path('ws/some_path/', consumers.PixelConsumer.as_asgi()),
    ]),
})


