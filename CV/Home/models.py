from asyncio.windows_events import NULL
from statistics import mode
from django.db import models

# Create your models here.
# class Entry(models.Model):
#     ID = models.CharField(max_length=10,primary_key=True)
#     name = models.CharField(max_length=50)
#     rollno = models.CharField(max_length=50)

class Top(models.Model):
    name = models.CharField(max_length=50,default=NULL)
    title = models.CharField(max_length=30,default=NULL)
    phone = models.IntegerField(max_length=11,default=NULL)
    email = models.EmailField(max_length=20,default=NULL)
    linkedin_profile = models.CharField(max_length=50,default=NULL)
    github_profile = models.CharField(max_length=50,default=NULL)
    portfolio_link = models.CharField(max_length=50,blank=True)
    content = models.CharField(max_length=1000,default=NULL)
    tenure = models.CharField(max_length=30,default=NULL)
    designation = models.CharField(max_length=50,default=NULL)
    company_name = models.CharField(max_length=50, default=NULL)
    description = models.CharField(max_length=1000,default=NULL)
    tenure1 = models.CharField(max_length=30, blank=True)
    designation1 = models.CharField(max_length=50, blank=True)
    company_name1 = models.CharField(max_length=50, blank=True)
    description1 = models.CharField(max_length=1000,blank=True)
    tenure2 = models.CharField(max_length=30,blank=True)
    designation2 = models.CharField(max_length=50,blank=True)
    company_name2 = models.CharField(max_length=50, blank=True)
    description2 = models.CharField(max_length=1000,blank=True)
    period = models.CharField(max_length=30,default=NULL)
    degree = models.CharField(max_length=50,default=NULL)
    institute_name = models.CharField(max_length=50,default=NULL)
    academic_details = models.CharField(max_length=1000, default=NULL)
    skills = models.CharField(max_length=100,default=NULL)
    skills1 = models.CharField(max_length=100,default=NULL)
    skills2 = models.CharField(max_length=100,default=NULL)
    certificate_name = models.CharField(max_length=200, default=NULL)
    certificate_name1 = models.CharField(max_length=200, default=NULL)
    certificate_name2 = models.CharField(max_length=200, default=NULL)
    
    



#run migrate because changes made


    