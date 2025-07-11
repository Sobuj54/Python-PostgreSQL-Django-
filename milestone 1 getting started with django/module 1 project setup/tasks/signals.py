from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from tasks.models import Task

# Primary handler for M2M changes (best practice)
@receiver(m2m_changed, sender=Task.assigned_to.through)
def notify_employees_on_task_creation(sender, instance, action, **kwargs):
    if action == "post_add":  # Only when new assignments are made
        recipients = [emp.email for emp in instance.assigned_to.all() if emp.email]

        if recipients:
            subject = f"New Task Assigned: {instance.title}"
            message = f"""
                        Hello,

                        You have been assigned a new task.

                        Title: {instance.title}
                        Description: {instance.description}
                        Due Date: {instance.due_date}

                        Please log in to your dashboard to manage it.

                        Regards,
                        Task Management System
                        """
            send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    recipients,
                    fail_silently=False,
                )
            print(f"[Signal] Task created. Email sent to {len(recipients)} employees.")