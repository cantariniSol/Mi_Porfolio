from django.shortcuts import render
from .models import Proyecto

# Create your views here.

#Vista INICIO
def inicio(request):
    return render(request, 'inicio.html')

#Vista HOME
def home(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'home.html', {'proyectos': proyectos})

#Vista CONTACTO
def contacto(request):
    return render(request, 'contacto.html')