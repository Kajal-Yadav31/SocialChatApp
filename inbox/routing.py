from django.urls import path
from inbox.consumers import PersonalChatConsumer

websocket_urlpatterns = [
    path('ws/<int:id>/', PersonalChatConsumer.as_asgi()),
]
