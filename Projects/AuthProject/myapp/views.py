from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import logout

# Create your views here.
def login(request):
    msg=""
    if request.method=='POST':
        unm=request.POST["email"]
        pas=request.POST["password"]
        
        user=UserSignup.objects.filter(email=unm,password=pas)
        if user: #TRUE
            print("Login Successfully!")
            msg="Login Successfully!"
            
            request.session["user"]=unm #generate a session
            return redirect('home')
        else:
            print("Error!Login Faild...")
            msg="Error!Login Faild..."
    return render(request,'login.html',{'msg':msg})

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            print("Signup Successfull!")
            return redirect("/")
        else:
            print(form.errors)
    return render(request,'signup.html')

def home(request):
    user=request.session.get("user")
    cuser=UserSignup.objects.get(email=user)
    return render(request,'home.html',{'user':cuser.fullname})

def userlogout(request):
    logout(request)
    return redirect('/')
    