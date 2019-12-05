# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    martialStatus = (
        ('1', 'Single'),
        ('2', 'Married'),
        ('3', 'divorced'),
    )
    gender_choices = (
    ('1', 'Male'),
    ('2', 'Female'),
    )
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    religion = models.CharField(max_length=20, blank=True, null=True)
    gender = models.CharField(max_length=50,choices=gender_choices, blank=True, null=True)
    present_residential_address = models.CharField(max_length=100, blank=True, null=True)
    permanent_residential_address = models.CharField(max_length=100, blank=True, null=True)
    martialStatus = models.CharField(max_length=25,choices=martialStatus, default='1')
    DateOfBirth = models.DateTimeField('Date of Birth/Time - format : YYYY-MM-DD HH:MM',blank=True,null=True)
    mobile_number = models.IntegerField(default=0, blank=True, null=True)
    email = models.EmailField(max_length=30, blank=True, null=True)
    alternativemobile_number = models.IntegerField(default=0)
    employee_id=models.CharField(max_length=20, blank=True, null=True)
    employee_desigination = models.CharField(max_length=20, blank=True, null=True)
    permanentAccount_number = models.IntegerField(default=0, blank=True, null=True)
    date_of_joining = models.DateTimeField(max_length=15, blank=True, null=True)
    passport_number = models.IntegerField(default=0, blank=True, null=True)

class Bankdetails(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    bankaccount_number = models.IntegerField(default=0, blank=True, null=True)
    bank_name = models.CharField(max_length=20, blank=True, null=True)
    branch_name = models.CharField(max_length=20, blank=True, null=True)
    ifsc_code = models.IntegerField(default=0, blank=True, null=True)

class Salarydetails(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    annual_ctc = models.IntegerField(default=0, blank=True, null=True)
    basic = models.IntegerField(default=0, blank=True, null=True)   
    other_allowances = models.IntegerField(default=0, blank=True, null=True)
    pf_employee_contribution = models.IntegerField(default=0, blank=True, null=True)
    esi = models.IntegerField(default=0, blank=True, null=True)

class Employeewitness(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    father_name = models.CharField(max_length=50, blank=True, null=True)
    mother_name = models.CharField(max_length=50, blank=True, null=True)
    mobile_number = models.IntegerField(default=0, blank=True, null=True)	

class Education(models.Model):    
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    education = models.CharField(max_length=50, blank=True, null=True)
    education_detail = models.CharField(max_length=150, blank=True, null=True)
    degree_certificate = models.FileField(upload_to='uploads/', null=True)
    college_certificate = models.FileField(upload_to='uploads/', null=True)
    school_certificate = models.FileField(upload_to='uploads/', null=True)
