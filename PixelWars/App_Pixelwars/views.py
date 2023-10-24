from django.shortcuts import render
from .models import Pixel
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    pixels = Pixel.objects.all()
    return render(request, 'index.html', {'pixels': pixels})


@csrf_exempt  # désactiver la vérification CSRF pour cette vue (utilisé à des fins de démonstration)
def update_pixel_color(request, pixel_id):
    if request.method == 'POST':
        new_color = request.POST.get('color', '#000000')  # Récupère la nouvelle couleur du pixel depuis la requête POST
        try:
            pixel = Pixel.objects.get(id=pixel_id)
            pixel.color = new_color
            pixel.save()  # Met à jour la couleur du pixel dans la base de données
            return JsonResponse({'message': 'Couleur du pixel mise à jour avec succès.'})
        except Pixel.DoesNotExist:
            return JsonResponse({'message': 'Pixel non trouvé.'}, status=404)
    else:
        return JsonResponse({'message': 'Méthode non autorisée.'}, status=405)


