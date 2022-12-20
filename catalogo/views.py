from django.shortcuts import get_object_or_404, render
from tienda.models import Producto
from catalogo.models import Categoria


def catalogoproducto(request, slug=None):
    categorias = None
    producto = None
    
    if slug != None:
        categorias = get_object_or_404(Categoria, slug=slug)
        producto = Producto.objects.filter(categoria=categorias, is_available=True)
        producto_contador = producto.count()
    else:
        producto = Producto.objects.filter(is_available=True)
        producto_contador = producto.count()
  
    context = {
        'productos': producto,
        'producto_contador': producto_contador,
        
    }
    
    
    return render(request, 'catalogoproducto.html', context)