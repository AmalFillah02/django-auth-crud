from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    form = AuthenticationForm()
    register_form = UserCreationForm()

    if request.method == 'POST':
        if 'login' in request.POST:
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                user = form.get_user()
                auth_login(request, user)
                return redirect('user_list')
            else:
                messages.error(request, "Login gagal. Silakan cek username dan password.")
        elif 'register' in request.POST:
            register_form = UserCreationForm(request.POST)
            if register_form.is_valid():
                register_form.save()
                messages.success(request, "Akun berhasil dibuat. Silakan login.")
                return redirect('/')
            else:
                messages.error(request, "Registrasi gagal. Silakan periksa kembali form dan ikuti petunjuknya.")

    return render(request, 'accounts/home.html', {
        'form': form,
        'register_form': register_form,
    })

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
def user_create(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'accounts/user_form.html', {'form': form})

@login_required
def user_update(request, pk):
    user = get_object_or_404(User, pk=pk)
    form = UserCreationForm(request.POST or None, instance=user)
    if form.is_valid():
        form.save()
        return redirect('user_list')
    return render(request, 'accounts/user_form.html', {'form': form})

@login_required
def user_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'accounts/user_confirm_delete.html', {'user': user})