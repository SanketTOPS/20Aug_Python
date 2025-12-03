from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        newuser=SignupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect("login")
        else:
            print(newuser.errors)
    return render(request,'signup.html')

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