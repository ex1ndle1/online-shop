from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, LoginForm


def home(request):
    return render(request,  'user/home.html')



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:login')  
    else:
        form = RegisterForm() 

    return render(request, 'user/register.html', {"form": form})


def login_choice(request):
    return render(request, 'user/login_choice.html')


def login_by_username(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user) 
                return redirect('app:index')
            else:
                return render(request, 'user/login_by_username.html', {'form': form, 'error': 'Login is incorrect'})
    else:
        form = LoginForm()

    return render(request, 'user/login_by_username.html', {'form': form})



def login_by_phone(request):
     if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            user = authenticate(request, phone=phone, password=password)
            if user is not None:
                login(request, user) 
                return redirect('app:index')
            else:
                return render(request, 'user/login_by_phone.html', {'form': form, 'error': 'Login is incorrect'})
     else:
        form = LoginForm()

     return render(request, 'user/login_by_phone.html', {'form': form})


def login_by_email(request):
     if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user) 
                return redirect('app:index')
            else:
                return render(request, 'user/login_by_email.html', {'form': form, 'error': 'Login is incorrect'})
     else:
        form = LoginForm()

     return render(request, 'user/login_by_email.html', {'form': form})



def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')
    