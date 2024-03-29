from .models import Producto
from django.shortcuts import render

def producto_list(request):
    productos = Producto.objects.all()

    # Imprimir los productos en la consola
    for producto in productos:
        print(producto.nombre)  # O cualquier otro campo que desees imprimir

    return render(request, 'tienda/producto_list.html', {'productos': productos})
