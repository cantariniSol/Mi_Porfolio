from distutils.command.upload import upload
from tkinter import image_names
from django.db import models
from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField


# Create your models here.
class Proyecto(models.Model):
    titulo = CharField(max_length=100)
    descripcion = CharField(max_length=250)
    imagen = ImageField(upload_to='porfolio/imagen/')
    url = URLField(blank=True)
    
    def __str__(self):
        return 'Proyecto ' + str(self.id) + ': ' + self.titulo 
    
    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
