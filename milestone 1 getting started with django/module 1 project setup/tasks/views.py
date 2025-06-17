from django.shortcuts import render, HttpResponse
from tasks.forms import TaskForm, TaskModelForm
from tasks.models import Employee, Task
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