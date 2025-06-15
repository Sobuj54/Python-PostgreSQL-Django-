from django.shortcuts import render
# Create your views here.

def manager_dashboard(req):
    return render(req, "dashboard/manager-dashboard.html")

def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    return render(request, "test.html")