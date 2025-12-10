from django.db import models

# Create your models here.

class UserSignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    mobile=models.BigIntegerField()

class NotesData(models.Model):
    submitted_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(UserSignup,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    cate=models.CharField(max_length=100)
    files=models.FileField(upload_to='NotesData')
    desc=models.TextField()
    status_choice=[
        ('Pending','Pending'),
        ('Approve','Approve'),
        ('Reject','Reject')
    ]
    status=models.TextField(max_length=20,choices=status_choice)
    updated_at=models.DateTimeField(blank=True,null=True)
    