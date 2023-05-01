from django.shortcuts import render, redirect
from tienda.models import Producto
from  .models import Carrito, CarritoItem


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
            
def carrito(request):
    return render(request, 'carrito.html')