from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('eventos/', include('eventos.urls')),
    path('cliente/', include('clientes.urls'))]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
