from django.contrib import admin
from .models import Producto
from .models import Variation

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto','precio','stock', 'categoria', 'modified_date', 'is_available')
    prepopulated_fields = {'producto_slug': ['nombre_producto']}


class VariationAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'variation_category', 'variation_value', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('nombre_producto', 'variation_category', 'variation_value', 'is_active')

admin.site.register(Producto, ProductoAdmin)
admin.site.register(Variation, VariationAdmin)