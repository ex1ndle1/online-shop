from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from .forms import RegisterForm


def home(request):
    return render(request,  'user/home.html')



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user:home')  
    else:
        form = RegisterForm() 

    return render(request, 'user/register.html', {"form": form})