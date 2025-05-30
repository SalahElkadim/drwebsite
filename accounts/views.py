from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate , logout
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
        username = request.POST.get('username')  # تم التعديل هنا
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)  # وتم التعديل هنا أيضًا
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'اسم المستخدم أو كلمة السر غير صحيحة')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'تم تسجيل الخروج بنجاح.')
    return redirect('home')  # أو إلى الصفحة التي تريدها بعد تسجيل الخروج