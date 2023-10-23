import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PixelWars.settings")

# Initialisez l'application ASGI de Django tôt pour vous assurer que l'AppRegistry
# est peuplé avant d'importer du code qui peut importer des modèles ORM.
django_asgi_app = get_asgi_application()

from App_Pixelwars.consumers import PixelConsumer

application = ProtocolTypeRouter({
    # Application ASGI de Django pour gérer les requêtes HTTP traditionnelles
    "http": django_asgi_app,

    # WebSocket handler for pixel updates
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("ws/some_path/", PixelConsumer.as_asgi()),
            ])
        )
    ),
})

