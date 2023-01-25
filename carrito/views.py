from django.shortcuts import render, redirect
from tienda.models import Producto
from  .models import Carrito, CarritoItem
from django.core.exceptions import ObjectDoesNotExist


def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito


def agregarCarrito(request, product_id):
    product = Producto.objects.get(id=product_id)
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(
            carrito_id = _carrito_id(request)
        )
        carrito.save()
        
        try:
            carrito_item = CarritoItem.objects.get(product=product, carrito=carrito)
            carrito_item.cantidad +=1
            carrito_item.save()
        except CarritoItem.DoesNotExist:
            carrito_item = CarritoItem.objects.create(
                product = product,
                cantidad = 1,
                carrito = carrito
            )
            carrito_item.save
            
        return redirect('carrito')
            
def carrito(request, total=0,cantidad=0,carritoItem=None):
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        carritoItem = CarritoItem.objects.filter(carrito=carrito, is_active=True)
        for carritoItems in carritoItem:
            total += (carritoItems.product.precio * carritoItems.cantidad)
            cantidad += carritoItems.cantidad
        iva = (2*total)/100
        granTotal = total + iva
    
    except ObjectDoesNotExist:
        pass #ignorando el except
        
    context = {
        'total' : total,
        'cantidad' : cantidad,
        'carritoItem' : carritoItem,
        'iva' : iva,
        'granTotal' : granTotal,
        
    }
    
    return render(request, 'carrito.html', context)
