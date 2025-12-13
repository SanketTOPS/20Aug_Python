from django.contrib import admin
from django.urls import path,include
from adminapp import views

urlpatterns = [
   path('',views.admin_login),
   path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
   path('admin_userdata/',views.admin_userdata,name='admin_userdata'),
   path('admin_notesdata/',views.admin_notesdata,name='admin_notesdata'),
   path('approve_notes/<int:id>',views.approve_notes,name='approve_notes'),
   path('reject_notes/<int:id>',views.reject_notes,name='reject_notes'),
]
