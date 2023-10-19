from django.core.management.base import BaseCommand
from App_Pixelwars.models import Pixel

class Command(BaseCommand):
    help = 'Réinitialiser la base de données'

    def handle(self, *args, **options):
        # Supprimez tous les pixels existants dans la base de données
        Pixel.objects.all().delete()
        nombre = 1
        pixels_to_create = []
        for row in range(130):
            for column in range(40):
                print("Pixel", nombre, "créé !")
                nombre = nombre+1
                pixel = Pixel(row=row, column=column, color='#FFFFFF')
                pixels_to_create.append(pixel)

        # Utilisez bulk_create pour insérer les pixels en une seule requête SQL
        Pixel.objects.bulk_create(pixels_to_create, batch_size=100)  # Vous pouvez ajuster la taille du lot (batch_size) selon votre besoin

        self.stdout.write(self.style.SUCCESS('Base de données remplie !'))

