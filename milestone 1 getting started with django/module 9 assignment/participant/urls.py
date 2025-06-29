from django.urls import path
from participant.views import participant_list

app_name = 'participant'

urlpatterns = [
    path('list/',participant_list, name='list'),
]
