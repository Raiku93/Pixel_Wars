from django.db import models

class Pixel(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    color = models.CharField(max_length=7)  # Stocke la couleur au format HEX (#RRGGBB)

