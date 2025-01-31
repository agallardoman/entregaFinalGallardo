# pages/models.py
from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()  # Para el contenido con formato enriquecido
    image = models.ImageField(upload_to='pages_images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
