from django.contrib import admin
from django.urls import path, include
from App_Pixelwars import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  
]

