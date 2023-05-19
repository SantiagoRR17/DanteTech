from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Productos
# Create your views here.
def index(request):
    mensaje = "<title>Lorem Ipsum DB</title> <h1>Lorem Ipsum Test DB Django</h1><p>Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de <Strong>texto</strong>. Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la creación de las hojas </p>"
    productos = Productos.objects.all()

    return render(
        request,
        'index.html',
        context= {'productos': productos}
    )