import os
from django.core.asgi import get_asgi_application
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from api.consumers import VacancyConsumer


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hh_back.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path('ws/vacancies/submit/', VacancyConsumer.as_asgi()),
        ])
    ),
})
