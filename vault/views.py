from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, PasswordEntryForm
from .models import PasswordEntry
from .encryption import encrypt_password, decrypt_password
import secrets
import string

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, '❌ Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'vault/login.html', {'form': form})

def register_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Account created! Please login.')
            return redirect('login')
        else:
            messages.error(request, '❌ Please fix the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'vault/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    entries = PasswordEntry.objects.filter(user=request.user)
    decrypted_entries = []
    for entry in entries:
        decrypted_entries.append({
            'id': entry.id,
            'website': entry.website,
            'category': entry.category,
            'password': decrypt_password(entry.password),
            'created_at': entry.created_at,
            'updated_at': entry.updated_at,
        })
    return render(request, 'vault/dashboard.html', {'entries': decrypted_entries})

@login_required(login_url='login')
def add_password(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data['website']
            category = form.cleaned_data['category']
            password = form.cleaned_data['password']
            if PasswordEntry.objects.filter(user=request.user, website=website).exists():
                messages.error(request, f'⚠️ Entry for {website} already exists!')
            else:
                encrypted = encrypt_password(password)
                PasswordEntry.objects.create(
                    user=request.user,
                    website=website,
                    category=category,
                    password=encrypted
                )
                messages.success(request, f'✅ Password saved for {website}!')
                return redirect('dashboard')
    else:
        form = PasswordEntryForm()
    chars = string.ascii_letters + string.digits + string.punctuation
    suggested = ''.join(secrets.choice(chars) for _ in range(16))
    return render(request, 'vault/add_password.html', {'form': form, 'suggested': suggested})

@login_required(login_url='login')
def update_password(request, pk):
    entry = get_object_or_404(PasswordEntry, id=pk, user=request.user)
    if request.method == 'POST':
        new_password = request.POST.get('password')
        if new_password:
            entry.password = encrypt_password(new_password)
            entry.save()
            messages.success(request, f'✅ Password updated for {entry.website}!')
            return redirect('dashboard')
    decrypted = decrypt_password(entry.password)
    return render(request, 'vault/update_password.html', {'entry': entry, 'decrypted': decrypted})

@login_required(login_url='login')
def delete_password(request, pk):
    entry = get_object_or_404(PasswordEntry, id=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        messages.success(request, '✅ Password deleted successfully!')
        return redirect('dashboard')
    return redirect('dashboard')

@login_required(login_url='login')
def search_password(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        entries = PasswordEntry.objects.filter(
            user=request.user,
            website__icontains=query
        )
        for entry in entries:
            results.append({
                'id': entry.id,
                'website': entry.website,
                'category': entry.category,
                'password': decrypt_password(entry.password),
                'created_at': entry.created_at,
            })
    return render(request, 'vault/search.html', {'results': results, 'query': query})
