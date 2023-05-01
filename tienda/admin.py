from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','stock', 'categoria', 'modified_date', 'is_available')
    prepopulated_fields = {'producto_slug': ['nombre_producto']}

admin.site.register(Producto, ProductoAdmin)