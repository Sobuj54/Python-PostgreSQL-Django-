from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending"),
        ("IN_PROGRESS", "In progress"),
        ("COMPLETED", "Completed"),
    ]
    project = models.ForeignKey("Project", on_delete=models.CASCADE, default=1)
    assigned_to = models.ManyToManyField(Employee, related_name="tasks")
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default="PENDING")
    due_date = models.DateField()
    is_completed = models.BooleanField(default=False)
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