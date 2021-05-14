from django.shortcuts import render
from .models import Team

# Create your views here.
def home(request):
    teams = Team.objects.all()
    context = {'teams':teams,}
    return render(request,'Pages/home.html',context)

def about(request):
    teams = Team.objects.all()
    context = {'teams':teams,}
    return render(request,'Pages/about.html',context)

def services(request):
    return render(request,'Pages/services.html')

def contact(request):
    return render(request,'Pages/contact.html')