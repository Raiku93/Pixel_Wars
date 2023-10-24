from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        [
            path("ws/some_path/", consumers.PixelConsumer.as_asgi()),
            # Ajoutez d'autres routes WebSocket ici si nécessaire
        ]
    ),
})

