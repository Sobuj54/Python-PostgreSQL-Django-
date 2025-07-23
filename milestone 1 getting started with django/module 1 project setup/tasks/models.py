from django.db import models
from django.conf import settings
# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In progress"),
        ("COMPLETED", "Completed"),
    ]
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    # assigned_to = models.ManyToManyField(Employee, related_name="tasks")
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"


class TaskDetail(models.Model):
    PRIORITY_OPTIONS = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    )

    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="details")
    asset = models.ImageField(upload_to="tasks_asset", blank=True, null=True)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default="L")
    notes = models.CharField(blank=True, null=True)

    def __str__(self):
        return f"Details of task {self.task.title}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}"