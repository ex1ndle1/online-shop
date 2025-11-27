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



def login(request):
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
                return render(request, 'login.html', {'form': form, 'error': 'Неверный логин или пароль'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})



def logout_page(request):
    if request.method == 'POST':
        logout(request)
        return redirect('app:index')
    