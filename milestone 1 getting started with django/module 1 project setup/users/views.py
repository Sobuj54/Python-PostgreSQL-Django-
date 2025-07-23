from django.shortcuts import render, redirect, HttpResponse
from users.forms import CustomRegistrationForm, LoginForm, AssignRoleForm, CreateGroupForm,CustomPasswordChangeForm, CustomPasswordResetForm, CustomPasswordResetConfirmForm, EditProfileForm
from django.contrib import messages
from django.contrib.auth import login,logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.views.generic import TemplateView, UpdateView
from django.urls import reverse_lazy
from users.models import UserProfile

# Test for users
def is_admin(user):
    return user.groups.filter(name="Admin").exists()

# Create your views here.

class EditProfileView(UpdateView):
    model = User
    form_class = EditProfileForm
    template_name = "accounts/update-profile.html"
    context_object_name = "form"

    def get_object(self):
        return self.request.user
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['userprofile'] = UserProfile.objects.get(user=self.request.user)
        return kwargs   
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = UserProfile.objects.get(user=self.request.user)
        context["form"] = self.form_class(instance=self.object, userprofile=user_profile)
        return context
    
    def form_valid(self, form):
        form.save(commit=True)
        return redirect("users:profile")


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


class CustomLoginView(LoginView):
    form_class = LoginForm


class ChangePassword(PasswordChangeView):
    template_name = "accounts/password-change.html"
    success_url = reverse_lazy("users:password_change_done")
    form_class = CustomPasswordChangeForm


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


class ProfileView(TemplateView):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user =  self.request.user

        context['username'] = user.username
        context["email"] = user.email
        context["name"] = user.get_full_name()
        context["bio"] = user.userprofile.bio
        context["profile_image"] = user.userprofile.profile_image
        context["member_since"] = user.date_joined
        context["last_login"] = user.last_login
        return context
    

class CustomPasswordResetView(PasswordResetView):
    form_class = CustomPasswordResetForm
    template_name = "registration/reset-password.html"  # <- This is the form template
    email_template_name = "registration/reset_email.html"  # <- THIS is for the email
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        self.extra_email_context = {
            "protocol": 'https' if self.request.is_secure() else "http",
            "domain": self.request.get_host(),
        }
        messages.success(self.request, "A reset email has been sent. Please check your email.")
        return super().form_valid(form)

    

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomPasswordResetConfirmForm
    template_name = "registration/reset-password.html"
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        messages.success(self.request, "Password reset successfull.")
        return super().form_valid(form)
