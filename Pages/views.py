from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'Pages/home.html')

def about(request):
    return render(request,'Pages/about.html')

def services(request):
    return render(request,'Pages/services.html')

def contact(request):
    return render(request,'Pages/contact.html')