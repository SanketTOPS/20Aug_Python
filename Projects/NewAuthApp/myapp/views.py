from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout

# Create your views here.
def login(request):
    if request.method=='POST':
        unm=request.POST["email"]
        pas=request.POST["password"]
        
        user=UserSignup.objects.filter(email=unm,password=pas)
        if user:
            print("Login Successfully!")
            request.session["user"]=unm
            
            return redirect("home")
        else:
            print("Error!Login Faild...")
    return render(request,'login.html')

def signup(request):
    msg=""
    if request.method=='POST':
        email=request.POST["email"]
        newuser=SignupForm(request.POST)
        if newuser.is_valid():
            if UserSignup.objects.filter(email=email).exists():
                msg="Email is alreasy exists!"
            else:
                newuser.save()
                print("Signup Successfully!")
                return redirect("/")
        else:
            print(newuser.errors)
    return render(request,'signup.html',{'msg':msg})

def home(request):
    cuser=request.session.get("user")
    try:
        uname=UserSignup.objects.get(email=cuser)
        print("Name:",uname.firstname)
        return render(request,'home.html',{'cuser':uname.firstname})
    except UserSignup.DoesNotExist:
        print("Error")
        return render(request,'home.html')
    

def userlogout(request):
    logout(request)
    return redirect("/")