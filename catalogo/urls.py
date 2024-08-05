from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import obtener_imagen_variacion

app_name = 'catalogo'


urlpatterns = [
    path('productos/search/', views.search, name='search'),
    path('productos/', views.catalogoproducto, name='catalogo_producto'),
    path('productos/<slug:slug>/', views.catalogoproducto, name='slug'),
    path('productos/<slug:slug>/<slug:producto_slug>/', views.product_detail, name='product_detail'),
    path('obtener-imagen-variacion/<int:variacion_id>/', obtener_imagen_variacion, name='obtener_imagen_variacion'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
