from django.shortcuts import get_object_or_404, render
from carrito.models import CarritoItem
from carrito.views import _carrito_id
from tienda.models import Producto
from catalogo.models import Categoria
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from tienda.models import Variation
from django.http import JsonResponse


def catalogoproducto(request, slug=None):
    categorias = None
    producto = None

    if slug != None:
        categorias = get_object_or_404(Categoria, slug=slug)
        producto = Producto.objects.filter(categoria=categorias, is_available=True).order_by('id')
        print(producto)
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

from django.shortcuts import get_object_or_404, render
from carrito.models import CarritoItem
from carrito.views import _carrito_id
from tienda.models import Producto, Variation
from catalogo.models import Categoria



def product_detail(request, slug, producto_slug):
    single_product = get_object_or_404(Producto, categoria__slug=slug, producto_slug=producto_slug)
    in_carrito = CarritoItem.objects.filter(carrito__carrito_id=_carrito_id(request), product=single_product).exists()

    color_variations = single_product.variation_set.filter(variation_category='color')
    talla_variations = single_product.variation_set.filter(variation_category='talla')

    # Inicializar la URL de la imagen principal
    imagen_url = single_product.images.url if single_product.images else None

    context = {
        'single_product': single_product,
        'in_carrito': in_carrito,
        'imagen_url': imagen_url,
        'color_variations': color_variations,
        'talla_variations': talla_variations,
    }

    return render(request, 'product_detail.html', context)

def obtener_imagen_variacion(request, variacion_id):
    variacion = get_object_or_404(Variation, id=variacion_id)
    imagen_url = variacion.imagen.url if variacion.imagen else ''
    return JsonResponse({'imagen_url': imagen_url})


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
