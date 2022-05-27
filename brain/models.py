from django.db import models
#image ar time ,date debr jonno bellow
import datetime
import os

# Create your models here.

#doctor form fillup ar model create

#doctor_img ar jonno
def doctorimg(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

#disease-category for ownerformfill model ar..work
DISEASE_CATEGORY=(                
    ('Meningioma', 'Meningioma'),
    ('Pituitary Adenoma', 'Pituitary Adenoma'),
    ('Craniopharyngioma', ' Craniopharyngioma'),
    ('Schwannoma', 'Schwannoma'),
   
)

class Doctorformfill(models.Model):
    name=models.CharField(max_length=100)
    doctor_nid=models.IntegerField()
    doctor_img=models.ImageField(upload_to=doctorimg, null=True, blank=True )
    disease_name=models.CharField(choices=DISEASE_CATEGORY, max_length=100)
    details=models.CharField(max_length=100)
        

#story add model
#doctor_img ar jonno
def patientimg(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Story(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    type=models.CharField(max_length=200)
    storytitle=models.CharField(max_length=400)
    story=models.CharField(max_length=1000)
    patient_img=models.ImageField(upload_to=patientimg, null=True, blank=True )
    email=models.EmailField()
    address=models.CharField(max_length=200) 
    hospital_name=models.CharField(max_length=200, default='')
    
    class Meta:
        verbose_name = "Story"
        verbose_name_plural = "Story"
        

#map for neuro hospital
class map(models.Model):
    address=models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.address        