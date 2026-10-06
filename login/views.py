from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
# Create your views here.
def register(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match.'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists.'})

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect('login')

    return render(request, 'register.html')

def login_page(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )
        print(user)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        return render(
            request,
            'login.html',
            {'error': 'Invalid credentials'}
        )

    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def logout_page(request):
    logout(request)
    return redirect('/')