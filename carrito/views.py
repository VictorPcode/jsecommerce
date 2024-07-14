from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto
from .models import Carrito, CarritoItem
from django.core.exceptions import ObjectDoesNotExist


 #funcion privada  para usarla en este view
def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregarCarrito(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    try:
        #este carrito id sera la session actual que viene de la funcion privada _carrito_id
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(carrito_id=_carrito_id(request))
        carrito.save()

    try:
        carrito_item = CarritoItem.objects.get(product=product, carrito=carrito)
        carrito_item.cantidad += 1
        carrito_item.save()
    except CarritoItem.DoesNotExist:
        carrito_item = CarritoItem.objects.create(
            product=product,
            cantidad=1,
            carrito=carrito,
        )
        carrito_item.save()

    return redirect('carrito')

def remover_carritoItem(request, product_id):
    carrito = get_object_or_404(Carrito, carrito_id=_carrito_id(request))
    product = get_object_or_404(Producto, id=product_id)
    try:
        carrito_item = CarritoItem.objects.get(product=product, carrito=carrito)
        if carrito_item.cantidad > 1:
            carrito_item.cantidad -= 1
            carrito_item.save()
        else:
            carrito_item.delete()
    except CarritoItem.DoesNotExist:
        pass

    return redirect('carrito')

def carrito(request, total=0, cantidad=0, carritoItem=None):
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        carritoItem = CarritoItem.objects.filter(carrito=carrito, is_active=True) #carrito= ... en carritoItem es igual a carrito que se define en la linea anterior 
        for item in carritoItem:   #este for es para ver elprecio total de los producto y la cantidad de productos en el carrito de compra
            total += (item.product.precio * item.cantidad)
            cantidad += item.cantidad

        iva = (2 * total) / 100
        grand_total = total + iva
    except ObjectDoesNotExist:
        iva = 0
        grand_total = 0

    context = {
        'total': total,
        'cantidad': cantidad,
        'carritoItems': carritoItem,
        'iva': iva,
        'grand_total': grand_total,
    }

    return render(request, 'carrito.html', context)

def eliminar_del_carrito(request, producto_slug):
    carrito = get_object_or_404(Carrito, carrito_id=_carrito_id(request))
    producto = get_object_or_404(Producto, producto_slug=producto_slug)
    try:
        carrito_item = CarritoItem.objects.get(product=producto, carrito=carrito)
        carrito_item.delete()
    except CarritoItem.DoesNotExist:
        pass

    return redirect('carrito')
