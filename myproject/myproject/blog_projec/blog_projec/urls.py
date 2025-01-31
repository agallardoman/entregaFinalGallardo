# blog_project/urls.py
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),  # Agrega las URLs de la app de cuentas
]
