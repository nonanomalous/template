import os
import environ

env = environ.Env()
environ.Env.read_env()

from django.core.asgi import get_asgi_application
httpApp = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

#from my_app.routing import ws_urlpatterns
#'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', env("SETTINGS_ENV"))

application = ProtocolTypeRouter({
    'http': httpApp,
})