from .models import Producto
from django.shortcuts import render, get_object_or_404

def producto_list(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/producto_list.html', {'productos': productos})

def producto_detalle(request, pk):
    # Obtener el producto con el ID proporcionado (pk) o devolver un error 404 si no se encuentra
    producto = get_object_or_404(Producto, pk=pk)
    # Renderizar la plantilla producto_detalle.html con el producto obtenido
    return render(request, 'tienda/producto_detalle.html', {'producto': producto})

