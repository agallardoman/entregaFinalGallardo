from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from .forms import PageForm
from django.contrib.auth.decorators import login_required

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'blog/page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'blog/page_detail.html', {'page': page})

@login_required
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'blog/page_form.html', {'form': form})

@login_required
def page_update(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/page_form.html', {'form': form})

@login_required
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    page.delete()
    return redirect('page_list')
# Vista para mostrar "Acerca de mí"
def about_view(request):
    # Información sobre el dueño del sitio
    context = {
        'name': 'Andres Gallardo',
        'bio': 'Hola soy un alumno utilizando Django y Python. Este es un blog personal donde comparto mis experiencias y conocimientos.',
        'social_links': {
            'github': 'https://github.com/',
            'twitter': 'https://twitter.com/',
        },
        'avatar': 'path_to_avatar_image.jpg' 
    }
    return render(request, 'blog/about.html', context)