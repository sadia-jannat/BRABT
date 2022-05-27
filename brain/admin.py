from django.contrib import admin

from brain.forms import Storyform

# Register your models here.

#register Doctorformfill model and class create for admin
from .models import Doctorformfill
@admin.register(Doctorformfill)
class Doctorformfilladmin(admin.ModelAdmin):
    list_display= ('name', 'doctor_nid', 'doctor_img','disease_name',
                   'details')
    
#register Story model and class create for admin
from .models import Story
@admin.register(Story)
class Storyformadmin(admin.ModelAdmin):
    list_display= ('firstname', 'lastname', 'type', 'storytitle', 'story', 'patient_img',
                'email', 'address', 'hospital_name')    


#map for neuro hospital
from .models import map
@admin.register(map)
class mymapreg(admin.ModelAdmin):
    list_display=()