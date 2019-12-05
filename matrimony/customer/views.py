# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
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
from customer.models import *

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
        data_obj=Customer.objects.all()
        list=[]
        for i in range(len(data_obj)):
            data={
                "first_name":data_obj[i].first_name,
                "age":data_obj[i].age,
                "last_name":data_obj[i].last_name,
                "height":data_obj[i].height,
                "color":data_obj[i].color,
                "religion":data_obj[i].religion,
                #"caste":data_obj[i].caste,
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
        age=request.POST.get('age')
        height=request.POST.get('height')
        color=request.POST.get('color')
        religion=request.POST.get('religion')
        caste=request.POST.get('caste')
        print(first_name, last_name, age, middle_name, height, color,religion,caste)
        reg_obj=Customer()
        reg_obj.first_name=first_name
        reg_obj.middle_name=middle_name
        reg_obj.last_name=last_name
        reg_obj.age=age
        reg_obj.height=height
        reg_obj.color=color
        reg_obj.religion=religion
        reg_obj.caste=caste
        reg_obj.save()

        return HttpResponse("Registration Success")
