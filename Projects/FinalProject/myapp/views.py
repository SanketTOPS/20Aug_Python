from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from FinalProject import settings
from django.contrib.auth import logout

# Create your views here.
def index(request):
    user=request.session.get("user") #session get
    return render(request,'index.html',{'user':user})

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
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']
        
        user=UserSignup.objects.filter(username=unm,password=pas)
        userid=UserSignup.objects.get(username=unm)
        print("UserID:",userid)
        if user:
            print("Login Successfull!")
            request.session["user"]=unm #session gen.
            request.session["userid"]=userid.id #session gen.
            return redirect("/")
        else:
            print("Error!Login Faild...")
    return render(request,'login.html')

def about(request):
    user=request.session.get("user")
    return render(request,'about.html',{'user':user})

def contact(request):
    user=request.session.get("user")
    return render(request,'contact.html',{'user':user})

def notes(request):
    try:
        user=request.session.get("user")
        unm=UserSignup.objects.get(username=user)
        if request.method=='POST':
            newReq=NotesForm(request.POST,request.FILES)
            if newReq.is_valid():
                x=newReq.save(commit=False)
                x.user=unm
                x.status="Pending"
                x.save()
                print("Notes Submitted!")
            else:
                print(newReq.errors)
    except:
        print("Error!")   
    return render(request,'notes.html',{'user':user})
        

def profile(request):
    user=request.session.get("user") #session get
    userid=request.session.get("userid") #session get
    cuser=UserSignup.objects.get(id=userid)
    if request.method=='POST':
        updateReq=UpdateForm(request.POST,instance=cuser)
        if updateReq.is_valid():
            updateReq.save()
            print("Profile Updated!")
            return redirect("/")
        else:
            print(updateReq.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def userlogout(request):
    logout(request)
    return redirect("login")