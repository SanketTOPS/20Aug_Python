from django.shortcuts import render,redirect
from .forms import *

# Create your views here.
def index(request):
    if request.method=='POST':
        user=UserForm(request.POST)
        if user.is_valid():
            user.save()
            print("Record Inserted!")
        else:
            print(user.errors)        
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def showdata(request):
    data=Userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def deletedata(request,id):
    uid=Userinfo.objects.get(id=id)
    Userinfo.delete(uid)
    return redirect("showdata")
    