from channels.generic.websocket import AsyncWebsocketConsumer
import json
from asgiref.sync import sync_to_async
from channels.consumer import AsyncConsumer
from django.contrib.auth import get_user_model

User = get_user_model


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self, event):
        print('connect', event)
        await self.send({
            'type': 'websocket.accept'
        })

    async def receive(self, event):
        print('receive', event)
        received_data = json.loads(event['text'])
        msg = received_data.get('message')
        if not msg:
            return False

        response = {
            'message': msg
        }

        await self.send({
            'type': 'websocket.send',
            'text': json.dumps(response)
        })

    async def disconnect(self, event):
        print('disconnect', event)
