from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.catalogoproducto, name='catalogo_producto')
]