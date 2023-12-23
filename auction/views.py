from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import *

# Create your views here.


def home(request):
    return render(request, "home.html")


def signup(request):
    context = {}
    if request.POST:
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if not User.objects.filter(username=username).exists():
            user = User.objects.create_user(username=username, email=email, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)
            return redirect("home-page")
        else:
            context['status'] = 'This username already exists !!!'
            context['col'] = 'alert-danger'
    return render(request, "register.html", context)


def login_page(request):
    context = {}
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("home-page")
        else:
            context['status'] = 'Username or Password incorrect !!!'
            context['col'] = 'alert-danger'
    return render(request, "login.html", context)


def logout_page(request):
    logout(request)
    return redirect("home-page")
