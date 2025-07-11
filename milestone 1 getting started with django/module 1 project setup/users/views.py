from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomRegistrationForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            messages.success(request, "Please check your mail to activate account.")
            return redirect("users:login")
    else:
        form = CustomRegistrationForm()
        
    return render(request, "registration/register.html", {"form": form})


def sign_in(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
        
    return render(request, "registration/login.html", {"form": form})

def user_logout(request):
    logout(request)
    return redirect("users:login")

def active_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active = True
            user.save()
            return redirect("users:login")
        else:
            return HttpResponse("Invalid id or token.")
    except User.DoesNotExist:
        return HttpResponse("User does not exist.")