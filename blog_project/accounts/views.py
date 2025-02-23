from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Vista para el Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            return redirect('home')  # Redirige a la página principal o la página deseada
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

# Vista para el Logout
def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')

# Vista para el Registro de Usuario
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}!')
            return redirect('login')  # Redirige a la página de login después de registrarse
        else:
            messages.error(request, 'Por favor, corrige los errores.')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})
# accounts/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Vista para mostrar el perfil del usuario
@login_required
def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user': user})

@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la vista del perfil después de editar
    else:
        form = ProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

# accounts/views.py
# Vista para editar el perfil del usuario
@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirige a la vista del perfil después de editar
    else:
        form = ProfileForm(instance=user)
    return render(request, 'accounts/edit_profile.html', {'form': form})
