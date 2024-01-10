import json
from asgiref.sync import sync_to_async,async_to_sync
from .models import ChatHistory
from django.utils import timezone

from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    def saveToDB(self,user,message,roomID):
        chat_obj = ChatHistory(sendUser=user,sendMessage=message,sendRoom=roomID)
        chat_obj.save()
    # Receive message from WebSocket
    @sync_to_async
    def receive(self, text_data): # ここでhtmlから送られた情報をもらってdbにチャットログを保存してる
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        user = text_data_json["user"]
        roomID = text_data_json["roomID"]
        
        self.saveToDB(user,message,roomID)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message, "user": user, "nowTime": str(timezone.now().astimezone().isoformat())}
        )
    

    # Receive message from room group
    async def chat_message(self, event):
        message = event["message"]
        user = event["user"]
        nowTime = event["nowTime"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message, "user": user, "nowTime": nowTime}))