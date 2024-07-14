from .models import Carrito, CarritoItem
from .views import _carrito_id
from django.core.exceptions import ObjectDoesNotExist

def counter(request):
    carrito_count = 0

    try:
        carrito_id = _carrito_id(request)
        carrito = Carrito.objects.get(carrito_id=carrito_id)
        carrito_items = CarritoItem.objects.filter(carrito=carrito)
        for carrito_item in carrito_items:
            carrito_count += carrito_item.cantidad
    except Carrito.DoesNotExist:
        carrito_count = 0

    return dict(carrito_count=carrito_count)
