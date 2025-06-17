from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(Employee)
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TaskDetail(models.Model):
    PRIORITY_OPTIONS = (
        ("H", "High"),
        ("M", "Medium"),
        ("L", "Low"),
    )

    task = models.OneToOneField(Task, on_delete=models.CASCADE)
    assigned_to = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY_OPTIONS, default="L")


class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()