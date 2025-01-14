from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from .models import CustomUser


def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        middle_name = request.POST.get("middle_name")
        role = request.POST.get("role", 0)

        hashed_password = make_password(password)

        user = CustomUser.objects.create(
            email=email, password=hashed_password, first_name=first_name, last_name=last_name, middle_name=middle_name,
            role=role
        )
        user.is_active = True
        user.save()
        login(request, user)
        return redirect("login")
    return render(request, "auth/register.html")


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect("home")
        return render(request, "auth/login.html", {"error": "Wrong username or password"})
    return render(request, "auth/login.html")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def user_list(request):
    if request.user.role != 1:
        return redirect("home")
    users = CustomUser.objects.all()
    return render(request, "users/list.html", {"users": users})


@login_required
def user_detail(request, user_id):
    if request.user.role != 1:
        return redirect(request)
    user = CustomUser.objects.filter(id=user_id).first()
    if not user:
        return render(request, "users/detail.html", {"error": "User not found"})
    return render(request, "users/detail.html", {"user": user})


def home(request):
    return render(request, "home.html")
