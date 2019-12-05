# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Company(models.Model):
    workStatus = (
    ('1', 'Active'),
    ('2', 'InActive'),
    )
    companyname = models.CharField(max_length=50, blank=True, null=True)
    company_address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.IntegerField(max_length=20, blank=True, null=True)
    personal_email = models.EmailField(max_length=30, blank=True, null=True)
    company_email = models.EmailField(max_length=30, blank=True, null=True)
    workstatus = models.CharField(max_length=50,choices=workstatus, blank=True, null=True)
    uan_number = models.IntegerField(max_length=20, blank=True, null=True)
    date_of_joining = models.DateTimeField(max_length=15, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    employee_id = models.CharField(max_length=20, blank=True, null=True)
    employee_desigination = models.CharField(max_length=20, blank=True, null=True)
    
