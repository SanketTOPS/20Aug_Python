from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=SignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            
            #Email Sending Code
            global otp
            otp=random.randint(1111,9999)
            
            sub="Your One Time Password!"
            msg=f"Dear User\n\nThanks for registration with us!\nFor Verification, your one time password is {otp}.\n\nThanks & Regards!\nNotesApp Team\n+91 9724799469 | www.tops-int.com"
            from_ID=settings.EMAIL_HOST_USER
            to_ID=[request.POST['username']]

            send_mail(subject=sub,message=msg,from_email=from_ID,recipient_list=to_ID)
            
            return redirect("otpverify")
        else:
            print(newuser.errors)
    return render(request,'signup.html')

def otpverify(request):
    msg=""
    if request.method=='POST':
        if request.POST["otp"]==str(otp):
            print("Verification Success!")
            msg="Verification Success!"
            return redirect("login")
        else:
            print("Error!OTP Verification faild...")
            msg="Error!OTP Verification faild..."
    return render(request,'otpverify.html',{'msg':msg})

def login(request):
    return render(request,'login.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')