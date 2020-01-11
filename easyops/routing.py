from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import webssh.routing
from channels.security.websocket import AllowedHostsOriginValidator


application = ProtocolTypeRouter({
    'websocket': AllowedHostsOriginValidator(
    AuthMiddlewareStack(
        URLRouter(
            webssh.routing.websocket_urlpatterns
        )
    ),
    ),
})
