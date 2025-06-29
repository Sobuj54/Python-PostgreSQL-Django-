from django.urls import path
from category.views import category_list

urlpatterns = [
    path("list/", category_list)
]
