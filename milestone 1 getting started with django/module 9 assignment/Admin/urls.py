from django.urls import path
from Admin.views import admin_dashboard,todays_events

app_name="Admin"

urlpatterns = [
    path("home/", admin_dashboard , name="home"),
    path("todays-events/", todays_events, name="todays-events")
]
