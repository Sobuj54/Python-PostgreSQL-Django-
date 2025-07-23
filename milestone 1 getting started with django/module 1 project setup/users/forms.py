from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group, Permission
from django import forms
import re
from django.utils.translation import gettext_lazy as _
from tasks.forms import StyledFormMixin
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm

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

class CustomPasswordChangeForm(StyledFormMixin, PasswordChangeForm):
    pass

class CustomPasswordResetForm(StyledFormMixin, PasswordResetForm):
    pass

class CustomPasswordResetConfirmForm(StyledFormMixin, SetPasswordForm):
    pass

class EditProfileForm(StyledFormMixin,forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
    
    bio = forms.CharField(required=False, widget=forms.Textarea, label="bio")
    profile_image = forms.ImageField(required=False, label="profile image")

    def __init__(self, *args, **kwargs):
        self.userprofile = kwargs.pop("userprofile", None)
        super().__init__(*args, **kwargs)

        if self.userprofile:
            self.fields["bio"].initial = self.userprofile.bio
            self.fields['profile_image'].initial =  self.userprofile.profile_image
    
    def save(self, commit = True):
        user = super().save(commit=False)

        if self.userprofile:
            self.userprofile.bio = self.cleaned_data.get("bio")
            self.userprofile.profile_image = self.cleaned_data.get("profile_image")
            if commit:
                self.userprofile.save()
        
        if commit:
            user.save()
        
        return user