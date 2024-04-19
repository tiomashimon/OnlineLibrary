from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page or any other page
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'client/register.html', {'form': form})

def login(request):
    return render(request, 'client/login.html')


def home(request):
    return render(request, 'client/home.html')

def likes(request):
    return render(request, 'client/likes.html')

def notifications(request):
    return render(request, 'client/notifications.html' )

def orders(request):
    return render(request, 'client/orders.html')

def fines(request):
    return render(request, 'client/fines.html')

def logout(request):
    return render(request, 'client/logout.html')
