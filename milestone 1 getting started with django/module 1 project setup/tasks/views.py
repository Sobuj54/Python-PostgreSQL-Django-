from django.shortcuts import render, HttpResponse
from tasks.forms import  TaskModelForm
from tasks.models import  Task, TaskDetail, Project, Employee
from datetime import date
from django.db.models import Q
# Create your views here.

def manager_dashboard(req):
    return render(req, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    context = {
        "names": ["sobuj", "maruf", "ashik"]
    }
    return render(request, "test.html", context)

def create_task(request):
    # employees = Employee.objects.all()
    form = TaskModelForm()

    if request.method =="POST":
        form = TaskModelForm(request.POST)
        if form.is_valid():
             """ This code is for django model form """
             form.save()
             return render(request, "form.html",{"form": form, "message":"Task created successfully."})
             """ Below code is only necessafy for django form"""
            # data = form.cleaned_data
            # title = data.get("title")
            # description = data.get("description")
            # due_date = data.get("due_date")
            # assigned_to = data.get("assigned_to")

            # task = Task.objects.create(title=title, description=description, due_date=due_date)
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)

    context = {"form": form}
    return render(request, "form.html", context)

def view_task(request):
    # fetch all the tasks from task table
    tasks = Task.objects.all()

    # get a specific task by id
    task_id = Task.objects.get(id=1)

    #get the first task
    first_task = Task.objects.first()

    # filter tasks by their status
    filter_tasks = Task.objects.filter(status="PENDING")

    # tasks that are due today
    due_today = Task.objects.filter(due_date=date.today())

    # exclue from filter query
    ex = TaskDetail.objects.exclude(priority="L")

    # check if a field contains certain character or word
    contains_value = Task.objects.filter(title__icontains="mac")

    # get the rows where title contains "mac" and status is in progress
    AND = Task.objects.filter(title__icontains="mac", status="IN_PROGRESS")
    
    # get the rows where title status is pending or in progress
    OR = Task.objects.filter(Q(status="PENDING") | Q(status="IN_PROGRESS"))


    """ optimizing the db queries. Using join """
    tasks_joined_taskDetail = Task.objects.select_related("details").all() # only works in one to one relation
    taskDetail_joined_tasks = TaskDetail.objects.select_related("task").all() # only works in one to one relation
    task_project = Task.objects.select_related("project").all() # here this works for foreign key relation only in forward

    """ for many to many or foreign key relation """
    project_task = Project.objects.prefetch_related("task_set").all() # foreign key
    task_employee = Task.objects.prefetch_related("assigned_to").all() # many to many relation
    employee_task = Employee.objects.prefetch_related("task_set").all() # many to many reverse relation


    CONTEXT = {
        "tasks": tasks, "task_id":task_id, "first_task": first_task, "filter_tasks": filter_tasks, 
        "due_today": due_today, "ex": ex, "contains": contains_value, "and": AND, "or": OR,
        "task_joined": tasks_joined_taskDetail, "taskDetail_joined": taskDetail_joined_tasks,
        "task_project": task_project, "project_task": project_task, "task_employee": task_employee,
        "employee_task": employee_task
    }

    return render(request, "show_tasks.html", context=CONTEXT)