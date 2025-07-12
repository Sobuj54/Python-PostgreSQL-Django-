from django.shortcuts import render, HttpResponse, redirect
from tasks.forms import  TaskModelForm, TaskDetailModelForm
from tasks.models import  Task, TaskDetail, Project, Employee
from datetime import date
from django.db.models import Q,Count
from django.contrib import messages
from django.contrib.auth.decorators import  user_passes_test, login_required, permission_required

# Test for user
def is_manager(user):
    return user.groups.filter(name="Manager").exists()

def is_employee(user):
    return user.groups.filter(name="Employee").exists()

# Create your views here.
@user_passes_test(is_manager, login_url="no-permission")
def manager_dashboard(req):
    type = req.GET.get("type", "all")

    # tasks = Task.objects.select_related("details").all()
    # total_task = Task.objects.all().count()
    # pending_task = Task.objects.filter(status="PENDING").count()
    # in_progress_task = Task.objects.filter(status="IN_PROGRESS").count()
    # completed_task = Task.objects.filter(status="COMPLETED").count()

    """ optimized way to count instead of filter """
    counts = Task.objects.aggregate(
        total_task=Count("id"),
        pending_task=Count("id", filter=Q(status="PENDING")),
        in_progress_task=Count("id", filter=Q(status="IN_PROGRESS")),
        completed_task=Count("id", filter=Q(status="COMPLETED")),
        )
    
    base_query = Task.objects.select_related("details")

    if type=="completed":
        tasks = base_query.filter(status="COMPLETED")
    elif type=="pending":
        tasks = base_query.filter(status="PENDING")
    elif type=="in-progress":
        tasks = base_query.filter(status="IN_PROGRESS")
    elif type=="all":
        tasks = base_query.all()

    context = {
        "tasks": tasks,
        "counts" : counts
    }

    return render(req, "dashboard/manager-dashboard.html", context=context)

@user_passes_test(is_employee, login_url="no-permission")
def employee_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")


@login_required
@permission_required("tasks.add_task", login_url="no-permission")
def create_task(request):
    # employees = Employee.objects.all()
    task_form = TaskModelForm()
    task_Detail_form = TaskDetailModelForm()

    if request.method =="POST":
        task_form = TaskModelForm(request.POST)
        task_Detail_form = TaskDetailModelForm(request.POST)
        if task_form.is_valid() and task_Detail_form.is_valid():
             """ This code is for django model form """
             task = task_form.save()
             task_detail = task_Detail_form.save(commit=False)

             task_detail.task = task
             task_detail.save()

             messages.success(request, "Task created successfully.")
             return render(request, "form.html", {"task_form": task_form, "task_detail_form": task_Detail_form})
             """ Below code is only necessary for django form"""
            # data = form.cleaned_data
            # title = data.get("title")
            # description = data.get("description")
            # due_date = data.get("due_date")
            # assigned_to = data.get("assigned_to")

            # task = Task.objects.create(title=title, description=description, due_date=due_date)
            # for emp_id in assigned_to:
            #     employee = Employee.objects.get(id=emp_id)
            #     task.assigned_to.add(employee)

    context = {"task_form": task_form, "task_detail_form": task_Detail_form}
    return render(request, "form.html", context)

@login_required
@permission_required("tasks.change_task", login_url="no-permission")
def update_task(request, id):
    task = Task.objects.get(id = id)
    task_form = TaskModelForm(instance=task)

    if task.details:
        task_Detail_form = TaskDetailModelForm(instance=task.details)

    if request.method =="POST":
        task_form = TaskModelForm(request.POST, instance=task)
        task_Detail_form = TaskDetailModelForm(request.POST, instance=task.details)
        
        if task_form.is_valid() and task_Detail_form.is_valid():
             """ This code is for django model form """
             task = task_form.save()
             task_detail = task_Detail_form.save(commit=False)

             task_detail.task = task
             task_detail.save()

             messages.success(request, "Task updated successfully.")
             return render(request, "form.html", {"task_form": task_form, "task_detail_form": task_Detail_form})

    context = {"task_form": task_form, "task_detail_form": task_Detail_form}
    return render(request, "form.html", context)


@login_required
@permission_required("tasks.delete_task", login_url="no-permission")
def delete_task(request, id):
    if request.method == "POST":
        task = Task.objects.get(id=id)
        task.delete()
        messages.success(request, "Task deleted successfully.")
        return redirect("manager-dashboard")
    else:
        messages.error(request, "Task deletion failed")
        return redirect("manager-dashboard")


@login_required
@permission_required("tasks.view_task", login_url="no-permission")
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

    """ aggregation """
    # numbers of tasks
    task_count = Task.objects.aggregate(task_num=Count("id"))
    # count the numbers of tasks in each project
    projects = Project.objects.annotate(num_task=Count("task")).order_by("num_task")


    CONTEXT = {
        "tasks": tasks, "task_id":task_id, "first_task": first_task, "filter_tasks": filter_tasks, 
        "due_today": due_today, "ex": ex, "contains": contains_value, "and": AND, "or": OR,
        "task_joined": tasks_joined_taskDetail, "taskDetail_joined": taskDetail_joined_tasks,
        "task_project": task_project, "project_task": project_task, "task_employee": task_employee,
        "employee_task": employee_task, "task_count": task_count, "projects": projects
    }

    return render(request, "show_tasks.html", context=CONTEXT)