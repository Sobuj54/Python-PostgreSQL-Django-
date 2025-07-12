from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomRegistrationForm, LoginForm, AssignRoleForm, CreateGroupForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test

# Test for users
def is_admin(user):
    return user.groups.filter(name="Admin").exists()

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

@login_required
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
    

@user_passes_test(is_admin, login_url="no-permission")
def admin_dashboard(request):
    # unoptimized approach
    # users = User.objects.all()

    # optimized approach
    users = User.objects.prefetch_related("groups").all()

    for user in users:
        if user.groups.exists():
            user.group_name = user.groups.first().name
        else:
            user.group_name = "No group assigned."
    return render(request, "admin/dashboard.html", {"users": users})


@user_passes_test(is_admin, login_url="no-permission")
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()

    if request.method == "POST":
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get("role")
            user.groups.clear() # removes previous role
            user.groups.add(role)
            messages.success(request, f"{user.username} has been assigned to {role.name} role")
            return redirect("users:admin-dashboard")
        
    return render(request, "admin/assign-role.html", {"form": form})


@user_passes_test(is_admin, login_url="no-permission")
def create_group(request):
    form = CreateGroupForm()

    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f"Group {group.name} has been created successfully.")
            return redirect("users:create-group")
        
    return render(request, "admin/create-group.html", {"form":form})


@user_passes_test(is_admin, login_url="no-permission")
def group_list(request):
    groups = Group.objects.all()
    return render(request, "admin/group-list.html", {"groups": groups})