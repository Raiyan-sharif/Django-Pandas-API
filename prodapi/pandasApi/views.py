from django.shortcuts import render
from . import dataRetrieve
from django.http import JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
# Create your views here.

class DriverClass(APIView):
    def get(self,request):
        if request.method == "GET":
            data = request.GET.get("data")
            result = dataRetrieve.RetieveData.test(data)

            return result