from django.shortcuts import render
from .models import *

# Create your views here.

def index(req):
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def courses(req):
    data=Courses.objects.all()
    return render(req,'courses.html',{'courses':data})
    

def placement(req):
    return render(req,'placement.html')