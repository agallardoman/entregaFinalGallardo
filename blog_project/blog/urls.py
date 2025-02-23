from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_list, name='page_list'),
    path('page/<int:pk>/', views.page_detail, name='page_detail'),
    path('create/', views.page_create, name='page_create'),
    path('update/<int:pk>/', views.page_update, name='page_update'),
    path('delete/<int:pk>/', views.page_delete, name='page_delete'),
    path('about/', views.about_view, name='about'),  # Ruta para "Acerca de mí"
]
