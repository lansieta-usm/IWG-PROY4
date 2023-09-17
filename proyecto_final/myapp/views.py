from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuario

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def user(request):
    users = Usuario.objects.all()
    return render(request, "users.html", {"users" : users})

def añadir(request):
    return render(request, "añadir.html")

def blog(request):
    return render(request, "blog.html")