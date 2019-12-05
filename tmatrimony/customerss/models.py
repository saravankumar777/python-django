# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Customerss(models.Model):
    """Customer Details"""
    SKINCOLOR=(
        (1, 'FAIR'),
        (2, 'DARK'),
    )
    first_name=models.CharField(max_length=50)
    middle_name=models.CharField(max_length=50, blank=True, null=True)
    last_name=models.CharField(max_length=50)
    age=models.IntegerField(default=18)
    height=models.FloatField(blank=True, null=True)
    color=models.CharField(choices=SKINCOLOR, max_length=5, blank=True, null=True)
    religion=models.CharField(max_length=20)
    caste=models.CharField(max_length=50)
    sub_caste=models.CharField(max_length=50)
    martialStatus = (
        (1, 'Single'),
        (2, 'Married'),
        (3, 'divorced'),
    )
    martialStatus = models.CharField(max_length=25,choices=martialStatus, default='single')
    weight = models.CharField(max_length=15)
    drink = models.CharField(max_length=15)
    smoke = models.CharField(max_length=15)
    dateOfBirth = models.DateTimeField('Date of Birth/Time - format : YYYY-MM-DD HH:MM',null=True,blank=True)
    motherTongue = models.CharField(max_length=50)
    gender_choices = (
    (1, 'Male'),
    (2, 'Female'),
    )
    gender = models.CharField(max_length=50,choices=gender_choices)
    blood_group = models.CharField(max_length=20)
    placeOfBirth = models.CharField(max_length=50)
    star = models.CharField(max_length=20)
    #education&carrier
    
    education = models.CharField(max_length=50)
    education_detail = models.CharField(max_length=150)
    occupation_detail = models.CharField(max_length=100)
    annual_income = models.CharField(max_length=20,default="not specified")
    current_location = models.CharField(max_length=30)
    #Family Details
    
    father_occupation = models.CharField(max_length=50)
    mother_occupation = models.CharField(max_length=50) 
    no_of_sisters = models.IntegerField(default=0)
    no_of_brothers = models.IntegerField(default=0)
    #partner prefrences

    partner_age_min = models.IntegerField(default=0)
    partner_age_max = models.IntegerField(default=0)
    partner_Martial_status = models.CharField(max_length=25,default=0)
    partner_Height = models.CharField(max_length=25)
    partner_Religion = models.CharField(max_length=25)
    partner_Caste = models.CharField(max_length=25)
    partner_Mother_Tongue = models.CharField(max_length=25)
    partner_Education = models.CharField(max_length=25)
    

