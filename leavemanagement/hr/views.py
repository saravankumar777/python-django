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
from hr.models import *
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

