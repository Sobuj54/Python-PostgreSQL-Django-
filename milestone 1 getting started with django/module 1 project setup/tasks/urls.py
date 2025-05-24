from django.urls import path
from tasks.views import showTask

urlpatterns = [
    path("show-tasks/", showTask)
]