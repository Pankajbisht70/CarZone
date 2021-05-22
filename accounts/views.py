from contacts.models import Contact
from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
    if request.method == "POST":
        print("1111111111111111111111111111111111111111")
        username = request.POST['username']
        password = request.POST['password']
        

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'User is login')
            return redirect('dashboard')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('login')

    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
       # messages.error(request, 'This is error message')
       # return redirect('register')
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request,"username already exist")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already exist")
                    return redirect('register')
                else:
                    user = User.objects.create_user(first_name=firstname,last_name=lastname,username=username,password=password,email=email)
                    #this code used for auto login after registration
                    auth.login(request,user)
                    messages.success(request,"You are Login sucessfully. ")
                    return redirect('dashboard')
                    # Code end
                    user.save()
                    messages.success(request,"You are registered sucessfully.")
                    return redirect('login')
        else:
            messages.error(request,"Password do not match ! Try Again")
            return redirect('register')

    return render(request, 'accounts/register.html')

@login_required(login_url = 'login')

def dashboard(request):
    user_inquiry = Contact.objects.order_by('-create_date').filter(user_id = request.user.id)
    data = {
        'user_inquiry':user_inquiry
    }
    return render(request, 'accounts/dashboard.html',data)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        #messages.success(request,'You are sucessfully logout')
        return redirect('home')
    return redirect('home')