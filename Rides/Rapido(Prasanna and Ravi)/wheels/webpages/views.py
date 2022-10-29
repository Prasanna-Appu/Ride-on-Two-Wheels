from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import HomeCard,HomeCurosol,Services,Contact,AboutJumbo,AboutJumbo2,AboutJumbo3
from django.contrib import messages

# Create your views here.

def homePage(request):
    Homecard = HomeCard.objects.all()
    data ={
        'Homecard':Homecard
    }

    return render(request ,'webpages/home.html',data)


def homeCurosol(request):
    HomeCurosol = HomeCurosol.objects.all()
    data ={
        'HomeCurosol':HomeCurosol
    }

    return render(request ,'webpages/home.html',data)



def aboutPage(request):
    'AboutJumbo' == AboutJumbo.objects.all()
    data ={
        'AboutJumbo':AboutJumbo
    }

    
    'AboutJumbo2' == AboutJumbo2.objects.all()
    data ={
        'AboutJumbo2':AboutJumbo2
    }

    'AboutJumbo3' == AboutJumbo3.objects.all()
    data ={
        'AboutJumbo3':AboutJumbo3
    }



    return render(request ,'webpages/about.html')

def servicesPage(request):
    services = Services.objects.all()
    data ={
        'services':services
    }
    return render(request ,'webpages/services.html',data)



    
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