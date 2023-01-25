from django.db import models
from tienda.models import Producto


class Carrito (models.Model):
    carrito_id = models.CharField(max_length=250, blank=True)
    fecha_agregado = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.carrito_id
    
class CarritoItem(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    is_active = models.BooleanField(default=True)
    
    
    def subtotal(self):
        
        return self.product.precio * self.cantidad
        
    def __unicodes__(self):
        return self.product