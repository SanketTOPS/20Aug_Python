from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields='__all__'
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields=['firstname','lastname','city','state','mobile']
        
class NotesForm(forms.ModelForm):
    class Meta:
        model=NotesData
        fields=['title','cate','files','desc']