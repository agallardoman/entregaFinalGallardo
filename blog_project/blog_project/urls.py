from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Rutas de autenticación y perfil
    path('', include('blog.urls')),  # Rutas del blog
]
