from django.urls import path
from . import views


from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('home', views.home, name='home'),
    path('contacto', views.contacto, name='contacto'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 