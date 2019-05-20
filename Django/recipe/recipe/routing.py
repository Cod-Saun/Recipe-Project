from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import recipeApp.routing

application = ProtocolTypeRouter({
  'websocket': AuthMiddlewareStack(
        URLRouter(
            recipeApp.routing.websocket_urlpatterns
        )
    ),
  })
