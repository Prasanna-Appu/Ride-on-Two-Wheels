from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import HomeCard,Services,Contact
from django.contrib import messages

# Create your views here.

def homePage(request):
    Homecard = HomeCard.objects.all()
    data ={
        'Homecard':Homecard
    }

    return render(request ,'webpages/home.html',data)

def aboutPage(request):

    return render(request ,'webpages/about.html')

def servicesPage(request):
    services = Services.objects.all()
    data ={
        'services':Services
    }
    return render(request ,'webpages/services.html',data)


def careersPage(request):
    return render(request ,'webpages/careers.html')
    
def contactPage(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        message = request.POST.get('message', False)
        
        
        contact = Contact(name=name,email=email, address=address, phone=phone,message=message)
        contact.save()
        messages.success(request, 'Thanks for reaching out!')
        return redirect('home')
    return render(request ,'webpages/contact.html')