from django.shortcuts import render

# Create your views here.

def index(req):
    return render(req,'index.html')

def about(req):
    return render(req,'about.html')

def contact(req):
    return render(req,'contact.html')

def courses(req):
    return render(req,'courses.html')

def placement(req):
    return render(req,'placement.html')