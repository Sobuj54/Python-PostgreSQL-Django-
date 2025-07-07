from django.shortcuts import render
from event.models import Event
from participant.models import Participant
from category.models import Category
from django.utils import timezone

# Create your views here.
def admin_dashboard(request):
    total_events = Event.objects.count()
    total_participants = Participant.objects.filter(participants__isnull=False).distinct().count()
    total_categories = Category.objects.count()

    today = timezone.localdate()
    upcoming_events = Event.objects.filter(date__gt=today).order_by("date", "time")
    upcoming_events_count = upcoming_events.count()
    todays_events = Event.objects.filter(date=today)
    print(today)
    print(todays_events)

    context = {
        "total_events": total_events,
        "total_participants": total_participants,
        "total_categories": total_categories,
        "upcoming_events_count": upcoming_events_count,
        "events": todays_events
    }

    return render(request,"todays-events.html", context)


def todays_events(request):
    pass

def all_events(request):
    pass

def past_events(request):
    pass

def upcoming_events(request):
    pass
