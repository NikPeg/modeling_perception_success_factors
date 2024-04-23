from django.contrib.admin import register
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_qs = User.objects.filter(email=email)
        if user_qs.exists() and authenticate(request, username=email, email=email, password=password):
            return redirect('base')  # Redirect to a new URL
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('home')
    return redirect('home')


def register_view(request):
    if request.method == 'POST':
        passwords = request.POST.getlist("password")
        if passwords[0] != passwords[1]:
            messages.error(request, "Passwords don't match!")
            return redirect('home')
        email = request.POST.get('email')
        password = request.POST.get('password')
        User.objects.create_user(email, email, password)
        return redirect('base')


def base_view(request):
    return render(request, 'base.html')
