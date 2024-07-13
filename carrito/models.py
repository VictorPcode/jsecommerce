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
    
    
<<<<<<< HEAD
    def subtotal(self):
        
        return self.product.precio * self.cantidad
        
    def __unicodes__(self):
=======
    def sub_total(self):
        return self.product.precio * self.cantidad
    
    def __unicode__(self):
>>>>>>> 5f80bc760dd46574259e28fd7c94b34b6f6c0d81
        return self.product