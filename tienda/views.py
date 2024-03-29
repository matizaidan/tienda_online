from django.shortcuts import render
from .models import Producto

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_list.html', {'producto': productos})

