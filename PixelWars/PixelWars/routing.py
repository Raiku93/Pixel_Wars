from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/some_path/', consumers.PixelConsumer),
]

application = ProtocolTypeRouter({
    "websocket": URLRouter(websocket_urlpatterns),
})

