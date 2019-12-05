from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    ###user Details###
    first_name=models.CharField(max_length=20)
    middle_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gmail=models.CharField(max_length=20)
    mobile_number=models.IntegerField()
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    relationship_status=models.CharField(max_length=20)
    bio=models.CharField(max_length=50)
    date_of_birth=models.CharField(max_length=20)
    education=models.CharField(max_length=50)
    work_details=models.CharField(max_length=50)
    re_enterpassword=models.CharField(max_length=50)
