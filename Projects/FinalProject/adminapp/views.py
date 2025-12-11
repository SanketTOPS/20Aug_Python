from django.shortcuts import render,redirect
from myapp.models import *

# Create your views here.
def admin_login(request):
    if request.method=='POST':
        unm=request.POST["username"]
        pas=request.POST["password"]
        
        if unm=="admin" and pas=="admin@123":
            print("Login Success!")
            return redirect('admin_dashboard')
        else:
            print("Error!Login Faild...")
    return render(request,'admin_login.html')

def admin_dashboard(request):
    return render(request,'admin_dashboard.html')

def admin_userdata(request):
    udata=UserSignup.objects.all()
    return render(request,'admin_userdata.html',{'udata':udata})

def admin_notesdata(request):
    ndata=NotesData.objects.all()
    return render(request,'admin_notesdata.html',{'ndata':ndata})