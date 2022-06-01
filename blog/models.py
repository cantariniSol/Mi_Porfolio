from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion=models.TextField()
    imagen = models.ImageField(upload_to='blog/imagen')
    fecha = models.DateField()
    
    def __str__(self):
        return 'Post ' + str(self.id) + ': ' +  self.titulo
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
