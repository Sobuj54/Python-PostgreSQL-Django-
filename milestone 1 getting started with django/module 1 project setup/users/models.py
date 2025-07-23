from django.db import models
from django.contrib.auth.models import  AbstractUser
"""
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="userprofile",primary_key=True)
    profile_image = models.ImageField(upload_to="profile_image", blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"User profile name {self.user.username}"
"""  

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to="profile_image", blank=True)

    def __str__(self):
        return self.username