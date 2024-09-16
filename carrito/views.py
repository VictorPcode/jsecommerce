from django.shortcuts import render, redirect, get_object_or_404
from tienda.models import Producto, Variation
from .models import Carrito, CarritoItem
from django.core.exceptions import ObjectDoesNotExist

def _carrito_id(request):
    carrito = request.session.session_key
    if not carrito:
        carrito = request.session.create()
    return carrito

def agregarCarrito(request, product_id):
    product = get_object_or_404(Producto, id=product_id)
    product_variation = []
    print('product_variation ---> ', product_variation)
    if request.method == 'POST':
        print("POST data:", request.POST)
        for key in request.POST:
            if key == 'csrfmiddlewaretoken':
                continue
            value = request.POST[key]
            print(f"Checking for variation - Category: {key}, Value: {value}")
            try:
                variation = Variation.objects.get(
                    nombre_producto=product,
                    variation_category__iexact=key,
                    variation_value__iexact=value
                )
                product_variation.append(variation)
                print(f"Variation found: {variation}")
            except Variation.DoesNotExist:
                print(f"No variation found for category '{key}' with value '{value}'")
            except Exception as e:
                print(f"Error retrieving variation: {e}")

        print("Product variations after loop:", product_variation)

    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
    except Carrito.DoesNotExist:
        carrito = Carrito.objects.create(carrito_id=_carrito_id(request))
        carrito.save()

    is_cart_item_exists = CarritoItem.objects.filter(
        product=product,
        carrito=carrito
    ).exists()

    if is_cart_item_exists:
        cart_items = CarritoItem.objects.filter(
            product=product,
            carrito=carrito
        )
        existing_variation_list = [list(item.variations.all()) for item in cart_items]

        if product_variation in existing_variation_list:
            index = existing_variation_list.index(product_variation)
            item_id = cart_items[index].id
            item = CarritoItem.objects.get(id=item_id)
            item.cantidad += 1
            item.save()
        else:
            item = CarritoItem.objects.create(
                product=product,
                cantidad=1,
                carrito=carrito
            )
            if len(product_variation) > 0:
                item.variations.clear()
                item.variations.add(*product_variation)
            item.save()
    else:
        cart_item = CarritoItem.objects.create(
            product=product,
            cantidad=1,
            carrito=carrito
        )
        if len(product_variation) > 0:
            cart_item.variations.clear()
            cart_item.variations.add(*product_variation)
        cart_item.save()

    return redirect('carrito:carrito')

def remover_carritoItem(request, product_id, carrito_item_id):
    carrito = get_object_or_404(Carrito, carrito_id=_carrito_id(request))
    product = get_object_or_404(Producto, id=product_id)
    try:
        carrito_item = CarritoItem.objects.get(product=product, carrito=carrito, id=carrito_item_id)
        if carrito_item.cantidad > 1:
            carrito_item.cantidad -= 1
            carrito_item.save()
        else:
            carrito_item.delete()
    except CarritoItem.DoesNotExist:
        pass

    return redirect('carrito:carrito')

def carrito(request, total=0, cantidad=0, carritoItem=None):
    try:
        carrito = Carrito.objects.get(carrito_id=_carrito_id(request))
        carritoItem = CarritoItem.objects.filter(carrito=carrito, is_active=True)
        for item in carritoItem:
            total += (item.product.precio * item.cantidad)
            cantidad += item.cantidad

        iva = (2 * total) / 100
        grand_total = total + iva
    except ObjectDoesNotExist:
        iva = 0
        grand_total = 0

    formatted_total = f"{total:,.0f}".replace(",", ".")
    formatted_iva = f"{iva:,.0f}".replace(",", ".")
    formatted_grand_total = f"{grand_total:,.0f}".replace(",", ".")

    context = {
        'total': formatted_total,
        'cantidad': cantidad,
        'carritoItems': carritoItem,
        'iva': formatted_iva,
        'grand_total': formatted_grand_total,  # Usa el valor formateado aquí
    }

    return render(request, 'carrito.html', context)

def eliminar_del_carrito(request, producto_slug, item_id):
    carrito = get_object_or_404(Carrito, carrito_id=_carrito_id(request))
    producto = get_object_or_404(Producto, producto_slug=producto_slug)

    try:
        carrito_item = CarritoItem.objects.get(product=producto, carrito=carrito, id=item_id)
        carrito_item.delete()
    except CarritoItem.DoesNotExist:
        pass

    return redirect('carrito:carrito')
