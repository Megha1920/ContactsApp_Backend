# contacts/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ContactConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'contacts_group'

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        contact_id = text_data_json.get('contact_id')

        # Broadcast the message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'contact_update',
                'action': action,
                'contact_id': contact_id,
            }
        )

    async def contact_update(self, event):
        action = event['action']
        contact_id = event['contact_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'action': action,
            'contact_id': contact_id,
        }))
