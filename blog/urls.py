from django.urls import path
from . import views
# Nombre blog es una variable que hace referencia a cada post
app_name = 'blog'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:post_id>', views.post_detail, name='post_detail'),
]