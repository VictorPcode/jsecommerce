from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'catalogo'


urlpatterns = [
    path('productos/search/', views.search, name='search'), 
    path('productos/', views.catalogoproducto, name='catalogo_producto'),
    path('productos/<slug:slug>/', views.catalogoproducto, name='slug'),
    path('productos/<slug:slug>/<slug:producto_slug>/', views.product_detail, name='product_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)