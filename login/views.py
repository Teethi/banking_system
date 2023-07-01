from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from .models import Users as banking_user
from django.contrib import messages

# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'login.html', {"name":"timthy" })

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        phone_number=request.POST['phone_number']
        address=request.POST['address']    
        date_of_birth=request.POST['date_of_birth']
        gender=request.POST['gender']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        # security_question=request.POST['security_question']
        # security_answer=request.POST[security_answer]    
        
        if password ==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User registered')
                messages.info(request,'Please Login')
                login_user=banking_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number,
                    address=address,
                    date_of_birth=date_of_birth,
                    gender=gender,
                    username=username,
                    password=password,

                )
                login_user.save()
        else:
            messages.info(request,'Password not matching')
        return redirect('/')
        
            
def login(request):
    username=request.POST['username']
    password=request.POST['password']
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return render(request, 'afterlogin.html')
    else:
        messages.info(request,'Invalid credentials')
        return redirect('/#')
    
def logout(request):
    auth.logout(request)
    return redirect('/#')
    

