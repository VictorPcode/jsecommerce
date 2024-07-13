from django.db import models
from catalogo.models import Categoria
from django.urls import reverse

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=200, unique=True)
    producto_slug = models.CharField(max_length=200, unique=True)
    descripcion = models.TextField(max_length=500, blank=True)
    precio = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')  
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        return reverse('product_detail', args=[self.categoria.slug,self.producto_slug])
    
    def __str__(self):
        return self.nombre_producto