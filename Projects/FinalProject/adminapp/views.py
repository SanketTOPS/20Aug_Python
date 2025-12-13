from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *
import datetime

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

def approve_notes(request,id):
    nid=get_object_or_404(NotesData,id=id)
    nid.status="Approve"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Notes Approved!")
    
    #Sent Email
    
    return redirect('admin_notesdata')
    
def reject_notes(request,id):
    nid=get_object_or_404(NotesData,id=id)
    nid.status="Reject"
    nid.updated_at=datetime.datetime.now()
    nid.save()
    print("Notes Rejected!")
    return redirect('admin_notesdata')