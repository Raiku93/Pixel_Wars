from django.contrib import admin
from django.urls import path
from App_Pixelwars import views
from PixelWars import consumers  
from channels.routing import ProtocolTypeRouter, URLRouter

websocket_urlpatterns = [
    path('ws/some_path/', consumers.PixelConsumer),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('update_pixel_color/<int:pixel_id>/', views.update_pixel_color, name='update_pixel_color'),
    
]

