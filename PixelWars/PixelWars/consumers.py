import json

from channels.generic.websocket import AsyncWebsocketConsumer

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

        # Faites le traitement nécessaire pour changer la couleur du pixel avec l'ID donné
        # Par exemple, vous pouvez appeler une méthode pour mettre à jour la base de données ici

        # Envoyez la nouvelle couleur à tous les clients connectés
        await self.send(text_data=json.dumps({
            'pixel_id': pixel_id,
            'color': new_color,
        }))
