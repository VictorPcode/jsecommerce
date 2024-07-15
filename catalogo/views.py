from django.shortcuts import get_object_or_404, render
from carrito.models import CarritoItem
from carrito.views import _carrito_id
from tienda.models import Producto
from catalogo.models import Categoria
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q


def catalogoproducto(request, slug=None):
    categorias = None
    producto = None
    
    if slug != None:
        categorias = get_object_or_404(Categoria, slug=slug)
        producto = Producto.objects.filter(categoria=categorias, is_available=True).order_by('id')
        paginator = Paginator(producto, 3)
        page = request.GET.get('page')
        paged_productos = paginator.get_page(page)
        producto_contador = producto.count()
    else:
        producto = Producto.objects.filter(is_available=True).order_by('id')
        paginator = Paginator(producto, 4)
        page = request.GET.get('page')
        paged_productos = paginator.get_page(page)
        producto_contador = producto.count()
  
    context = {
        'productos': paged_productos,
        'producto_contador': producto_contador,
        
    }
    
    
    return render(request, 'catalogoproducto.html', context)

def product_detail(request, slug, producto_slug): 
    try:
        single_product = Producto.objects.get(categoria__slug=slug, producto_slug=producto_slug)
        in_carrito = CarritoItem.objects.filter(carrito__carrito_id=_carrito_id(request), product=single_product).exists()
    except Exception as e:
        raise e
    
    context = {
        'single_product' : single_product,
        "in_carrito" : in_carrito,
    }
    
    return render(request, 'product_detail.html', context)

def search(request):
    producto = None
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        if keyword:
            producto = Producto.objects.order_by('-create_date').filter(
                Q(nombre_producto__icontains=keyword) | Q(descripcion__icontains=keyword)
            )
    
    context = {
        'productos': producto,
        'producto_contador': producto.count() if producto else 0,
    }
    return render(request, 'catalogoproducto.html', context)