from django.shortcuts import render
from tienda.models import Producto

def catalogoproducto(request):
    
    producto = Producto.objects.all().filter(is_available=True)
    
    context = {
        'productos': producto,
    }
    return render(request, 'catalogoproducto.html', context)