from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from .forms import SignUpForm


def home_view(request):
    return render(request, 'home.html')


def about_view(request):
    return render(request, 'about.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a new page upon successful login
            return redirect('home')  # Replace 'home' with the name of your desired URL pattern
        else:
            # Handle invalid login credentials (e.g., display error message)
            return render(request, 'login.html', {'error_message': 'Invalid email or password'})

    return render(request, 'login.html')


def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Замените 'home' на путь для перенаправления пользователя
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})