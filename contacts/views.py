from contacts.models import Contact
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact


# Create your views here.
def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id = car_id, user_id = user_id)
            if has_contacted:
                messages.error(request,"You have already made enquiry about this car")
                return redirect('/cars/'+car_id)
        
        contact = Contact(
            car_id=car_id, car_title=car_title, user_id=user_id, 
            first_name=first_name, last_name=last_name, customer_need=customer_need, 
            city=city, state=state, email=email, message=message
            )

        contact.save()
        messages.success(request, "Contact Saved")
        return redirect('/cars/'+car_id)