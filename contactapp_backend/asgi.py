# contactapp_backend/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from contacts.consumers import ContactConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'contactapp_backend.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/contacts/', ContactConsumer.as_asgi()),
        ])
    ),
})
