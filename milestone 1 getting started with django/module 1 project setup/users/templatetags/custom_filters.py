from django import template
from datetime import datetime

register = template.Library()

@register.filter
def humanized_date(value):
    if value:
        today = datetime.now().date()
        if value.date() == today:
            return f"Today at {value.strftime('%I:%M %p')}"
        if value.date() == today.replace(day=today.day - 1):
            return f"Yesterday at {value.strftime('%I:%M %p')}"
        else:
            return f"{value.date()}"
    return "No login date found."