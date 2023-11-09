from django.test import TestCase
from django.urls import reverse
from .models import Pixel

class PixelWarsTestCase(TestCase):
    def setUp(self):
        Pixel.objects.create(x=1, y=1, color='#FFFFFF')

    def test_pixel_creation(self):
        pixel = Pixel.objects.get(x=1, y=1)
        self.assertEqual(pixel.color, '#FFFFFF')

    def test_pixel_list_view(self):
        response = self.client.get(reverse('pixel_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pixel Wars')
        self.assertQuerysetEqual(response.context['pixels'], ['<Pixel: Pixel object (1, 1)>'])

    def test_pixel_detail_view(self):
        pixel = Pixel.objects.get(x=1, y=1)
        response = self.client.get(reverse('pixel_detail', args=[pixel.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Pixel Details')
        self.assertEqual(response.context['pixel'], pixel)

    def test_create_pixel_view(self):
        response = self.client.post(reverse('create_pixel'), {'x': 2, 'y': 2, 'color': '#FF0000'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Pixel.objects.filter(x=2, y=2, color='#FF0000').exists())

    def test_update_pixel_view(self):
        pixel = Pixel.objects.get(x=1, y=1)
        response = self.client.post(reverse('update_pixel', args=[pixel.id]), {'x': 1, 'y': 1, 'color': '#000000'})
        self.assertEqual(response.status_code, 302)
        updated_pixel = Pixel.objects.get(id=pixel.id)
        self.assertEqual(updated_pixel.color, '#000000')

    def test_delete_pixel_view(self):
        pixel = Pixel.objects.get(x=1, y=1)
        response = self.client.post(reverse('delete_pixel', args=[pixel.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Pixel.objects.filter(id=pixel.id).exists())
