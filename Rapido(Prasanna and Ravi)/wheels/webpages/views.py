from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import HomeCard,HomeCurosol,Services,Contact,Careers,AboutJumbo,AboutJumbo2,AboutJumbo3
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


def careersPage(request):
     if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        caddress = request.POST.get('caddress')
        paddress = request.POST.get('paddress')
        phoneno = request.POST.get('phoneno')
        aadhar = request.POST.get('aadhar')
        dlno = request.POST.get('dlno')
        rcno = request.POST.get('rcno')
        
        
        careers = Careers(fname=fname,lname=lname,email=email, caddress=caddress, paddress=paddress,phoneno=phoneno,aadhar=aadhar,dlno=dlno, rcno=rcno)
        careers.save()
        messages.success(request, 'We Will Confirm You Within 24 hours, Kindly Wait!')
        return redirect('home')
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