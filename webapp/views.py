from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from .serializers import employeesSeializer

class employeesList(APIView):
    def get(self,req):
        employe1=employees.objects.all()
        serializer1=employeesSeializer(employe1,many=True)
        return Response(serializer1.data)

    def post(self):
        pass

        


