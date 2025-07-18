from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django import forms
import re
from django.utils.translation import gettext_lazy as _
from tasks.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm

# this is noob way
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

# pro way
class CustomRegistrationForm(StyledFormMixin,forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]

    # field validation
    def clean_password(self):
        password = self.cleaned_data.get("password")
        if password:
            if not re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+])(?=.{8,})', password):
                raise forms.ValidationError( "Password must be at least 8 characters long and contain at least one uppercase letter, "
                    "one lowercase letter, one digit, and one special character.")
        return password
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already in use.")
        return email


    # non field validation
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", _("Passwords do not match."))

    # must for password hashing in django
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        if commit:
            user.save()
        return user
    

class LoginForm(StyledFormMixin, AuthenticationForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class AssignRoleForm(StyledFormMixin,forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a role"
    )


class CreateGroupForm(StyledFormMixin, forms.ModelForm):
    permissions = forms.ModelMultipleChoiceField(
        queryset=Permission.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        label="Assign permissions"
    )

    class Meta:
        model = Group
        fields = ["name", "permissions"]

