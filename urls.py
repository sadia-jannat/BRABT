"""braintumor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include

#brain app to use views add
from brain import views
#image add ar jonno
from django.conf import settings
from django.conf.urls.static import static

#API
from brain.views import *


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index" ),
    path('introduction/', views.introduction, name="introduction"),
    path('about/', views.about, name="about"),
    path('slide/', views.slide, name="slide"),
    path('type/', views.type, name="type"),
    path('user_signup/', views.user_signup, name="user_signup"),
    path('user_login/', views.user_login, name="user_login"),
    path('user_logout/', views.user_logout, name="user_logout"),
    
    path('doctorfillup/', views.doctorfillup, name="doctorfillup"),
    path('showdoctoropinion/', views.showdoctoropinion, name="showdoctoropinion"),
    path('symptom/', views.symptom, name="symptom"),
    path('treatment/', views.treatment, name="treatment"),
    path('diagnosis/', views.diagnosis, name="diagnosis"),
    path('food/', views.food, name="food"),
    path('checkbody/', views.checkbody, name="checkbody"),
    
    path('sharestory/', views.sharestory, name="sharestory"),
    path('showstoryhome/', views.showstoryhome, name="showstoryhome"),
    path('showstory/<str:pk>', views.showstory, name='showstory'),
    
    path('hospitallist/', views.hospitallist, name="hospitallist"),
    path('doctorlist/', views.doctorlist, name="doctorlist"),
    path('googlemap/', views.googlemap, name="googlemap"),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
