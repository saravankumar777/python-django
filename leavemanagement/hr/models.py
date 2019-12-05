# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Hr(models.Model):
    leaveType = (
        ('1', 'causal'),
        ('2', 'sick'),
        ('3', 'maternity'),
    )
    FromSessionType = (
    ('1', 'FirstSession'),
    ('2', 'secondSession'),
    )
    ToSessionType = (
    ('1', 'FirstSession'),
    ('2', 'secondSession'),
    )
    approvedBy= (
    ('1', 'HR'),
    ('2', 'MANAGER'),
    ('3','TEAMLEADER')
    )
    workStatus = (
    ('1', 'Active'),
    ('2', 'InActive'),
    )
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    bankdetails = models.ForeignKey(Bankdetails,on_delete=models.CASCADE)
    salarydetails = models.ForeignKey(Salarydetails,on_delete=models.CASCADE)
    education = models.ForeignKey(Education,on_delete=models.CASCADE)
    uan_number = models.IntegerField(max_length=20, blank=True, null=True)
    date_of_joining = models.DateTimeField(max_length=15, blank=True, null=True)
    workStatus = models.CharField(max_length=20,choices=workStatus, blank=True, null=True)
    department = models.CharField(max_length=20, blank=True, null=True)
    employee_id = models.CharField(max_length=20, blank=True, null=True)
    employee_desigination = models.CharField(max_length=20,choices=employee_desigination)

class Leave(models.model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=50, blank=True, null=True)
    leaveType = models.CharField(max_length=20,choices=leaveType)
    FromDate = models.DateTimeField('Date - format : YYYY-MM-DD',blank=True,null=True)
    ToDate = models.DateTimeField('Date - format : YYYY-MM-DD',blank=True,null=True)
    FromSessionType = models.CharField(max_length=50,choices=FromSessionType)
    ToSessionType = models.CharField(max_length=50,choices=ToSessionType)
    approvedBy = models.CharField(max_length=50,choices=approvedBy)
