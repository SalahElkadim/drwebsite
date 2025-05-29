from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'تم التسجيل بنجاح!')
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'البريد الإلكتروني أو كلمة السر غير صحيحة')
    return render(request, 'accounts/login.html')

def home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/home.html')