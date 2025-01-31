# pages/urls.py
from django.urls import path
from .views import PageListView, PageDetailView, PageCreateView, PageUpdateView, PageDeleteView

app_name = 'pages'

urlpatterns = [
    path('', PageListView.as_view(), name='list'),
    path('about/', PageDetailView.as_view(), name='about'),
    path('create/', PageCreateView.as_view(), name='create'),
    path('<int:pk>/update/', PageUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', PageDeleteView.as_view(), name='delete'),
]
