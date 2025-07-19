from django.urls import path
from tasks.views import manager_dashboard, employee_dashboard, create_task,view_task, update_task, delete_task, task_details, redirect_based_on_role, CreateTask, ViewProject, TaskDetails, UpdateTask

urlpatterns = [
    path("manager-dashboard/",manager_dashboard, name="manager-dashboard"),
    path("user-dashboard/",employee_dashboard, name="user-dashboard"),
    # path("create-task/",create_task, name="create-task"),
    path("create-task/",CreateTask.as_view(), name="create-task"),
    # path("view_tasks/", view_task, name="view-tasks"),
    path("view_tasks/", ViewProject.as_view(), name="view-tasks"),
    # path("task/<int:task_id>/details/", task_details, name="task-details"),
    path("task/<int:pk>/details/", TaskDetails.as_view(), name="task-details"),
    # path("update-task/<int:id>/", update_task, name="update-task"),
    path("update-task/<int:pk>/", UpdateTask.as_view(), name="update-task"),
    path("delete-task/<int:id>/", delete_task, name="delete-task"),
    path("dashboard/", redirect_based_on_role, name="dashboard")
]