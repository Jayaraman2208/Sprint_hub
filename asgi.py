import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from core.consumers import TaskConsumer, NotificationConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sprint_hub.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/tasks/', TaskConsumer.as_asgi()),
            path('ws/notifications/', NotificationConsumer.as_asgi()),
        ])
    ),
})
