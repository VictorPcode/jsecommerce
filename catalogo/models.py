from django.db import models

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255, blank =True)
    slug = models.CharField(max_length=100, unique=True)
    cat_image = models.ImageField(upload_to='photos/categories', blank=True)
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.nombre_categoria 
    
