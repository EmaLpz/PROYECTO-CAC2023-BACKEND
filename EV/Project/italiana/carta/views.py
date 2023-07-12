from django.shortcuts import render
from .models import Project

# Create your views here.

def carta(request):
    projects = Project.objects.all()
    return render(request, "carta/menu.html", {'projects': projects})