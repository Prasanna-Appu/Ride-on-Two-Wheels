from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import RentingService,BookARide,Emergency
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
import razorpay

# Create your views here.
@login_required(login_url='login')
def payment(request):
    if request.method == 'POST':
        amount = 500
        order_currency = 'INR'
        client = razorpay.Client(
            auth=('rzp_test_i2hZmqLyieAh7Q','zsmy5ehCv6X6igPEeDRvRj6w'))
        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})

    return render(request,'rider/payment.html')

@csrf_exempt
def success(request):
    return render(request, "rider/success.html")




def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.warning(request,'You are logged IN')
            return redirect('home')
        else:
            messages.warning(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'rider/login.html') 

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'Username exists')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.warning(request, 'Email already exists')
                    return redirect('signup')
                else:
                     user = User.objects.create_user(first_name=firstname, last_name=lastname,
                                        username=username, email=email,
                                        password=password)
                     user.save()
                     messages.success(request, 'Account Created Successfully ')
            return render(request,'rider/login.html')

        else:
            messages.warning(request, 'Password do not match')
            return redirect('signup')
       
    
    return render(request,'rider/signup.html')
    

def logout_user(request):
    logout(request)
    return redirect('home')


@login_required(login_url='login')
def bookARide(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        DOB = request.POST['DOB']
        email = request.POST['email']
        phone = request.POST.get('phone')
        gender = request.POST['gender']
        city = request.POST['city']
        pick_up = request.POST['pick_up']
        drop_addr = request.POST['drop_addr']

        bookARide = BookARide(firstname=firstname,lastname=lastname,DOB=DOB,email=email,phone=phone,gender=gender,city=city,pick_up=pick_up,drop_addr=drop_addr)
        bookARide.save()
        messages.success(request, 'Thank You for registration')
        return redirect('payment')
        
    return render(request,'rider/bookaride.html')

@login_required(login_url='login')
def emergency(request):
    emergency = Emergency.objects.all()
    data={
        'emergency' : emergency
    }
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        DOB = request.POST['DOB']
        email = request.POST['email']
        phone = request.POST['phone']
        gender = request.POST['gender']
        city = request.POST['city']
        state = request.POST['state']
        pick_up = request.POST['pick_up']
        drop_addr = request.POST['drop_addr']

        emergency = Emergency(firstname=firstname,lastname=lastname,DOB=DOB,email=email,phone=phone,gender=gender,city=city,pick_up=pick_up,drop_addr=drop_addr)
        emergency.save()
        messages.success(request, 'Thank You for registration')
        return redirect('payment')
    return render(request,'rider/emergency.html',data)

@login_required(login_url='login')
def rentBike(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST.get('phone')
        gender = request.POST['gender']
        Occupation = request.POST.get('Occupation')
        driving_lic_no = request.POST.get('driving_lic_no')
        city = request.POST.get('city')
        curr_address = request.POST.get('curr_address')
        perm_address = request.POST['perm_address']
        rent_hrs = request.POST.get('rent_hrs')
        rent_chars = request.POST.get('rent_chars')

        rentBike = RentingService(firstname=firstname,lastname=lastname,email=email,phone=phone,gender=gender,Occupation=Occupation,driving_lic_no=driving_lic_no,city=city,curr_address=curr_address,perm_address=perm_address,rent_hrs=rent_hrs,rent_chars=rent_chars)
        rentBike.save()
        messages.success(request, 'Thank You for registration')
        return redirect('payment')
    return render(request,'rider/rentbike.html')


