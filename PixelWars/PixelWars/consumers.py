from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from App_Pixelwars.models import Pixel
import json

class PixelConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("WebSocket Connected")
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        pixel_id = data.get('pixel_id')
        new_color = data.get('color')

        # Utilisez database_sync_to_async pour rendre l'opération de base de données asynchrone
        pixel = await self.get_pixel_from_db(pixel_id)
        if pixel:
            # Mettez à jour la couleur et enregistrez le pixel dans la base de données
            pixel.color = new_color
            await database_sync_to_async(pixel.save)()
            # Envoyez la nouvelle couleur à tous les clients connectés
            await self.send_new_color_to_clients(pixel_id, new_color)

    async def get_pixel_from_db(self, pixel_id):
        # Utilisez database_sync_to_async pour rendre la recherche du pixel asynchrone
        return await database_sync_to_async(Pixel.objects.get)(id=pixel_id)

    async def send_new_color_to_clients(self, pixel_id, new_color):
        # Envoyez la nouvelle couleur à tous les clients connectés dans le groupe 'pixel_group'
        await self.channel_layer.group_add('pixel_group', self.channel_name)
        await self.channel_layer.group_send(
            'pixel_group',
            {
                'type': 'pixel.color_updated',
                'pixel_id': pixel_id,
                'color': new_color,
            }
        )

    async def pixel_color_updated(self, event):
        # Envoyez la nouvelle couleur à tous les clients dans le groupe 'pixel_group'
        await self.send(text_data=json.dumps({
            'pixel_id': event['pixel_id'],
            'color': event['color'],
        }))

