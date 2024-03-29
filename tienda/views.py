from .models import Producto
from django.shortcuts import render

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_list.html', {'productos': productos})
