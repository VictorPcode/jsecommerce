from django.urls import path
from . import views

urlpatterns = [
    path('',views.carrito, name='carrito'),
    path('agregarcarrito/<int:product_id>/', views.agregarCarrito, name='agregarCarrito')
]