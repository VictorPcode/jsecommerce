from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('productos/', views.catalogoproducto, name='catalogo_producto'),
    path('productos/<slug:slug>', views.catalogoproducto, name='slug'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)