# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import JsonResponse
import json
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.http import JsonResponse
from django.template import loader
from employee.models import *
from django.shortcuts import render

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Login(APIView):
    def post(self, request, *args, **kwargs):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username, password=password)
        print(username, password)
        if user is not None:
            try:
                print("Success")
                #employee = Users.objects.get(username=username)
                return JsonResponse({'status': 200, 'user':username}, status=200)
            except:
                return JsonResponse({'status': 403}, status=403)
        else:
            return JsonResponse({'status': 403}, status=403)




@method_decorator(csrf_exempt, name='dispatch')
class Registration(View):
    def get(self, request, *args, **kwargs):
        data_obj=Employee.objects.all()
        list=[]
        for i in range(len(data_obj)):
            data={
                "first_name":data_obj[i].first_name,
                "middle_name":data_obj[i].middle_name,
                "last_name":data_obj[i].last_name,
                "father_name":data_obj[i].father_name,
                "mother_name":data_obj[i].mother_name,
                "gender":data_obj[i].gender,
                "religion":data_obj[i].religion,
                "residential_address":data_obj[i].residential_address,
                "martial_status":data_obj[i].martial_status,
                "employee_id":data_obj[i].employee_id,
                "employee_designation":data_obj[i].employee_designation,
                "pan_number":data_obj[i].pan_number,
                "passport_number":data_obj[i].passport_number,
                "bank_name":data_obj[i].bank_name,
                "branch_name":data_obj[i].branch_name,
                "bankaccount_number":data_obj[i].bankaccount_number,
                "bankifsc_code":data_obj[i].bankifsc_code,
            }
            list.append(data)

        dump = json.dumps(list)
        print(data_obj);
        return HttpResponse(dump, content_type='application/json')
    def post(self, request, *args, **kwargs):
        print("POST")
        first_name=request.POST.get('firstName')
        middle_name=request.POST.get('middleName')
        last_name=request.POST.get('lastName')
        father_name=request.POST.get('fatherName')
        mother_name=request.POST.get('motherName')
        gender=request.POST.get('gender')
        religion=request.POST.get('religion')
        residential_address=request.POST.get('residential_address')
        martial_status=request.POST.get('martialStatus')
        employee_id=request.POST.get('employeeId')
        employee_designation=request.POST.get('employeeDesignation')
        pan_number=request.POST.get('panNumber')
        passport_number=request.POST.get('passportNumber')
        bank_name=request.POST.get('bank_name')
        branch_name=request.POST.get('branch_name')
        bankaccount_number=request.POST.get('bankaccount_number')
        bankifsc_code=request.POST.get('bankifsc_code')
        print(first_name, middle_name, last_name, father_name, mother_name, gender,religion,residential_address, martial_status, employee_id, employee_designation, pan_number, passport_number, bank_name, branch_name, bankaccount_number, bankifsc_code)
        reg_obj=Employee()
        reg_obj.first_name=first_name
        reg_obj.middle_name=middle_name
        reg_obj.last_name=last_name
        reg_obj.father_name=father_name
        reg_obj.mother_name=mother_name
        reg_obj.gender=gender
        reg_obj.religion=religion
        reg_obj.residential_address=residential_address
        reg_obj.martial_status=martial_status
        reg_obj.employee_id=employee_id
        reg_obj.employee_designation=employee_designation
        reg_obj.pan_number=pan_number
        reg_obj.passport_number=passport_number
        reg_obj.bank_name=bank_name
        reg_obj.branch_name=branch_name
        reg_obj.bankaccount_number=bankaccount_number
        reg_obj.bankifsc_code=bankifsc_code
        reg_obj.save()

        return HttpResponse("Registration Success")
