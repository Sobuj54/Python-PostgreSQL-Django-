from django.urls import path
from event.views import event_list

urlpatterns = [
    path("list/", event_list)
]
