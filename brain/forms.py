import django
from django.core import validators
from django.forms import fields, widgets
from django import forms

from .models import *

#models.py ar class name add must.All model name have to import that create by admin
from .models import Doctorformfill
from .models import Story


#create authenticate own model and form which django create
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#django create authenticate form (class name add me)
class UserSignUp(UserCreationForm):
    class Meta:
        model=User
        fields=['username', 'email', 'password1', 'password2']
        
#create Doctorformfill model ar forms.py
class Doctorformfillform(forms.ModelForm):
    class Meta:
        model=Doctorformfill()
        fields=['name', 'doctor_nid', 'doctor_img', 'disease_name', 'details']        
        
#create Stroy model ar forms.py
class Storyform(forms.ModelForm):
    class Meta:
        model=Story()
        fields=['firstname', 'lastname', 'type', 'storytitle', 'story', 'patient_img',
                'email', 'address', 'hospital_name']        
                

#auto search for diseases 
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

#map for neuro hospital
class mapform(forms.ModelForm):
    
    address=forms.CharField(label='')

    class Meta:
        model=map
        fields=['address',]    
                