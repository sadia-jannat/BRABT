# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
#add first create
from django.contrib import admin
from brain import views
#we need all time for views.py
from urllib import request
from django.http.response import HttpResponseRedirect, JsonResponse,json
from django.shortcuts import redirect
from django.contrib import messages
#query ar jonno
from django.db.models import Q
from .forms import SearchForm
#google map ar jonno
import folium
import geocoder
import json

# all models and forms name add korar jonno * use kora jay
from .models import *
from .forms import *


#from django.contrib.auth.forms import UserCreationForm nisilm..akhn nijer form create korsi django r under a
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

#django authentication ar jonno forms.py class name UserSignUp giving by me.
#auth ar own class name User
from .forms import UserSignUp
from django.contrib.auth.models import User

#Doctorformfill model and Doctorformfillform form for doctorfillup page
from .forms import Doctorformfillform
from .models import Doctorformfill 

#Story model and Storyform form for sharestory page
from .forms import Storyform
from .models import Story

#google map page ar jonno
from .forms import mapform
from .models import map


def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def introduction(request):
    return render(request, 'introduction.html')

def slide(request):
        return render(request, 'slide.html')
    
def type(request):
        return render(request, 'type.html')
    

#signup page and authentication..it not UserSignUp me.django create
def user_signup(request):
    fo=UserSignUp()
    if request.method == "POST":
        fo=UserSignUp(request.POST)
        if fo.is_valid():
            fo.save()
            messages.success(request, 'Your Account create successfully!!')
            
    context={'form':fo}

    return render(request, 'user_signup.html', context)  

#create login page use global variable login_result=1,(UserSignUp hoty nia)username,password1 1 na dily o hobe.
#authenticate,login, agula django ar auth create korse..jar maddome amra get method use korty pari

login_result=1
def user_login(request):
    
    if request.method == "POST":
     username=request.POST.get('username')
     password=request.POST.get('password') 
     user=authenticate(request, username=username, password=password)
     if user is not None:
            global login_result
            login_result=0
            
            login(request,user)
            return redirect('/doctorfillup/')
        
    return render(request, 'user_login.html')   

#user_logout page
#logout by authenticate..use logout tag
def user_logout(request):

    logout(request)

    return redirect('/')   


#doctor form fill ar work and use model class name,POST method use
def doctorfillup(request):
    
    if request.method =="POST":
        form=Doctorformfill()
        
        form.name = request.POST.get('name')
        form.doctor_nid=request.POST.get('doctor_nid')
        form.disease_name=request.POST.get('disease_name')
        form.details=request.POST.get('details')
        if len(request.FILES) != 0:
            form.doctor_img=request.FILES['doctor_img']
            
        form.save()
        messages.info(request,'Your opinion added successfully!!')  
        
    context={ 'login_result':login_result}  
        
    return render(request, 'doctorfillup.html', context)

#showdoctoropinion page
disease_list=[]
def showdoctoropinion(request):
    
    if request.method == 'POST':
        search = SearchForm(request.POST)
        if search.is_valid():
            query = search.cleaned_data['query']
            global disease_list
            disease_list=Doctorformfill.objects.filter(disease_name__icontains=query)
        else:
            disease_list=Doctorformfill.objects.all()
                
    show=Doctorformfill.objects.all()
    context={'disease_list':disease_list,
             'login_result':login_result,
             'show':show, }
    
    return render(request, 'showdoctoropinion.html', context)

#symptom page
def symptom(request):
    return render(request, 'symptom.html')

#treatment page
def treatment(request):
    return render(request, 'treatment.html')

#diagnosis page
def diagnosis(request):
    return render(request, 'diagnosis.html')

#food page
def food(request):
    return render(request, 'food.html')

#checkbody page
def checkbody(request):
    return render(request, 'checkbody.html')

#share story page
def sharestory(request):
    
     if request.method =="POST":
            story=Story()
            story.firstname = request.POST.get('firstname')
            story.lastname = request.POST.get('lastname')
            story.type = request.POST.get('type')
            story.storytitle = request.POST.get('storytitle')
            story.story = request.POST.get('story')
            story.email = request.POST.get('email')
            story.address = request.POST.get('address')
            story.hospital_name = request.POST.get('hospital_name')
            
            if len(request.FILES) != 0:
                story.patient_img=request.FILES['patient_img']
            
            story.save() 
            messages.info(request,'Your story added successfully!!')     
                
     return render(request, 'sharestory.html')


#showstoryhome page
def showstoryhome(request):
    show=Story.objects.all()
    
    context={'show':show, }
    return render(request, 'showstoryhome.html', context)

#share showstory page 
def showstory(request, pk):
    showall=Story.objects.get(id=pk)

    context={'showall':showall, }
    return render(request, 'showstory.html', context)

#hospitallist page
def hospitallist(request):
    return render(request, 'hospitallist.html')

#doctorlist page
def doctorlist(request):
    return render(request, 'doctorlist.html')

#map for bangladesh neuro hospital list
def googlemap(request):
    #map post code
    if request.method=='POST':
        form=mapform(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/googlemap')
    else:
        form=mapform()
        
    #geocode ar code
    geo=map.objects.all().last()

    location=geocoder.osm(geo)
    lat=location.lat
    lng=location.lng
    country=location.country

    #correct area na dily data ty add hobe na.tuturial thyk dekty hobe aber
    #if lat == None or lng == None:
        #geo.delete()
        #return HttpResponse('Your location input is invalid')
        
    #create map for bangladesh lat,lng and location num ok

    m=folium.Map(location=[23.684994, 90.356331], zoom_start=4)

    folium.Marker([lat, lng], tooltip='click for more', icon=folium.Icon(color='green', icon='cloud'), popup=country).add_to(m)

    #we can want to add 8 division marker map to our creat map
    folium.Marker(location=[24.903561,91.873611], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Sylhet</strong>").add_to(m)
    folium.Marker(location=[24.098379,90.328712], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Dhaka</strong>").add_to(m)
    #baki gula per day ty nity hobe
    folium.Marker(location=[24.376930,88.603073], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Rajshahi</strong>").add_to(m)
    folium.Marker(location=[22.841930,89.558060], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Khulna</strong>").add_to(m)
    folium.Marker(location=[22.700411,90.374992], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Barishal</strong>").add_to(m)
    folium.Marker(location=[22.330370,91.832626], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Chittagong</strong>").add_to(m)
    folium.Marker(location=[24.744221,90.403008], tooltip='click for more', icon=folium.Icon(color='red', icon='envelope'), popup="<strong>Mymensingh</strong>").add_to(m)
    folium.Marker(location=[25.740580,89.261139], tooltip='click for more', icon=folium.Icon(color='red', icon='cloud'), popup="<strong>Rangpur</strong>").add_to(m)


    m=m._repr_html_()
    context={
        'm':m,
        'form':form,
    }
        
    return render(request, 'googlemap.html', context)
