import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model
from .models import Task, Notification, ActivityLog

User = get_user_model()

class TaskConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'task_updates'
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')

        if message_type == 'task_update':
            await self.handle_task_update(data)
        elif message_type == 'notification':
            await self.handle_notification(data)

    async def handle_task_update(self, data):
        task_id = data.get('task_id')
        action = data.get('action')
        
        if task_id:
            task = await self.get_task(task_id)
            if task:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'task_update_message',
                        'task': {
                            'id': task.id,
                            'title': task.title,
                            'status': task.status,
                            'priority': task.priority,
                            'action': action
                        }
                    }
                )

    async def handle_notification(self, data):
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'notification_message',
                'message': data.get('message', ''),
                'notification_type': data.get('notification_type', 'info')
            }
        )

    async def task_update_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'task_update',
            'data': event['task']
        }))

    async def notification_message(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'notification_type': event['notification_type']
        }))

    @database_sync_to_async
    def get_task(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        if self.user.is_authenticated:
            self.room_group_name = f'user_{self.user.id}'
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )

    async def send_notification(self, event):
        await self.send(text_data=json.dumps({
            'type': 'notification',
            'message': event['message'],
            'notification_type': event['notification_type'],
            'data': event.get('data', {})
        }))
