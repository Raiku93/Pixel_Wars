from django.shortcuts import render
from .models import Pixel

def index(request):
    pixels = Pixel.objects.all()
    return render(request, 'index.html', {'pixels': pixels})

