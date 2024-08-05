from django.urls import path
from . import views

app_name = 'carrito'

urlpatterns = [
    path('', views.carrito, name='carrito'),
    path('agregarcarrito/<int:product_id>/', views.agregarCarrito, name='agregarCarrito'),
    path('remover_carritoItem/<int:product_id>/<int:carrito_item_id>/', views.remover_carritoItem, name='remover_carritoItem'),
    path('eliminar/<slug:producto_slug>/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
]
