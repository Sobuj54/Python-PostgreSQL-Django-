from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("welcome to task management system")

def contact(request):
    return HttpResponse("welcome to contact page")

def showTask(request):
    return HttpResponse("welcome to show task page")
