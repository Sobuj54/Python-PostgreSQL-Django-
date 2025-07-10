from django.shortcuts import render
from users.forms import CustomRegistrationForm
from django.contrib import messages

# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully.")
    else:
        form = CustomRegistrationForm()
        
    return render(request, "registration/register.html", {"form": form})
