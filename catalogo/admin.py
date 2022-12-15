from django.contrib import admin
from .models import Categoria


class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre_categoria',)}
    list_display = ('nombre_categoria', 'slug')    
    
    
admin.site.register(Categoria, CategoriaAdmin)
