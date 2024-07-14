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
    

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def talla(self):
        return super(VariationManager, self).filter(variation_category='talla', is_active=True)

variation_category_choice = (
    ('color', 'color'),
    ('talla', 'talla'),
)
class Variation(models.Model):
    nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length=100, choices=(variation_category_choice))
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now=True)
    
    objects = VariationManager()
    
    def __unicode__(self):
        return self.nombre_producto 