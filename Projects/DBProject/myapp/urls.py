from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
   path('',views.index),
   path('about/',views.about,name='about'),
   path('showdata/',views.showdata,name='showdata'),
   path('deletedata/<int:id>',views.deletedata,name="deletedata"),
]