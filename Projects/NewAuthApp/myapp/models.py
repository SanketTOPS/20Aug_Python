from django.db import models

# Create your models here.
class UserSignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=15)